import html
from pathlib import Path
from typing import Iterator, Optional, Sequence, Callable

from sett.core.error import UserError
from .component import SelectionAction, ToolBar, LineEdit, Action, warning_callback
from .parallel import Worker
from .pyside import QtCore, QtGui, QtWidgets, QAction, open_window
from ..core import crypt
from ..core.crypt import gpg
from ..utils.config import Config
from ..workflows import (
    upload_keys as upload_keys_workflow,
    request_sigs as request_sigs_workflow,
)


class KeysTab(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threadpool = QtCore.QThreadPool.globalInstance()
        self.app_data = self.parent().app_data
        self.update_private_keys()
        self.update_public_keys()

        self.text_panel = QtWidgets.QTextEdit()
        self.text_panel.setReadOnly(True)

        self.priv_keys_view = QtWidgets.QListView()
        self.priv_keys_view.setModel(self.app_data.priv_keys_model)
        self.priv_keys_view.selectionModel().currentChanged.connect(
            self._update_display
        )

        self.pub_keys_view = QtWidgets.QListView()
        self.pub_keys_view.setModel(self.app_data.pub_keys_model)
        self.pub_keys_view.selectionModel().currentChanged.connect(self._update_display)
        self.pub_keys_view.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )

        # When item is selected clear selection in the other list
        self.priv_keys_view.selectionModel().currentChanged.connect(
            lambda: self.pub_keys_view.selectionModel().clear()
        )
        self.pub_keys_view.selectionModel().currentChanged.connect(
            lambda: self.priv_keys_view.selectionModel().clear()
        )

        action_generate_key = Action(
            QtGui.QIcon(":icon/feather/plus-square.png"),
            "Generate new private/public key",
            self,
        )
        action_generate_key.triggered.connect(lambda: KeyGenDialog(parent=self).show())
        action_refresh_keys = QAction(
            QtGui.QIcon(":icon/feather/refresh-cw.png"),
            "Refresh keys from the local keyring",
            self,
        )
        action_refresh_keys.triggered.connect(
            lambda: (
                self.update_private_keys(),
                self.update_public_keys(),
                self._update_display(
                    self.pub_keys_view.selectionModel().currentIndex()
                ),
            )
        )

        toolbar = ToolBar("Key management", self)
        toolbar.addAction(action_generate_key)
        toolbar.addSeparator()
        for action in self.create_public_keys_actions():
            toolbar.addAction(action)
        toolbar.addSeparator()
        toolbar.addAction(action_refresh_keys)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(toolbar, 0, 0, 1, 2)
        layout.addWidget(QtWidgets.QLabel("Private keys"), 1, 0)
        layout.addWidget(self.priv_keys_view, 2, 0)
        layout.addWidget(QtWidgets.QLabel("Public keys"), 1, 1)
        layout.addWidget(self.pub_keys_view, 2, 1)
        layout.addWidget(self.text_panel, 3, 0, 1, 2)
        self.setLayout(layout)

    def key_to_html(self, key: gpg.Key) -> str:
        """Represent a PGP key as an HTML string"""

        # Add key info (user ID, key ID, fingerprint, signatures).
        content = ["<table>"]
        rows = [
            ("User ID", html.escape(str(key.uids[0]))),
            ("Key ID", key.key_id),
            ("Key fingerprint", key.fingerprint),
            ("Key length", key.key_length),
        ]
        for k, v in rows:
            content.append(f"<tr><th>{k}</th><td>{v}</td></tr>")

        content.append("<tr><th>Signatures</th><td>")
        content.append(
            "<br>".join(
                [
                    f"{html.escape(str(sig.issuer_uid))} {sig.issuer_key_id} "
                    f"{sig.signature_class}"
                    for sig in key.valid_signatures
                ]
            )
        )
        content.append("</td></tr>")

        # Add key validation info: is the key signed or not.
        content.append("</table>")
        if key.key_type == gpg.KeyType.public:
            try:
                crypt.validate_pub_key(
                    key=key,
                    signee_key=self.app_data.validation_authority_key,
                    keyserver_url=self.app_data.config.keyserver_url,
                )
                if self.app_data.validation_authority_key:
                    content.append('<p class="safe">This key has been verified</p>')
                elif self.app_data.config.key_authority_fingerprint:
                    content.append(
                        '<p class="info">This key could not be verified because the '
                        "key validation authority's key ["
                        + self.app_data.config.key_authority_fingerprint
                        + "] is not available on your machine or is invalid.</p>"
                    )
                else:
                    content.append(
                        '<p class="info">This key could not be verified because no '
                        "key validation authority is defined in the setting.</p>"
                    )
            except UserError as e:
                # Note: changing "<email>" to "[email]" in the error message
                # as the text between "< >" is not rendered.
                content.append(
                    f'<p class="danger">'
                    f"{str(e).replace('<', '[').replace('>', ']')}</p>"
                )
        else:
            content.append(
                "<p>This is a private key. Private keys cannot be signed.</p>"
            )
        return "".join(content)

    @staticmethod
    def key_to_text(key: gpg.Key) -> str:
        return f"User ID: {key.uids[0]}\n" f"Fingerprint: {key.fingerprint}"

    def create_public_keys_actions(self) -> Iterator[QAction]:
        selection_model = self.pub_keys_view.selectionModel()

        def offline_action(icon: str, tip: str, selection: bool = True):
            """Force disable button in offline mode"""
            icon_obj = f":icon/feather/{icon}.png"
            if self.app_data.config.offline:
                action = Action(
                    QtGui.QIcon(icon_obj),
                    f"{tip} (not available in the offline mode)",
                    self,
                )
                action.setEnabled(False)
            else:
                if selection:
                    action = SelectionAction(
                        QtGui.QIcon(icon_obj),
                        tip,
                        self,
                        selection_model=selection_model,
                    )
                else:
                    action = Action(QtGui.QIcon(icon_obj), tip, self)
            return action

        for action, fn in (
            (
                offline_action(
                    "download-cloud",
                    "Search and download keys from the keyserver",
                    False,
                ),
                lambda: KeyDownloadDialog(parent=self).show(),
            ),
            (
                offline_action("upload-cloud", "Upload selected keys to the keyserver"),
                self.upload_key,
            ),
            (
                offline_action("pen-tool", "Request signature for the selected keys"),
                self.send_signature_request,
            ),
            (
                offline_action("rotate-cw", "Update selected keys from the keyserver"),
                self.update_keys,
            ),
            (
                SelectionAction(
                    QtGui.QIcon(":icon/feather/trash-2.png"),
                    "Delete selected keys from your computer",
                    self,
                    selection_model=selection_model,
                ),
                self.delete_keys,
            ),
            (
                Action(
                    QtGui.QIcon(":icon/feather/file-plus.png"),
                    "Import key from file",
                    self,
                ),
                self.import_key,
            ),
        ):
            action.triggered.connect(fn)
            yield action

    def update_private_keys(self):
        # Retrieve all private keys from local keyring.
        keys_private = self.app_data.config.gpg_store.list_sec_keys()
        try:
            default_key = (
                self.app_data.config.default_sender
                or self.app_data.config.gpg_store.default_key()
            )
            self.app_data.default_key_index = next(
                index
                for index, entry in enumerate(keys_private)
                if entry.fingerprint == default_key
            )
            self.app_data.encrypt_sender = default_key
        except StopIteration:
            pass
        self.app_data.priv_keys_model.set_data(
            {f"{key.uids[0]} {key.key_id}": key for key in keys_private}
        )

    def update_public_keys(self):
        # Retrieve all public keys from local keyring.
        keys_public = self.app_data.config.gpg_store.list_pub_keys(sigs=True)
        self.app_data.pub_keys_model.set_data(
            {f"{key.uids[0]} {key.key_id}": key for key in keys_public}
        )

    def update_keys(self):
        """Updated selected keys from the keyserver."""
        show_ok = ok_message("Updated keys", "Keys have been successfully updated.")
        show_warning = warning_callback("GPG key update error")

        selected_keys = [
            index.model().get_value(index).fingerprint
            for index in self.pub_keys_view.selectedIndexes()
        ]
        if selected_keys:
            worker = Worker(
                crypt.download_keys,
                selected_keys,
                self.app_data.config.keyserver_url,
                self.app_data.config.gpg_store,
                report_config=self.app_data.config,
                forward_errors=show_warning,
            )
            worker.signals.result.connect(
                lambda x: (
                    self.update_public_keys(),
                    self._update_display(
                        self.pub_keys_view.selectionModel().currentIndex()
                    ),
                    show_ok(),
                )
            )
            self.threadpool.start(worker)

    def import_key(self):
        path = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select GPG key file", str(Path.home())
        )[0]
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("GPG public key import")
        try:
            if path:
                with open(path) as fin:
                    key_data = fin.read()
                crypt.import_keys(key_data, self.app_data.config.gpg_store)
                self.update_public_keys()
                self._update_display(self.pub_keys_view.selectionModel().currentIndex())
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Key has been imported.")
                open_window(msg)
        except (UnicodeDecodeError, UserError) as e:
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(format(e))
            open_window(msg)

    def delete_keys(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Delete public key")
        msg.setText("Do you really want to delete the following public key?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg_warn = QtWidgets.QMessageBox()
        msg_warn.setWindowTitle("GPG key deletion error")
        msg_warn.setIcon(QtWidgets.QMessageBox.Warning)
        priv_keys = self.app_data.config.gpg_store.list_sec_keys()

        selected_keys = [
            index.model().get_value(index)
            for index in self.pub_keys_view.selectedIndexes()
        ]
        for key in selected_keys:
            if any(k for k in priv_keys if key.fingerprint == k.fingerprint):
                msg_warn.setText(
                    "Unable to delete key:\n\n"
                    f"{key.uids[0]}\n{key.fingerprint}\n\n"
                    "Deleting private keys (and by extension public keys "
                    "with an associated private key) is not supported by "
                    "this application. Please use an external software  "
                    "such as GnuPG (Linux, MacOS) or Kleopatra (Windows)."
                )
                open_window(msg_warn)
                continue
            msg.setDetailedText(self.key_to_text(key))
            if key is selected_keys[0]:
                click_show_details(msgbox=msg)
            status = open_window(msg)
            if status == QtWidgets.QMessageBox.Ok:
                try:
                    crypt.delete_pub_keys(
                        [key.fingerprint], self.app_data.config.gpg_store
                    )
                    self.pub_keys_view.selectionModel().clearSelection()
                except UserError as e:
                    msg_warn.setText(format(e))
                    open_window(msg_warn)
                self.text_panel.clear()
        self.update_public_keys()

    def upload_key(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Send public key")
        msg.setText("Do you want to upload the selected key to the key server?")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        show_ok = ok_message(
            "Send public key", "Key has been successfully uploaded to the keyserver."
        )
        show_warning = warning_callback("GPG key upload error")

        selected_keys = [
            index.model().get_value(index)
            for index in self.pub_keys_view.selectedIndexes()
        ]
        for key in selected_keys:
            msg.setDetailedText(self.key_to_text(key))
            if key is selected_keys[0]:
                click_show_details(msgbox=msg)
            status = open_window(msg)
            if status == QtWidgets.QMessageBox.Ok:
                worker = Worker(
                    upload_keys_workflow.upload_keys,
                    [key.fingerprint],
                    config=self.app_data.config,
                    report_config=self.app_data.config,
                    capture_loggers=(upload_keys_workflow.logger,),
                    forward_errors=show_warning,
                )
                worker.signals.result.connect(lambda _: show_ok())
                self.threadpool.start(worker)

    def send_signature_request(self):
        selected_keys = [
            index.model().get_value(index)
            for index in self.pub_keys_view.selectedIndexes()
        ]
        request_signature(selected_keys, self.app_data.config, self.threadpool, self)

    def _update_display(self, index: QtCore.QModelIndex):
        style = (
            "<style>"
            "th {text-align: left; padding: 0 20px 5px 0;}"
            ".danger { color: red;}"
            ".safe { color: green;}"
            "</style>"
        )
        if index.isValid():
            try:
                self.text_panel.setHtml(
                    style + self.key_to_html(index.model().get_value(index))
                )
            except IndexError:
                self.text_panel.setHtml("")


class KeyDownloadDialog(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threadpool = QtCore.QThreadPool.globalInstance()
        self.setWindowTitle("Download public keys from the server")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        self.search_string = LineEdit()
        self.btn_search = QtWidgets.QPushButton("Search")
        self.btn_search.clicked.connect(self.search_keys)

        self.key_list_view = QtWidgets.QListView()
        key_list_model = QtCore.QStringListModel()
        self.key_list_view.setModel(key_list_model)

        self.btn_download = QtWidgets.QPushButton("Download")
        self.btn_download.clicked.connect(self.download_selected)

        btn_cancel = QtWidgets.QPushButton("Close")
        btn_cancel.clicked.connect(self.close)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(
            QtWidgets.QLabel(
                "Enter a search term (e.g. user name, email, key " "fingerprint)"
            ),
            0,
            0,
        )
        layout.addWidget(self.search_string, 1, 0)
        layout.addWidget(self.btn_search, 1, 1)
        layout.addWidget(QtWidgets.QLabel("Select a key to download"), 2, 0)
        layout.addWidget(self.key_list_view, 3, 0)
        layout.addWidget(self.btn_download, 3, 1)
        layout.addWidget(btn_cancel, 4, 1)
        self.setLayout(layout)

    def search_keys(self):
        self.btn_search.setEnabled(False)
        self.key_list_view.model().setStringList([])
        show_warning = warning_callback("GPG key search error")
        worker = Worker(
            crypt.search_keyserver,
            self.search_string.text(),
            self.parent().app_data.config.keyserver_url,
            report_config=self.parent().app_data.config,
            forward_errors=show_warning,
        )
        worker.signals.result.connect(
            lambda keys: self.key_list_view.model().setStringList(
                [f"{k.uid} {k.fingerprint}" for k in keys]
            )
        )
        worker.signals.finished.connect(lambda: self.btn_search.setEnabled(True))
        self.threadpool.start(worker)

    def download_selected(self):
        key_ids = []
        for index in self.key_list_view.selectedIndexes():
            key_ids.append(index.model().data(index).split()[-1])
        if key_ids:
            self.btn_download.setEnabled(False)
            show_warning = warning_callback("GPG key search error")
            worker = Worker(
                crypt.download_keys,
                key_ids,
                self.parent().app_data.config.keyserver_url,
                self.parent().app_data.config.gpg_store,
                report_config=self.parent().app_data.config,
                forward_errors=show_warning,
            )
            worker.signals.result.connect(lambda x: self.parent().update_public_keys())
            worker.signals.finished.connect(lambda: self.btn_download.setEnabled(True))
            self.threadpool.start(worker)


class KeyGenDialog(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threadpool = QtCore.QThreadPool.globalInstance()
        self.setWindowTitle("Generate new key pair")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        self.text_name_full = LineEdit()
        self.text_name_extra = LineEdit()
        self.text_email = LineEdit()
        self.text_pass = LineEdit()
        self.text_pass_repeat = LineEdit()
        self.toggle_password_visibility(False)

        re_email = QtCore.QRegularExpression(r"[^@]+@[^@]+\.[^@]+")
        self.text_email.setValidator(QtGui.QRegularExpressionValidator(re_email))

        self.btn_run = QtWidgets.QPushButton("Generate key")
        self.btn_run.setDefault(True)
        self.btn_run.clicked.connect(self.create_private_key)
        btn_cancel = QtWidgets.QPushButton("Close")
        btn_cancel.clicked.connect(self.close)
        btn_show_pass = QtWidgets.QPushButton("Show")
        btn_show_pass.setCheckable(True)
        btn_show_pass.clicked.connect(self.toggle_password_visibility)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(QtWidgets.QLabel("Full name"), 0, 0)
        layout.addWidget(self.text_name_full, 0, 1)
        layout.addWidget(QtWidgets.QLabel("(optional) institution/project"), 1, 0)
        layout.addWidget(self.text_name_extra, 1, 1)
        layout.addWidget(QtWidgets.QLabel("Institutional email"), 2, 0)
        layout.addWidget(self.text_email, 2, 1)
        layout.addWidget(QtWidgets.QLabel("Password"), 3, 0)
        layout.addWidget(self.text_pass, 3, 1)
        layout.addWidget(QtWidgets.QLabel("Password (repeat)"), 4, 0)
        layout.addWidget(self.text_pass_repeat, 4, 1)
        layout.addWidget(btn_show_pass, 4, 2)
        layout.addWidget(btn_cancel, 5, 0)
        layout.addWidget(self.btn_run, 5, 1)
        layout.addWidget(
            QtWidgets.QLabel("Key generation can take a few minutes"), 6, 0, 1, 3
        )
        self.setLayout(layout)

    def toggle_password_visibility(self, show: bool):
        mode = QtWidgets.QLineEdit.Normal if show else QtWidgets.QLineEdit.Password
        self.text_pass.setEchoMode(mode)
        self.text_pass_repeat.setEchoMode(mode)

    def clear_form(self):
        self.text_name_full.clear()
        self.text_name_extra.clear()
        self.text_email.clear()
        self.text_pass.clear()
        self.text_pass_repeat.clear()

    def post_key_creation(self, key: gpg.Key):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("GPG Key Generation")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        try:
            revocation_cert = crypt.create_revocation_certificate(
                key.fingerprint,
                self.text_pass.text(),
                self.parent().app_data.config.gpg_store,
            )
            msg.setText(
                "Your new key has been successfully generated.\n\n"
                "Additionally, a revocation certificate was also created. "
                "It can be used to revoke your key in the eventuality that it "
                "gets compromised, lost, or that you forgot your password.\n"
                "Please store the revocation certificate below in a safe "
                "location, as anyone can use it to revoke your key."
            )
            msg.setDetailedText(revocation_cert.decode())
            # Programatically click the "Show Details..." button so that the
            # certificate is shown by default.
            click_show_details(msgbox=msg)

        except UserError:
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(
                "Key has been successfully generated. "
                "However, it was not possible to create a revocation "
                "certificate. "
                "Execute the following command to create the certificate\n\n"
                f"gpg --gen-revoke {key.fingerprint}"
            )
        finally:
            open_window(msg)
            if (
                self.parent().app_data.config.key_authority_fingerprint
                and not self.parent().app_data.config.offline
            ):
                request_signature(
                    (key,), self.parent().app_data.config, self.threadpool, self
                )
            self.clear_form()
            self.parent().update_private_keys()
            self.parent().update_public_keys()
            self.close()

    def create_private_key(self):
        show_warning = warning_callback("GPG Key Generation Error")
        self.btn_run.setEnabled(False)
        full_name = f"{self.text_name_full.text()} " f"{self.text_name_extra.text()}"
        worker = Worker(
            crypt.create_key,
            full_name,
            self.text_email.text(),
            self.text_pass.text(),
            self.text_pass_repeat.text(),
            self.parent().app_data.config.gpg_store,
            forward_errors=show_warning,
            report_config=self.parent().app_data.config,
        )
        worker.signals.result.connect(self.post_key_creation)
        worker.signals.finished.connect(lambda: self.btn_run.setEnabled(True))
        self.threadpool.start(worker)


def click_show_details(msgbox: QtWidgets.QMessageBox):
    for button in msgbox.buttons():
        if msgbox.buttonRole(button) is QtWidgets.QMessageBox.ButtonRole.ActionRole:
            button.click()


def request_signature(
    keys: Sequence[gpg.Key],
    config: Config,
    threadpool: QtCore.QThreadPool,
    parent: Optional[QtWidgets.QWidget] = None,
):
    msg = QtWidgets.QMessageBox(parent)
    msg.setWindowTitle("Key signing request")
    msg.setText("Do you want to request signature for this key?")
    msg.setIcon(QtWidgets.QMessageBox.Question)
    msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    show_ok = ok_message(
        "Key signing request", "Key signing request has been sent.", parent=parent
    )
    show_warning = warning_callback("Key signing request", parent=parent)

    for key in keys:
        msg.setDetailedText(KeysTab.key_to_text(key))
        if key is keys[0]:
            click_show_details(msgbox=msg)
        status = open_window(msg)
        if status == QtWidgets.QMessageBox.Yes:
            worker = Worker(
                request_sigs_workflow.request_sigs,
                key_ids=[key.key_id],
                config=config,
                capture_loggers=(request_sigs_workflow.logger,),
                forward_errors=show_warning,
                report_config=config,
            )
            worker.signals.result.connect(lambda _: show_ok())
            threadpool.start(worker)


def ok_message(title: str, msg: str, parent=None) -> Callable:
    msg_ok = QtWidgets.QMessageBox(parent)
    msg_ok.setIcon(QtWidgets.QMessageBox.Information)
    msg_ok.setWindowTitle(title)
    msg_ok.setText(msg)
    return lambda: open_window(msg_ok)
