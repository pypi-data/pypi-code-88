import pathlib
import sys

import qtmodern.styles
import qtmodern.windows
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
# fmt: off
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QFileDialog,
                             QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QRadioButton, QScrollArea,
                             QVBoxLayout, QWidget)

import dupesearch

# fmt: on


class DuplicateRemover(QObject):
    finished = pyqtSignal(list)
    progress = pyqtSignal(int)

    def __init__(self, folder):
        super().__init__()
        self.folder = folder

    def run(self):
        """Long-running task."""
        res = dupesearch.get_duplicate_files(self.folder)
        self.finished.emit(res)


class PhotoChoice(QWidget):
    def __init__(self, button_group, photo_path):
        super().__init__()

        self.photo_path = photo_path

        layout = QHBoxLayout()

        self.button = QRadioButton()
        button_group.addButton(self.button)
        layout.addWidget(self.button)

        pixmap = QPixmap(photo_path)
        pixmap = pixmap.scaledToHeight(120)
        image = QLabel()
        image.setPixmap(pixmap)
        layout.addWidget(image)

        folder = QLabel(photo_path)
        layout.addWidget(folder)

        self.setLayout(layout)


class DuplicateGroup(QWidget):
    def __init__(self, photo_paths):
        super().__init__()

        self.photos = []
        layout = QHBoxLayout()
        self.buttons = QButtonGroup()
        for path in photo_paths:
            photo = PhotoChoice(self.buttons, path)
            layout.addWidget(photo)
            self.photos.append(photo)

        self.photos[0].button.setChecked(True)
        self.setLayout(layout)


class PhotoSelection(QWidget):
    def __init__(self, result):
        super().__init__()

        layout = QVBoxLayout()
        self.duplicate_groups = []

        for group in result:
            widget = DuplicateGroup(group)

            layout.addWidget(widget)
            self.duplicate_groups.append(widget)

        self.setLayout(layout)


class Result(QMainWindow):
    def __init__(self, result):
        super().__init__()

        self.setWindowTitle("Duplicates Found")

        widget = QWidget()

        layout = QVBoxLayout()
        widget.setLayout(layout)

        title = QLabel(
            "<font size=4>"
            f"Found {len(result)} groups of duplicates, and {sum(len(i)-1 for i in result)}"
            " duplicate photos in total.<br>"
            "Select the photos from each duplicate group you would like to keep:"
            "</font>"
        )
        layout.addWidget(title)

        self.photo_list = PhotoSelection(result)
        photo_scroller = QScrollArea()
        photo_scroller.setWidget(self.photo_list)

        layout.addWidget(photo_scroller)

        delete_button = QPushButton("Delete duplicates")
        delete_button.clicked.connect(self.delete_duplicates)
        layout.addWidget(delete_button)

        self.setCentralWidget(widget)

    def delete_duplicates(self):
        to_delete = []
        for group in self.photo_list.duplicate_groups:
            for photo in group.photos:
                print(photo.photo_path, photo.button.isChecked())


class SetupWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Duplicate Remover")

        main = QWidget()
        layout = QVBoxLayout()
        main.setLayout(layout)
        self.setCentralWidget(main)

        self.title = QLabel("Image Duplicate Remover")
        layout.addWidget(self.title)

        self.choose_folder_button = QPushButton("Choose Root Folder")
        self.choose_folder_button.clicked.connect(self.choose_folder)
        layout.addWidget(self.choose_folder_button)

        self.chosen_folder_display = QLineEdit()
        self.chosen_folder_display.setDisabled(True)
        layout.addWidget(self.chosen_folder_display)
        self.folder = pathlib.Path(
            r"C:\Users\zoran\Documents\duplicatetestphotos"  # Default for testing
        )

        self.run_button = QPushButton("Find Duplicates")
        layout.addWidget(self.run_button)
        self.run_button.clicked.connect(self.run)

    def choose_folder(self):
        self.folder = pathlib.Path(
            QFileDialog.getExistingDirectory(self, "Select Directory")
        )
        self.chosen_folder_display.setText(str(self.folder))
        print(self.folder)

    def run(self):
        self.thread = QThread()
        self.worker = DuplicateRemover(str(self.folder.absolute()))
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.open_photos_window)

        self.thread.start()

    def open_photos_window(self, result):
        self.dialog = Result(result=result)
        self.dialog.show()


if __name__ == "__main__":
    app = QApplication([])
    qtmodern.styles.dark(app)

    main = SetupWindow()
    main.show()
    sys.exit(app.exec())
