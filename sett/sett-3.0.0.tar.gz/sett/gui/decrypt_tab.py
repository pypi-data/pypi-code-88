from functools import partial

from .component import TabMixin, PathInput, GuiProgress, run_dialog
from .file_selection_widget import ArchiveOnlyFileSelectionWidget
from .parallel import Worker
from .pyside import QtCore, QtWidgets
from ..workflows import decrypt


class DecryptTab(QtWidgets.QWidget, TabMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threadpool = QtCore.QThreadPool.globalInstance()
        self.app_data = self.parent().app_data

        files_panel = self.create_files_panel()
        decrypt_options_panel = self.create_decrypt_options_panel()
        self.create_run_panel("Decrypt data", self.decrypt, "Decrypt selected files")
        self.app_data.add_listener("decrypt_files", self._enable_buttons)
        self.create_console()
        self.create_progress_bar()

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(files_panel)
        layout.addWidget(decrypt_options_panel)
        layout.addWidget(self.run_panel)
        layout.addWidget(self.console)
        layout.addWidget(self.progress_bar)

    def _enable_buttons(self):
        self.set_buttons_enabled(len(self.app_data.decrypt_files) > 0)

    def create_files_panel(self):
        box = ArchiveOnlyFileSelectionWidget(
            "Files to decrypt (hint: you can drag & drop files)", self
        )
        box.file_list_model.layoutChanged.connect(
            lambda: setattr(self.app_data, "decrypt_files", box.get_list())
        )
        return box

    def create_decrypt_options_panel(self):
        box = QtWidgets.QGroupBox("Output")

        decompress = QtWidgets.QCheckBox("Decompress", box)
        decompress.setStatusTip("Decompress data after decryption")
        decompress.setChecked(not self.app_data.decrypt_decrypt_only)
        decompress.stateChanged.connect(
            lambda state: setattr(
                self.app_data, "decrypt_decrypt_only", state == QtCore.Qt.Unchecked
            )
        )

        output_location = PathInput(path=self.app_data.encrypt_output_location)
        output_location.status_tip = "Destination folder for the decrypted packages"
        output_location.on_path_change(
            partial(setattr, self.app_data, "decrypt_output_location")
        )

        layout_output = QtWidgets.QHBoxLayout()
        layout_output.addWidget(QtWidgets.QLabel("Location"))
        layout_output.addWidget(output_location.text)
        layout_output.addWidget(output_location.btn)
        layout = QtWidgets.QVBoxLayout(box)
        layout.addWidget(decompress)
        layout.addLayout(layout_output)
        return box

    def decrypt(self, dry_run=False):
        progress = GuiProgress()
        progress.updated.connect(self.progress_bar.setValue)
        if not dry_run:
            pw = run_dialog(self, "Enter password for your GPG key")
            if pw is None:
                return
        else:
            pw = None
        worker = Worker(
            decrypt.decrypt,
            files=self.app_data.decrypt_files,
            capture_loggers=(decrypt.logger,),
            output_dir=str(self.app_data.decrypt_output_location),
            config=self.app_data.config,
            decrypt_only=self.app_data.decrypt_decrypt_only,
            passphrase=pw,
            dry_run=dry_run,
            progress=progress,
            ignore_exceptions=True,
            report_config=self.app_data.config,
        )
        self.add_worker_actions(worker)
        self.threadpool.start(worker)
