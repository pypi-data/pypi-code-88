from pathlib import Path
from typing import Iterable, List

from sett import APP_NAME_SHORT
from .component import (
    SelectionAction,
    MandatoryLabel,
    show_warning,
    ToolBar,
    Action,
)
from .pyside import QtWidgets, QtCore, QtGui, QAction, open_window


class FileSelectionWidget(QtWidgets.QGroupBox):
    """File selection widget"""

    def __init__(self, label_text, parent, name_filter=None):
        super().__init__(parent)
        self.path = str(Path.home())
        self.name_filter = name_filter

        self.file_list_model = QtCore.QStringListModel()
        self.file_list_view = QtWidgets.QListView(self)
        self.file_list_view.setModel(self.file_list_model)
        self.file_list_view.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.file_list_view.setLayout(QtWidgets.QVBoxLayout())

        toolbar = ToolBar("Add files", self)
        for action in self._create_actions():
            toolbar.addAction(action)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(MandatoryLabel(label_text))
        layout.addWidget(toolbar)
        layout.addWidget(self.file_list_view)

        self.setAcceptDrops(True)

    # pylint: disable=no-self-use
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        self._update_paths(url.toLocalFile() for url in event.mimeData().urls())

    def get_list(self) -> List[str]:
        """Returns the paths."""
        return self.file_list_model.stringList()

    def _create_actions(self) -> List[QtWidgets.QAbstractButton]:
        return [
            self._create_add_files_action(),
            self._create_remove_selected_action(),
            self._create_clear_list_action(),
        ]

    def _create_add_files_action(self) -> QAction:
        action = Action(QtGui.QIcon(":icon/feather/file-plus.png"), "Add file", self)
        action.triggered.connect(self._add_files)
        return action

    def _create_remove_selected_action(self) -> QAction:
        def clear_selected() -> None:
            indices = self.file_list_view.selectedIndexes()
            for index in indices:
                self.file_list_model.removeRows(index.row(), 1)
            self.file_list_model.layoutChanged.emit()

        action = SelectionAction(
            QtGui.QIcon(":icon/feather/file-minus.png"),
            "Remove selected",
            self,
            selection_model=self.file_list_view.selectionModel(),
        )
        action.triggered.connect(clear_selected)
        return action

    def _create_clear_list_action(self) -> QtWidgets.QAbstractButton:
        def clear_list() -> None:
            # Clear the selection BEFORE resetting the model
            self.file_list_view.selectionModel().clearSelection()
            self.file_list_model.setStringList([])
            self.file_list_model.layoutChanged.emit()

        action = Action(QtGui.QIcon(":icon/feather/trash-2.png"), "Clear list", self)
        action.triggered.connect(clear_list)
        return action

    def _update_paths(self, paths: Iterable[str]) -> None:
        paths = set(filter(None, paths))
        if paths:
            self.path = Path(next(iter(paths))).parent
        self.file_list_model.setStringList(
            sorted(set(self.file_list_model.stringList()) | paths)
        )
        self.file_list_model.layoutChanged.emit()

    def _add_files(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dialog.setDirectory(str(self.path))
        if self.name_filter:
            dialog.setNameFilter(self.name_filter)
            dialog.selectNameFilter(self.name_filter)
        if open_window(dialog) == QtWidgets.QDialog.Accepted:
            self._update_paths(dialog.selectedFiles())


class DirectoryAndFileSelectionWidget(FileSelectionWidget):
    """File selection widget extension adding directory selection"""

    def __init__(self, label_text, parent):
        super().__init__(label_text, parent)

    def _create_actions(self):
        actions = super()._create_actions()
        actions.insert(1, self._create_add_directory_button())
        return actions

    def _create_add_directory_button(self):
        def add_directory():
            directory = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select directory", str(self.path)
            )
            self._update_paths((directory,))

        action = Action(
            QtGui.QIcon(":icon/feather/folder-plus.png"), "Add directory", self
        )
        action.triggered.connect(add_directory)
        return action


class ArchiveOnlyFileSelectionWidget(FileSelectionWidget):
    """File selection widget extension for selecting ZIP and TAR archives only."""

    def __init__(self, label_text, parent):
        super().__init__(label_text, parent, "Archives (*.zip *.tar)")

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        paths = [
            url.toLocalFile()
            for url in event.mimeData().urls()
            if url.toLocalFile().endswith(".zip") or url.toLocalFile().endswith(".tar")
        ]
        if paths:
            self._update_paths(paths)
        else:
            show_warning(
                APP_NAME_SHORT,
                "Failed to load files. Only '.zip.' and '.tar' archives are allowed.",
                self,
            )
