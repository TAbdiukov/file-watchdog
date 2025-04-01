#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys

from datetime import datetime
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

log_filename = f"file_events_{int(time.time()):x}.log"  # HEX Unix time

# Custom event handler class
class FileEventHandler(FileSystemEventHandler):
	def on_any_event(self, event):
		hex_time = f"{int(time.time()):x}"
		iso_time = datetime.utcnow().isoformat(timespec='microseconds')

		# to stdout
		print(f"[{hex_time}] {event.event_type}: {event.src_path}")

		with open(log_filename, 'a') as log_file:
			log_file.write(f"[{iso_time}] {event.event_type}: {event.src_path}\n")

def main():
	# Create DIRECTORY.txt if doesn't exist
	if not os.path.exists('DIRECTORY.txt'):
		with open('DIRECTORY.txt', 'w') as file:
			file.write("")  # Create an empty file
		print("Created DIRECTORY.txt. Please add a directory path to monitor.")
		sys.exit(0)

	with open('DIRECTORY.txt', 'r') as file:
		directory = file.read().strip()

	if not directory or not os.path.isdir(directory):
		print(f"Error: '{directory}' is not a valid directory.")
		sys.exit(1)

	event_handler = FileEventHandler()
	observer = Observer()
	observer.schedule(event_handler, path=directory, recursive=True)

	observer.start()
	print(f"Monitoring directory: {directory}")
	print(f"Logging to: {log_filename}")

	try:
		while True:
			time.sleep(600)
	except KeyboardInterrupt:
		observer.stop()

	observer.join()

if __name__ == "__main__":
	main()
