import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/tuhina/Desktop/coding/P103"              # Add the path of you "Downloads" folder.
to_dir = "/Users/tuhina/Desktop/coding/P103" #Create "Document_Files" folder in your Desktop and update the path accordingly.


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("File is created/downloaded.")
    
    def on_modified(self):
        print("The file is modified")

    def on_moved(self):
        print("The file has moved")

    def on_deleted(self):
        print("The file has been deleted")

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
