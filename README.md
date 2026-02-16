# file-watchdog
Python 3.14 – file system Watchdog wrapper.

## Install

```
pip install -r requirements.txt
```

## Usage

Pass the directory path you want to monitor as an argument:

```
python file-watchdog.py <DIRECTORY_PATH>
```

Examples:

Windows:
```
python file-watchdog.py "C:\Users\User\Documents"
```

macOS / Linux:
```
python file-watchdog.py /Users/user/Documents
````

Before monitoring starts, the script will print whether the path:
- was found or not found,
- is a directory (not a file),
- is accessible (permission check).

## Output

* Events are logged to the console in the following format:
	```
	[HEX_TIMESTAMP] event_type (e.g., modified): path\to\file.log
	```
* Events are also saved to a log file named `watchdog_events_<timestamp>.log`, e.g., `watchdog_events_6613a3f1.log`.
* The log file is created in the **current working directory**.
* Log file entries use ISO timestamp format:
	```
	[2024-04-02T12:34:56.789012] event_type (e.g., modified): path\to\file.log
	```

## Finishing up

Press `Ctrl+C` to stop monitoring.

## See also
*My other small but snappy Python tools and automation,*

* [github-stargazers](https://github.com/TAbdiukov/github-stargazers) – Python 3.13 – Github Stargazer Scraper.
* [img2pdf_helper](https://github.com/TAbdiukov/img2pdf_helper) – Simplify img2pdf configuration and usage.
* **<ins>file-watchdog</ins>** – Python 3.14 – file system Watchdog wrapper.

----------------------------------
**Tim Abdiukov**

