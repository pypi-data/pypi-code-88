import copy
from typing import Optional, Dict

from .component import PathInput, FieldMapping, create_slider, LineEdit, SpinBox
from .pyside import QtCore, QtGui, QtWidgets
from .keys_refresh import load_authority_key_threaded
from ..utils import config
from ..utils.config import Config
from ..utils.validation import REGEX_URL, PACKAGE_SUFFIX


LABEL_COMPRESSION_LEVEL = "Compression level"
STATUS_TIP_COMPRESSION_LEVEL = (
    "Compression level used in data encryption, from 0 (no compression) to "
    "9 (highest). Higher compression levels require more computing time."
)


def config_to_settings(cfg: Config) -> Dict:
    config_dict = config.config_to_dict(cfg)
    del config_dict["connections"]  # connections are handled in "Transfer"
    return config_dict


class SettingsTab(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_widget = self.parent()
        self.config = self.parent_widget.app_data.config

        self.field_mapping = FieldMapping()
        self.layout: QtWidgets.QGridLayout = QtWidgets.QGridLayout()

        self.persist_btn_text = "Save to config file"
        self._add_header()
        self._add_settings()
        self._add_footer()
        self._populate_tab_with_config_values()

        self.setLayout(self.layout)

    def _populate_tab_with_config_values(self):
        """Populate the fields of the tab with the app's config values"""
        settings_dict = config_to_settings(self.config)
        self.field_mapping.load(settings_dict)

    def _update_config(self, cfg: Config):
        """Replaces the `config` with `cfg` and updates the contents of the
        widgets in the UI.
        """
        self.config = cfg
        self._populate_tab_with_config_values()

    def _save_config_to_disk(self):
        """Write the current in-app config values to a config file on disk"""
        config.save_config(config.config_to_dict(self.config))
        self.parent_widget.config_on_disk = copy.deepcopy(self.config)

    def _add_header(self):
        top_label = QtWidgets.QLabel(
            "Changes you make are applied instantly during the current session.\n"
            f"To persist changes across restarts, make sure to click the "
            f"'{self.persist_btn_text}' button at the bottom of the app."
        )
        top_label.setWordWrap(True)
        self.layout.addWidget(
            top_label,
            0,
            0,
            1,
            2,
        )

        reset_btn = QtWidgets.QPushButton("Reset", self)
        reset_btn.setStatusTip("Resets to your last persisted settings")
        reset_btn.clicked.connect(lambda: self._update_config(config.load_config()))
        self.layout.addWidget(reset_btn, 0, 2)

        defaults_btn = QtWidgets.QPushButton("Restore defaults", self)
        defaults_btn.setStatusTip("Reset all settings to their default values")
        defaults_btn.clicked.connect(
            lambda: self._update_config(config.default_config())
        )
        self.layout.addWidget(defaults_btn, 0, 3)

    def _add_settings(self):
        encrypt_decrypt_group = self._add_group("Data encryption / decryption settings")

        self._add_widget_int_range(
            encrypt_decrypt_group,
            LABEL_COMPRESSION_LEVEL,
            "compression_level",
            STATUS_TIP_COMPRESSION_LEVEL,
            0,
            9,
        )

        self._add_widget_str(
            encrypt_decrypt_group,
            "Default sender",
            "default_sender",
            "Default sender fingerprint for encryption",
        )

        self._add_widget_bool(
            encrypt_decrypt_group,
            "Sign encrypted data",
            "sign_encrypted_data",
            "Whether encrypted data should be signed with sender's key",
        )

        self._add_widget_bool(
            encrypt_decrypt_group,
            "Always trust recipient key",
            "always_trust_recipient_key",
            "If unchecked, the encryption key must be signed by the local user",
        )

        self._add_widget_path(
            encrypt_decrypt_group,
            "Output directory",
            "output_dir",
            "Default output directory, relevant for encryption/decryption",
            True,
        )

        self._add_widget_bool(
            encrypt_decrypt_group,
            "Offline mode",
            "offline",
            "In offline mode, sett will not make any network connections: "
            "DTR verification and automatic PGP key downloading/updating is disabled.",
        )

        self._add_widget_str(
            encrypt_decrypt_group,
            "Default package suffix",
            "package_name_suffix",
            "Default suffix for encrypted package name",
            regex=PACKAGE_SUFFIX,
        )

        pgp_keys_group = self._add_group("PGP keys")

        self._add_widget_str(
            pgp_keys_group,
            "Key validation authority fingerprint",
            "key_authority_fingerprint",
            "Fingerprint (40 characters) of the key validation authority's "
            "PGP key. If a value is specified, only keys signed the "
            "authority's key can be used.",
        )

        self._add_widget_path(
            pgp_keys_group,
            "GPG home directory",
            "gpg_home_dir",
            "Path of the directory where GnuPG stores its keyrings and "
            "configuration files.",
            True,
        )

        # no validation, as specifying http:// is optional
        self._add_widget_str(
            pgp_keys_group,
            "Keyserver URL",
            "keyserver_url",
            "URL of the keyserver: used for publishing/fetching public PGP keys.",
        )

        data_transfer_group = self._add_group("Data transfer")

        self._add_widget_str(
            data_transfer_group,
            "SSH password encoding",
            "ssh_password_encoding",
            "Character encoding used for the SSH key password",
        )

        self._add_widget_str(
            data_transfer_group,
            "DCC portal URL",
            "dcc_portal_url",
            "URL of portal instance. The portal is used for key signing and "
            "DTR (Data Transfer Request) validation.",
            REGEX_URL,
        )

        sett_updates_group = self._add_group("sett updates")

        self._add_widget_str(
            sett_updates_group,
            "Repo URL",
            "repo_url",
            "Python package repository, used when looking for updates",
            REGEX_URL,
        )

        self._add_widget_bool(
            sett_updates_group,
            "Check version",
            "check_version",
            "Check whether you have the latest version of sett on startup",
        )

        misc_log_group = self._add_group("Miscellaneous and logs")

        self._add_widget_bool(
            misc_log_group,
            "Quit confirmation",
            "gui_quit_confirmation",
            "Ask for confirmation before closing the application",
        )

        self._add_widget_path(
            misc_log_group,
            "Temp directory",
            "temp_dir",
            "Path to sett working directory",
            True,
        )

        self._add_widget_path(
            misc_log_group,
            "Log directory",
            "log_dir",
            "Path to log files directory",
            True,
        )

        self._add_widget_int(
            misc_log_group,
            "Log max. file number",
            "log_max_file_number",
            "Maximum number of logfiles to keep as backup",
            1,
        )

        self._add_widget_bool(
            misc_log_group,
            "Create error reports",
            "error_reports",
            "Write an error report if some error happens",
        )

    def _add_footer(self):
        persist_btn = QtWidgets.QPushButton(self.persist_btn_text, self)
        persist_btn.setIcon(QtGui.QIcon(":icon/feather/save.png"))
        persist_btn.setStatusTip("Saves your current settings to the config file")
        persist_btn.clicked.connect(
            # lambda: config.save_config(config.config_to_dict(self.config))
            self._save_config_to_disk
        )
        self.layout.addWidget(persist_btn, self.layout.rowCount() + 1, 0, 1, 4)

    def _set_config(self, key: str, value):
        """Updates the specified sett config attribute (key) with a new value"""
        if value != getattr(self.config, key):
            setattr(self.config, key, value)
            if key == "key_authority_fingerprint":
                # Only attempt to reload the key validation authority key if
                # a proper fingerprint was entered. Otherwise we get a warning
                # each time the user is entering a new character in the field.
                if len(value) == 40:
                    load_authority_key_threaded(self.parent_widget.app_data)
                else:
                    self.parent_widget.app_data.validation_authority_key = None

    def _get_config(self, key: str):
        return getattr(self.config, key)

    def _add_group(self, name: str) -> QtWidgets.QGridLayout:
        group_box = QtWidgets.QGroupBox(name)
        self.layout.addWidget(group_box, self.layout.rowCount() + 1, 0, 1, 4)
        layout = QtWidgets.QGridLayout(group_box)
        layout.setColumnMinimumWidth(0, 180)
        group_box.setLayout(layout)
        return layout

    def _add_widget_str(
        self,
        layout: QtWidgets.QGridLayout,
        label: str,
        config_key: str,
        status_tip: str,
        regex: Optional[str] = None,
    ):
        widget = self.field_mapping.bind_text(config_key, LineEdit())
        widget.setStatusTip(status_tip)
        if regex:
            widget.setValidator(
                QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(regex))
            )

        widget.textChanged.connect(lambda text: self._set_config(config_key, text))

        row = layout.rowCount() + 1
        layout.addWidget(QtWidgets.QLabel(label), row, 0)
        layout.addWidget(
            widget,
            row,
            1,
        )

    def _add_widget_path(
        self,
        layout: QtWidgets.QGridLayout,
        label: str,
        config_key: str,
        status_tip: str,
        directory: bool,
    ):
        widget = self.field_mapping.bind_path(
            config_key, PathInput(directory=directory, path=None)
        )
        widget.status_tip = status_tip

        widget.on_path_change(
            lambda path: self._set_config(config_key, "" if path is None else str(path))
        )

        row = layout.rowCount() + 1
        layout.addWidget(QtWidgets.QLabel(label), row, 0)
        layout.addWidget(widget.text, row, 1)
        layout.addWidget(widget.btn, row, 2)
        layout.addWidget(widget.btn_clear, row, 3)

    def _add_widget_bool(
        self,
        layout: QtWidgets.QGridLayout,
        label: str,
        config_key: str,
        status_tip: str,
    ):
        widget = self.field_mapping.bind_checked(config_key, QtWidgets.QCheckBox())
        widget.setStatusTip(status_tip)

        widget.stateChanged.connect(
            lambda state: self._set_config(config_key, state == QtCore.Qt.Checked)
        )

        row = layout.rowCount() + 1
        layout.addWidget(QtWidgets.QLabel(label), row, 0)
        layout.addWidget(
            widget,
            row,
            1,
        )

    def _add_widget_int(
        self,
        layout: QtWidgets.QGridLayout,
        label: str,
        config_key: str,
        status_tip: str,
        minimum: Optional[int] = None,
        maximum: Optional[int] = None,
    ):
        widget = self.field_mapping.bind_value(config_key, SpinBox())
        widget.setStatusTip(status_tip)
        if minimum is not None:
            widget.setMinimum(minimum)
        if maximum is not None:
            widget.setMaximum(maximum)

        widget.valueChanged.connect(lambda value: self._set_config(config_key, value))

        row = layout.rowCount() + 1
        layout.addWidget(QtWidgets.QLabel(label), row, 0)
        layout.addWidget(
            widget,
            row,
            1,
        )

    def _add_widget_int_range(
        self,
        layout: QtWidgets.QGridLayout,
        label: str,
        config_key: str,
        status_tip: str,
        minimum: int,
        maximum: int,
    ):
        def on_change(value: int):
            self._set_config(config_key, value)

        slider, slider_value = create_slider(
            minimum=minimum,
            maximum=maximum,
            initial_value=self._get_config(config_key),
            status_tip=status_tip,
            on_change=on_change,
            show_ticks=True,
        )
        self.field_mapping.bind_value(config_key, slider)
        row = layout.rowCount() + 1
        layout.addWidget(QtWidgets.QLabel(label), row, 0)
        layout.addWidget(slider, row, 1)
        layout.addWidget(slider_value, row, 2)
