from functools import partial
from pathlib import Path
from typing import Callable, Optional, Tuple

from .model import AppData
from .parallel import Worker
from .pyside import QtCore, QtWidgets, QAction, QtGui, open_window
from ..utils.progress import ProgressInterface

EXTRA_HEIGHT = 1
MACOS_TOOLTIP_BG_COLOR = "#ffffca"


def is_macos():
    return QtCore.QSysInfo.productType() in ("osx", "macos")


class Action(QAction):
    def __init__(
        self,
        icon: QtGui.QIcon,
        text: str,
        parent: Optional[QtWidgets.QWidget] = None,
    ):
        super().__init__(icon, text, parent)
        if is_macos():
            self.setToolTip(
                f"<p style='background-color: {MACOS_TOOLTIP_BG_COLOR};'>{text}</p>"
            )


class SpinBox(QtWidgets.QSpinBox):
    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        super().__init__(parent)
        if is_macos():
            self.setMinimumHeight(self.sizeHint().height() + EXTRA_HEIGHT)


class LineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        super().__init__(parent)
        if is_macos():
            self.setMinimumHeight(self.sizeHint().height() + EXTRA_HEIGHT)


class ToolBar(QtWidgets.QToolBar):
    def __init__(self, title: str, parent: Optional[QtWidgets.QWidget] = None):
        super().__init__(title, parent)
        if is_macos():
            self.setStyleSheet("background: transparent;border-width: 0px;")
        self.setIconSize(QtCore.QSize(20, 20))


class MandatoryLabel(QtWidgets.QLabel):
    """A label extension which appends a '*' to label's end to mark the field as required."""

    def __init__(self, label: str):
        super().__init__(label + " <sup><font color='red'>*</font></sup>")


class SelectionButton(QtWidgets.QPushButton):
    """A push button extension which connects this button to given selection model.

    The button is disabled by default. And gets enabled when the selection has, at least,
    one selected row.
    """

    def __init__(self, label: str, selection_model: QtCore.QItemSelectionModel):
        super().__init__(label)
        self.setEnabled(False)
        self._selection_model = selection_model
        selection_model.selectionChanged.connect(self.selection_changed)

    def selection_changed(self):
        # Following works better than using 'QItemSelection', especially in cases
        # where multiple selection is possible
        self.setEnabled(bool(len(self._selection_model.selectedRows())))


class SelectionAction(Action):
    """An action extension which connects this action to given selection model.

    The action is disabled by default. And gets enabled when the selection has, at least,
    one selected row.
    """

    def __init__(self, *args, selection_model: QtCore.QItemSelectionModel):
        super().__init__(*args)
        self.setEnabled(False)
        self._selection_model = selection_model
        selection_model.selectionChanged.connect(self.selection_changed)

    def selection_changed(self):
        # Following works better than using 'QItemSelection', especially in cases
        # where multiple selection is possible
        self.setEnabled(bool(len(self._selection_model.selectedRows())))


class GuiProgress(QtCore.QObject, ProgressInterface):
    updated = QtCore.Signal(int)

    def __init__(self):
        super().__init__()
        self.n = 0

    def update(self, completed_fraction):
        self.n = completed_fraction
        self.updated.emit(round(completed_fraction * 100, 0))

    def get_completed_fraction(self):
        return self.n


class ConsoleWidget(QtWidgets.QGroupBox):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.textbox = QtWidgets.QTextEdit()
        self.textbox.setReadOnly(True)
        btn_clear_console = QtWidgets.QPushButton(
            QtGui.QIcon(":icon/feather/slash.png"), ""
        )
        btn_clear_console.setToolTip("Clear console")
        btn_clear_console.clicked.connect(self.clear)
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.textbox)
        layout.addWidget(btn_clear_console, alignment=QtCore.Qt.AlignTop)

    def clear(self) -> None:
        self.textbox.clear()

    def append(self, text: str) -> None:
        self.textbox.append(text)

    def write(self, text: str) -> None:
        self.textbox.append(text)


class PathInput:
    """Path selection widget with a select button and a show path field."""

    def __init__(self, directory=True, path: Optional[Path] = Path.home(), parent=None):
        self.parent = parent
        self.text = LineEdit(parent)
        self.text.setReadOnly(True)
        self.btn = QtWidgets.QPushButton(
            QtGui.QIcon(f":icon/feather/{'folder' if directory else 'file'}.png"),
            "",
        )
        self.btn.setToolTip("Change location")
        self.btn.clicked.connect(partial(self._update_location, directory))
        # Additional action to clear the selected path
        self.btn_clear = QtWidgets.QPushButton(
            QtGui.QIcon(":icon/feather/slash.png"), ""
        )
        self.btn_clear.setToolTip("Clear location")
        self.btn_clear.clicked.connect(self._clear_location)
        self.update_path(path)

    def update_path(self, path: Optional[Path]):
        self.path = path
        self.text.setText("" if path is None else str(path))
        self.text.editingFinished.emit()

    def _update_location(self, directory: bool):
        if self.path and self.path.exists():
            location = self.path if self.path.is_dir() else self.path.parent
        else:
            location = Path.home()
        if directory:
            new_path = QtWidgets.QFileDialog.getExistingDirectory(
                self.parent, "Select Directory", str(location)
            )
        else:
            new_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                self.parent, "Select File", str(location)
            )
        if new_path:
            self.update_path(Path(new_path))

    def _clear_location(self):
        self.update_path(None)

    @property
    def status_tip(self) -> str:
        return self.text.statusTip()

    @status_tip.setter
    def status_tip(self, msg: str):
        self.text.setStatusTip(msg)

    def on_path_change(self, fn: Callable[[Optional[Path]], None]) -> None:
        """Run callback when path changes."""
        self.text.editingFinished.connect(lambda: fn(self.path))


