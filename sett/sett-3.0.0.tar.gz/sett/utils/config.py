import os
import platform
import json
import tempfile
import dataclasses
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple, Dict, Any, Optional

import gpg_lite as gpg
from libbiomedit.lib.deserialize import deserialize

from .log import get_default_log_dir, create_logger
from ..core.error import UserError
from ..core.portal_api import PortalApi
from .. import APP_NAME_SHORT


CONFIG_FILE_NAME = "config.json"
CONFIG_FILE_ENVIRON_VAR = "SETT_CONFIG_FILE"

conf_sub_dir_by_os: Dict[str, Tuple[str, ...]] = {
    "Linux": (".config",),
    "Darwin": (".config",),
    "Windows": ("AppData", "Roaming"),
}

logger = create_logger(__name__)


@dataclass(frozen=True)
class Connection:
    """dataclass holding config of a connection (sftp / liquid files)"""

    protocol: str
    parameters: Dict[str, Any]


TMP_DIR = tempfile.gettempdir()


@dataclass
class Config:
    """dataclass holding config data"""

    dcc_portal_url: str = "https://portal.dcc.sib.swiss"
    keyserver_url: Optional[str] = "keyserver.dcc.sib.swiss"
    gpg_home_dir: str = gpg.get_default_gnupg_home_dir()
    key_authority_fingerprint: Optional[
        str
    ] = "B37CE2A101EBFA70941DF885881685B5EE0FCBD3"
    sign_encrypted_data: bool = True
    always_trust_recipient_key: bool = True
    repo_url: str = "https://pypi.org"
    check_version: bool = True
    offline: bool = False
    log_dir: str = get_default_log_dir()
    error_reports: bool = True
    log_max_file_number: int = 1000
    connections: Dict[str, Connection] = dataclasses.field(default_factory=lambda: {})
    temp_dir: str = TMP_DIR
    output_dir: Optional[str] = None
    ssh_password_encoding: str = "utf_8"
    default_sender: Optional[str] = None
    gui_quit_confirmation: bool = True
    compression_level: int = 5
    package_name_suffix: Optional[str] = None

    def __post_init__(self):
        for url in ("dcc_portal_url", "repo_url"):
            setattr(self, url, getattr(self, url).rstrip("/"))

    @property
    def portal_api(self):
        return PortalApi(self.dcc_portal_url)

    @property
    def gpg_store(self):
        return open_gpg_dir(self.gpg_home_dir)


class ConnectionStore:
    """Connection configuration storage manager"""

    config_field_name = "connections"

    def __init__(self, config_path: Optional[str] = None):
        self.path = get_config_file() if config_path is None else config_path

    def _read(self) -> Dict:
        """Load data from config file"""
        try:
            with open(self.path) as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _write(self, data: Dict):
        """Write data to config file"""
        save_config(data, self.path)

    def save(self, name: str, connection: Connection, exclude: str = "pass"):
        """Save a new connection in the config file

        :param name: name of the new connection.
        :param connection: new connection object.
        :param exclude: exclude all connection fields containing `exclude` substring.
        """
        data = self._read()
        connections = data.setdefault(self.config_field_name, {})
        c = dataclasses.asdict(connection)
        pass_fields = {k for k in c["parameters"] if exclude in k}
        for f in pass_fields:
            del c["parameters"][f]
        connections[name] = c
        self._write(data)

    def delete(self, name: str):
        """Delete a new connection from the config file"""
        data = self._read()
        try:
            data.get(self.config_field_name, {}).pop(name)
            self._write(data)
        except KeyError as e:
            raise UserError(f"Connection '{name}' does not exist.") from e

    def rename(self, old: str, new: str):
        """Rename an existing connection from the config file"""
        data = self._read()
        try:
            connection = data.get(self.config_field_name, {}).pop(old)
            data[self.config_field_name][new] = connection
            self._write(data)
        except KeyError as e:
            raise UserError(f"Connection '{new}' does not exist.") from e


def load_config() -> Config:
    """Loads the config, returning a Config object."""

    # TODO: remove migration (see issue 283)
    migrate_from_keyid_to_fingerprint()

    cfg_dct = {}
    try:
        cfg_dct = sys_config_dict()
        cfg_dct.update(load_config_dict(get_config_file()))
    except UserError as e:
        warnings.warn(format(e))

    return deserialize(Config)(cfg_dct)


