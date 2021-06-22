import logging
import os
import shutil
import sys
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, PatternMatchingEventHandler


def move_file(filepath, extension_to_directory, path):
    _, ext = os.path.splitext(filepath)
    directory_name = extension_to_directory[ext]
    directory_path = os.path.join(path, directory_name)

    if not os.path.isdir(directory_path):
        os.mkdir(directory_path)

    return shutil.move(filepath, directory_path)


def perform_initial_sorting(extension_to_directory, path):
    for filename in os.listdir(path):
        _, ext = os.path.splitext(filename)
        filepath = os.path.join(path, filename)

        if os.path.isfile(filepath) and ext in extension_to_directory:
            move_file(filepath, extension_to_directory, path)


def schedule_sorting_handler(observer, extension_to_directory, path):
    pattern_matching_event_handler = PatternMatchingEventHandler(
        patterns=[f"*{ext}" for ext in extension_to_directory.keys()]
    )
    pattern_matching_event_handler.on_created = lambda e: move_file(
        e.src_path, extension_to_directory, path
    )

    observer.schedule(pattern_matching_event_handler, path, recursive=False)

    return observer


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
path = sys.argv[1] if len(sys.argv) > 1 else "."

directory_to_extensions = {
    "documents": {
        ".doc",
        ".docx",
        ".ods",
        ".odt",
        ".pdf",
        ".ppt",
        ".pptx",
        ".txt",
        ".xls",
        ".xlsx",
    },
    "images": {".gif", ".png", ".jpeg", ".jpg"},
}
extension_to_directory = {
    pat: ext
    for ext, patterns in directory_to_extensions.items()
    for pat in patterns
}

# sort directory
perform_initial_sorting(extension_to_directory, path)

# set up observer
observer = Observer()

logging_event_handler = LoggingEventHandler()
observer.schedule(logging_event_handler, path, recursive=False)
schedule_sorting_handler(observer, extension_to_directory, path)

# wait for events
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
