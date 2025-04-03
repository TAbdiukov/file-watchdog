# file-watchdog
Python 3.14 – file system Watchdog wrapper.

## Install

```
pip install -r requirements.txt
```

## Configure Directory

* Open or create `DIRECTORY.txt` in repo.
* Add the absolute path of the directory you want to monitor.
* Save and close the file.

## Usage

```
python watchdog.py
```

For example, if `DIRECTORY.txt` contains:

```
C:\Users\User\Documents
```

Running `watchdog.py` will monitor changes in `C:\Users\User\Documents` and log them.

## Output

* Events are logged to the console in the following format:
	```
	[HEX_TIMESTAMP] event_type (e.g., modified): path\to\file.log
	```
* Events are also saved to a log file named `file_events_<timestamp>.log`, e.g., `file_events_6613a3f1.log`.
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
