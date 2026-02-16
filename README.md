# fs-watchdog
File system Watchdog wrapper (CLI). Monitors a directory and logs events.

## Install

From PyPI:
```bash
pip install fs-watchdog
````

(Recommended for CLI tools)

```bash
pipx install fs-watchdog
```

## Usage

```bash
fs-watchdog <DIRECTORY_PATH>
```

Examples:

Windows:

```bash
fs-watchdog "C:\Users\User\Documents"
```

macOS / Linux:

```bash
fs-watchdog /Users/user/Documents
```

You can also run as a module:

```bash
python -m file_watchdog <DIRECTORY_PATH>
```

## Output

* Events are logged to the console in the following format:

  ```
  [HEX_TIMESTAMP] event_type: path/to/file
  ```
* Events are also saved to a log file named `watchdog_events_<timestamp>.log`.
* The log file is created in the **current working directory**.
* Log file entries use ISO timestamp format (UTC, Z suffix):

  ```
  [2024-04-02T12:34:56.789012Z] event_type: path/to/file
  ```

## Finishing up

Press `Ctrl+C` to stop monitoring.

## See also
*My other small but snappy Python tools and automation,*

* [github-stargazers](https://github.com/TAbdiukov/github-stargazers) – Python 3.13 – Github Stargazer Scraper.
* [img2pdf_helper](https://github.com/TAbdiukov/img2pdf_helper) – Simplify img2pdf configuration and usage.
* **<ins>fs-watchdog</ins>** – Python 3.14 – file system Watchdog wrapper.

----------------------------------
**Tim Abdiukov**

