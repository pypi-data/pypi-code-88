import warnings
import copy

from sett import (
    APP_NAME_LONG,
    URL_READTHEDOCS,
    URL_GITLAB_ISSUES,
    APP_NAME_SHORT,
    __version__,
    URL_GITLAB,
    VERSION_WITH_DEPS,
)
from .component import show_warning, is_macos
from .decrypt_tab import DecryptTab
from .encrypt_tab import EncryptTab
from .keys_tab import KeysTab
from .model import AppData
from .parallel import Worker
from .pyside import QtCore, QtGui, QtWidgets, QAction, open_window
from .keys_refresh import load_authority_key_threaded
from .settings_tab import SettingsTab, config_to_settings
from .transfer_tab import TransferTab
from ..core.versioncheck import check_version
from ..utils.config import load_config, save_config, config_to_dict

QtCore.QThreadPool.globalInstance().setExpiryTimeout(-1)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = f"{APP_NAME_LONG} ({__version__})"
        self.app_data = AppData(config=self.get_config())
        self.config_on_disk = copy.deepcopy(self.app_data.config)

        self.setWindowTitle(self.title)
        self.setMinimumSize(QtCore.QSize(900, 900))
        self.add_menu()
        self.add_tabs()
        self.add_status_bar()
        self.check_version()
        load_authority_key_threaded(self.app_data)

    def get_config(self):
        with warnings.catch_warnings(record=True) as w:
            config = load_config()
            if w:
                show_warning(
                    "Configuration Error",
                    "\n".join(format(warning.message) for warning in w),
                    self,
                )
        return config

    def add_tabs(self):
        tab_keys = KeysTab(self)  # FIXME created first to populate gpg keys
        tab_encrypt = EncryptTab(self)
        tab_decrypt = DecryptTab(self)
        tab_transfer = TransferTab(self)
        tab_settings = SettingsTab(self)

        tabs = QtWidgets.QTabWidget()
        tabs.addTab(tab_encrypt, QtGui.QIcon(":icon/feather/lock.png"), "&Encrypt")
        tabs.addTab(tab_transfer, QtGui.QIcon(":icon/feather/send.png"), "&Transfer")
        tabs.addTab(tab_decrypt, QtGui.QIcon(":icon/feather/unlock.png"), "&Decrypt")
        tabs.addTab(tab_keys, QtGui.QIcon(":icon/feather/key.png"), "&Keys")
        tabs.addTab(
            tab_settings, QtGui.QIcon(":icon/feather/settings.png"), "&Settings"
        )

        self.setCentralWidget(tabs)

    def add_status_bar(self):
        self.status = QtWidgets.QStatusBar()
        self.setStatusBar(self.status)

    def add_menu(self):
        action_exit = QAction(QtGui.QIcon(":icon/feather/log-out.png"), "&Exit", self)
        action_exit.setShortcut(QtGui.QKeySequence("Ctrl+Q"))
        action_exit.setStatusTip("Exit application")
        action_exit.triggered.connect(self.close)

        menu = self.menuBar()
        menu.setNativeMenuBar(not is_macos())
        menu_file = menu.addMenu("&File")
        menu_file.addAction(action_exit)

        action_help = QAction(
            QtGui.QIcon(":icon/feather/book-open.png"), "&Documentation", self
        )
        action_help.setStatusTip("Open online documentation")
        action_help.setShortcut(QtGui.QKeySequence(QtGui.QKeySequence.HelpContents))
        action_help.triggered.connect(open_url(URL_READTHEDOCS))

        action_bug_report = QAction(
            QtGui.QIcon(":icon/feather/alert-triangle.png"), "&Report an Issue", self
        )
        action_bug_report.setStatusTip("Open online bug report form")
        action_bug_report.triggered.connect(open_url(URL_GITLAB_ISSUES))

        action_about = QAction(QtGui.QIcon(":icon/feather/info.png"), "&About", self)
        action_about.setStatusTip("Show info about application")
        action_about.triggered.connect(self.show_about)

        menu_help = menu.addMenu("&Help")
        menu_help.addAction(action_help)
        menu_help.addAction(action_bug_report)
        menu_help.addAction(action_about)

    def closeEvent(self, event):
        if config_to_settings(self.app_data.config) != config_to_settings(
            self.config_on_disk
        ):
            reply = QtWidgets.QMessageBox.question(
                self,
                "Persist changed settings?",
                "You made changes to settings you did not persist yet.\nDo you "
                "want to permanently persist them to your sett configuration file?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No,
            )
            if reply == QtWidgets.QMessageBox.Yes:
                save_config(config_to_dict(self.app_data.config))

        if self.app_data.config.gui_quit_confirmation:
            reply = QtWidgets.QMessageBox.question(
                self,
                "Quit",
                "Do you really want to quit?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No,
            )
            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def check_version(self):
        if self.app_data.config.offline or not self.app_data.config.check_version:
            return

        def get_warnings():
            with warnings.catch_warnings(record=True) as w:
                check_version(self.app_data.config.repo_url, gui_formatting=True)
                return "\n".join(format(warning.message) for warning in w)

        worker = Worker(
            get_warnings,
            report_config=self.app_data.config,
        )
        worker.signals.result.connect(lambda x: x and show_warning(self.title, x, self))
        QtCore.QThreadPool.globalInstance().start(worker)

    def show_about(self):
        msg = QtWidgets.QMessageBox(parent=self)
        msg.setWindowTitle(f"About {APP_NAME_SHORT}")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setTextFormat(QtCore.Qt.RichText)
        msg.setText(
            f"{APP_NAME_LONG}<br>"
            f"{VERSION_WITH_DEPS}<br><br>"
            f"For documentation go to "
            f"<a href='{URL_READTHEDOCS}'>{URL_READTHEDOCS}</a><br>"
            f"To report an issue go to "
            f"<a href='{URL_GITLAB_ISSUES}'>{URL_GITLAB_ISSUES}</a><br>"
            f"Source code is available at "
            f"<a href='{URL_GITLAB}'>{URL_GITLAB}</a><br><br>"
            f"{APP_NAME_SHORT} is developed as part of the "
            f"<a href='https://sphn.ch/network/projects/biomedit/'>BioMedIT "
            f"project</a>"
        )
        msg.show()


def open_url(url: str):
    """Returns a function that will opens the specified URL in the user's
    default browser when called. The function that is returned has no
    arguments.
    :param url: URL to open.
    :returns: function that opens specifed URL.
    """

    def open_url_template():
        if not QtGui.QDesktopServices.openUrl(QtCore.QUrl(url)):
            msg_warn = QtWidgets.QMessageBox()
            msg_warn.setWindowTitle("Warning")
            msg_warn.setText(f"Unable to open URL at \n{url}.")
            msg_warn.setIcon(QtWidgets.QMessageBox.Warning)
            open_window(msg_warn)

    return open_url_template