def save_config(config: Dict, path: Optional[str] = None) -> str:
    """Save config to a file.
    :return: path of the created config file.
    """
    config_file = Path(get_config_file() if path is None else path)
    if not config_file.parent.is_dir():
        config_file.parent.mkdir(parents=True)

    with open(config_file, "w") as f:
        json.dump(config, f, indent=2, sort_keys=True)
    return config_file.as_posix()


def create_config() -> str:
    """Creates a new config file in the home directory's config folder
    :return: path of the created config file.
    """
    return save_config(config_to_dict(default_config()))


def config_to_dict(config: Config) -> dict:
    """Converts a Config object into a dict."""
    return dataclasses.asdict(config)


def default_config() -> Config:
    """Creates a new Config object with default values."""
    return deserialize(Config)(sys_config_dict())


def sys_config_dict() -> dict:
    """On linux only: try to load global sys config. If the env variable
    SYSCONFIG is set search there, else in /etc/{APP_NAME_SHORT}.
    """
    if platform.system() == "Linux":
        sys_cfg_dir = os.environ.get("SYSCONFIG", os.path.join("/etc", APP_NAME_SHORT))
        return load_config_dict(os.path.join(sys_cfg_dir, CONFIG_FILE_NAME))
    return {}


def load_config_dict(path: str) -> dict:
    """Load raw config as a dict."""
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.decoder.JSONDecodeError as e:
        raise UserError(f"Failed to load configuration from '{path}'. {e}") from e


def get_config_file() -> str:
    """Retrieve the platform-specific path of the config file. If the user has
    the correct config file path environmental variable defined in their
    current environment, this file gets used instead.

    :return: path of the config.
    :raises UserError:
    """
    # Case 1: a config file path environmental variable is defined.
    if CONFIG_FILE_ENVIRON_VAR in os.environ:
        config_file = os.environ[CONFIG_FILE_ENVIRON_VAR]
        if os.path.isdir(config_file):
            raise UserError(
                f"Environmental variable {CONFIG_FILE_ENVIRON_VAR} "
                f"must point to a file, not a directory "
                f"[{config_file}]."
            )
        return config_file

    # Case 2: use the default platform-specific config file.
    return os.path.join(get_config_dir(), CONFIG_FILE_NAME)


def get_config_dir() -> str:
    """Return platform specific default config direcory."""
    return os.path.join(
        os.path.expanduser("~"), *conf_sub_dir_by_os[platform.system()], APP_NAME_SHORT
    )


def open_gpg_dir(gpg_dir: str) -> gpg.GPGStore:
    """Open the database inside a GnuPG directory and return it as a gpg
    object.

    :param gpg_dir: path of the GnuPG directory to open.
    :return: a gpg-lite GPGStore
    :raises UserError:
    """
    if not Path(gpg_dir).is_dir():
        os.makedirs(gpg_dir, mode=0o700)

    try:
        return gpg.GPGStore(gnupg_home_dir=gpg_dir)
    except ValueError:
        raise UserError(f"unable to open GnuPG directory [{gpg_dir}].") from None


def migrate_from_keyid_to_fingerprint():
    """Temporary migration to auto-update user's config files after changes
    from https://gitlab.com/biomedit/sett/-/merge_requests/56
    """
    config_file = get_config_file()
    config_needs_update = False

    try:
        config_dict = load_config_dict(config_file)
    except UserError:
        return

    if "gpg_config_dir" in config_dict:
        config_dict["gpg_home_dir"] = config_dict.pop("gpg_config_dir")
        config_needs_update = True

    if "key_validation_authority_keyid" in config_dict:
        fingerprint = Config().key_authority_fingerprint
        key_id = config_dict.pop("key_validation_authority_keyid")
        if key_id == fingerprint[-16:]:
            config_dict["key_authority_fingerprint"] = fingerprint
        else:
            config_dict["key_authority_fingerprint"] = key_id
            warnings.warn(
                f"This new version of {APP_NAME_SHORT} requires the full "
                "fingerprint of the key validation authority. Please update "
                "the 'key_authority_fingerprint' field in your config file: "
                f"{config_file}"
            )

        config_needs_update = True

    if config_needs_update:
        save_config(config_dict, path=config_file)