class TabMixin:
    def create_console(self):
        self.console = ConsoleWidget("Console", self)

    def create_progress_bar(self):
        self.progress_bar = QtWidgets.QProgressBar(self)

    @staticmethod
    def _create_disabled_button(action_name: str) -> QtWidgets.QPushButton:
        button = QtWidgets.QPushButton(action_name)
        button.setEnabled(False)
        return button

    def set_buttons_enabled(self, enabled: bool):
        self.btn_run.setEnabled(enabled)
        self.btn_test.setEnabled(enabled)

    def create_run_panel(self, panel_name: str, action: Callable, action_name: str):
        self.run_panel = QtWidgets.QGroupBox(panel_name)
        layout = QtWidgets.QHBoxLayout(self.run_panel)
        self.btn_test = TabMixin._create_disabled_button("Test")
        # On pressed button, make sure that the focus switches to that button (Mac specific issue)
        self.btn_test.pressed.connect(self.btn_test.setFocus)
        self.btn_test.clicked.connect(partial(action, dry_run=True))
        self.btn_run = TabMixin._create_disabled_button(action_name)
        # On pressed button, make sure that the focus switches to that button (Mac specific issue)
        self.btn_run.pressed.connect(self.btn_run.setFocus)
        self.btn_run.clicked.connect(action)
        layout.addWidget(self.btn_test)
        layout.addWidget(self.btn_run)

    def add_worker_actions(self, worker: Worker):
        """Attach GUI-updating signals to worker"""
        worker.signals.started.connect(lambda: self.run_panel.setEnabled(False))
        worker.signals.logging.connect(self.console.write)
        worker.signals.error.connect(lambda e: self.console.append(str(e[1])))
        worker.signals.finished.connect(lambda: self.run_panel.setEnabled(True))


def run_dialog(parent, msg: str, password: bool = True):
    dialog_pwd = QtWidgets.QInputDialog(parent)
    dialog_pwd.setLabelText(msg)
    dialog_pwd.setWindowTitle("SETT")
    if password:
        dialog_pwd.setTextEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
    if (
        open_window(dialog_pwd) != QtWidgets.QDialog.Accepted
        or not dialog_pwd.textValue()
    ):
        return None
    return dialog_pwd.textValue()


def warning_callback(
    title: str, parent: Optional[QtWidgets.QWidget] = None
) -> Callable:
    msg_warn = warning_dialog(title, parent=parent)

    def _show_warning(msg: str):
        # add an extra line break so that text is easier to read in GUI.
        msg_warn.setText(format(msg).replace("\n", "\n\n"))
        open_window(msg_warn)

    return _show_warning


def warning_dialog(
    title: str, text: Optional[str] = None, parent: Optional[QtWidgets.QWidget] = None
) -> QtWidgets.QMessageBox:
    msg = QtWidgets.QMessageBox(parent=parent)
    msg.setWindowTitle(title)
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    if text is not None:
        msg.setText(text)
    return msg


def show_warning(title: str, text: str, parent: Optional[QtWidgets.QWidget] = None):
    warning_dialog(title, text, parent).show()


def create_verify_dtr_checkbox(
    app_data: AppData, field_name: str, parent: Optional[QtWidgets.QWidget] = None
) -> QtWidgets.QCheckBox:
    verify_dtr = QtWidgets.QCheckBox("Verify DTR ID", parent)
    verify_dtr.setStatusTip("Verify DTR (Data Transfer Request) ID")
    verify_dtr.setChecked(not app_data.config.offline and app_data.encrypt_verify_dtr)
    if app_data.config.offline:
        verify_dtr.setEnabled(not app_data.config.offline)
        verify_dtr.setStatusTip(
            "Verifying Transfer Request ID in offline mode is not possible"
        )
    verify_dtr.stateChanged.connect(
        lambda state: setattr(app_data, field_name, state == QtCore.Qt.Checked)
    )
    return verify_dtr


class FieldMapping:
    def __init__(self):
        self._mapping = {}

    def bind_text(self, field_name, w):
        self._mapping[field_name] = w.setText
        return w

    def bind_checked(self, field_name, w):
        self._mapping[field_name] = w.setChecked
        return w

    def bind_value(self, field_name, w):
        self._mapping[field_name] = w.setValue
        return w

    def bind_path(self, field_name, w):
        self._mapping[field_name] = lambda p: w.update_path(p and Path(p))
        return w

    def load(self, parameters):
        for key, val in parameters.items():
            try:
                self._mapping[key](val)
            except KeyError:
                raise ValueError(
                    f"Invalid field `{key}` found in your config file"
                ) from None
        for key in set(self._mapping.keys()) - set(parameters.keys()):
            self._mapping[key](None)


def create_slider(
    minimum: int,
    maximum: int,
    initial_value: int,
    status_tip: Optional[str],
    on_change: Optional[Callable[[int], None]] = None,
    show_ticks: bool = False,
    interval: int = 1,
) -> Tuple[QtWidgets.QSlider, QtWidgets.QLabel]:
    widget_value = QtWidgets.QLabel(str(initial_value))

    slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
    slider.setMinimum(minimum)
    slider.setMaximum(maximum)
    slider.setValue(initial_value)
    slider.setTickInterval(interval)
    if status_tip is not None:
        slider.setStatusTip(status_tip)
    if show_ticks:
        slider.setTickPosition(QtWidgets.QSlider.TicksBelow)

    def update_text(value: int):
        widget_value.setText(str(value))

    slider.valueChanged.connect(update_text)
    if on_change is not None:
        slider.valueChanged.connect(on_change)

    return slider, widget_value
