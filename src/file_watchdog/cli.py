import sys
import time
import argparse
from pathlib import Path
from datetime import datetime, timezone

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, log_path: Path):
        super().__init__()
        self.log_path = log_path

    def on_any_event(self, event):
        hex_time = f"{int(time.time()):x}"
        iso_time = (
            datetime.now(timezone.utc)
            .isoformat(timespec="microseconds")
            .replace("+00:00", "Z")
        )

        # to stdout
        print(f"[{hex_time}] {event.event_type}: {event.src_path}")

        # to log file in CWD
        try:
            with open(self.log_path, "a", encoding="utf-8") as log_file:
                log_file.write(f"[{iso_time}] {event.event_type}: {event.src_path}\n")
        except OSError as e:
            # If logging fails, still keep monitoring; warn once per event.
            print(
                f"Warning: failed to write to log file '{self.log_path}': {e}",
                file=sys.stderr,
            )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="fs-watchdog",
        description="File system watchdog wrapper. Monitors a directory and logs events.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Absolute or relative path of the directory to monitor.",
    )
    return parser.parse_args(argv)


def validate_directory(raw_path: str) -> Path:
    # Normalize user input (expand ~ etc.)
    p = Path(raw_path).expanduser()

    # Resolve to an absolute path (strict=False so we can still print a clean path on failure)
    abs_p = p.resolve(strict=False)

    print(f"Checking path: {abs_p}")

    if not abs_p.exists():
        print(f"Error: path was NOT found: {abs_p}")
        raise SystemExit(1)

    if abs_p.is_file():
        print(f"Error: path exists but is a file (expected a directory): {abs_p}")
        raise SystemExit(1)

    if not abs_p.is_dir():
        print(f"Error: path exists but is not a directory: {abs_p}")
        raise SystemExit(1)

    # Permission check: can we list the directory?
    try:
        next(abs_p.iterdir(), None)
    except PermissionError:
        print(f"Error: permission denied (cannot access directory): {abs_p}")
        raise SystemExit(1)
    except OSError as e:
        print(f"Error: OS error while accessing directory '{abs_p}': {e}")
        raise SystemExit(1)

    print(f"OK: directory was found and is accessible: {abs_p}")
    return abs_p


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)

    if not args.path:
        print("Error: no path provided.\n", file=sys.stderr)
        print("Example:", file=sys.stderr)
        print(r'  fs-watchdog "C:\Users\User\Documents"', file=sys.stderr)
        print("\nHelp:", file=sys.stderr)
        print("  fs-watchdog --help", file=sys.stderr)
        raise SystemExit(2)

    directory = validate_directory(args.path)

    # Create the log filename in the CURRENT WORKING DIRECTORY
    log_filename = Path.cwd() / f"watchdog_events_{int(time.time()):x}.log"

    event_handler = FileEventHandler(log_filename)
    observer = Observer()
    observer.schedule(event_handler, path=str(directory), recursive=True)

    print(f"Monitoring directory: {directory}")
    print(f"Logging to: {log_filename}")

    try:
        observer.start()
    except Exception as e:
        print(f"Error: failed to start observer for '{directory}': {e}")
        raise SystemExit(1)

    try:
        while True:
            time.sleep(600)
    except KeyboardInterrupt:
        print("\nStopping (Ctrl+C received)...")
        observer.stop()

    observer.join()
    print("Stopped.")
