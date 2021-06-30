import threading
import time
from pathlib import Path

from rich.progress import BarColumn, Progress, TimeRemainingColumn
from rich.prompt import Prompt

from . import dupesearch


def get_progress_bar():
    progress_bar = Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
        "{task.completed} of {task.total} processed",
        auto_refresh=False,
    )
    return progress_bar


def ask_for_path():
    option = Prompt.ask(
        "Enter the folder path to search in (leave blank to use current directory)",
        default=Path.cwd(),
    )
    path = str(Path(option).absolute())
    print("Searching for duplicate photos at path: ", path)
    return path


def display_progress_bar(dupefinder):
    with get_progress_bar() as progress:
        finding_files = progress.add_task("Finding Files...")
        while not dupefinder.has_found_files:
            value = dupefinder.file_count
            progress.update(finding_files, completed=value, total=value)
            progress.refresh()
            time.sleep(0.1)
        value = dupefinder.file_count
        progress.update(finding_files, completed=value, total=value)
        progress.stop_task(finding_files)

        processing_files = progress.add_task(
            "Processing Files...", total=dupefinder.file_count
        )
        while not dupefinder.has_processed_files:
            progress.update(
                processing_files, completed=dupefinder.processed_count
            )
            progress.refresh()
            time.sleep(0.1)
        progress.update(processing_files, completed=dupefinder.processed_count)
        progress.stop_task(processing_files)

        finding_dupes = progress.add_task("Getting Duplicates...", start=True)
        while not dupefinder.has_finished:
            progress.refresh()
            time.sleep(0.1)
        dupes_found = len(dupefinder.duplicates)
        progress.update(finding_dupes, total=dupes_found, completed=dupes_found)
        progress.stop_task(finding_dupes)


def process_result(dupefinder):
    option = Prompt.ask(
        "What would you like to do next?",
        choices=["delete", "save", "exit"],
        default="delete",
    )
    if option == "save":
        pass
    elif option == "delete":
        thread = threading.Thread(target=dupefinder.delete_duplicates)
        thread.start()
        with get_progress_bar() as progress:
            deleting = progress.add_task("Deleting Duplicates...", total=len(dupefinder.duplicates))
            while thread.is_alive():
                progress.update(deleting, completed=100)
        thread.join()
        print("Completed!")


def main():
    path = ask_for_path()

    dupefinder = dupesearch.DuplicateFinder(path)
    thread = threading.Thread(target=dupefinder.find_duplicates)
    thread.start()
    display_progress_bar(dupefinder)
    thread.join()

    process_result(dupefinder)


if __name__ == "__main__":
    main()
