# Copyright (c) 2014-2021 GeoSpock Ltd.

import json
from pathlib import Path

import keyring
from tenacity import retry, wait_fixed, stop_after_attempt

from .constants import messages
from .exceptions import CLIError
from keyring.errors import NoKeyringError

GEOSPOCK_DIR = Path.home().joinpath(".geospock")
CONFIG_FILE = GEOSPOCK_DIR.joinpath("config.json")


class ConfigReaderAndWriter:
    def __init__(self, profile: str):
        self.profile = profile

    def write_login(self, username: str,
                    password: str,
                    request_address: str,
                    ca_cert_file,
                    disable_verification: bool):
        if username is None or password is None or request_address is None:
            raise CLIError(messages.helpLogin)
        Path(GEOSPOCK_DIR).mkdir(parents=True, exist_ok=True)
        current_config = self.get_config()
        try:
            current_config[self.profile] = dict(request_address=request_address,
                                                ca_cert_file=ca_cert_file,
                                                disable_verification=disable_verification)
        except Exception:
            raise CLIError("Could not generate configuration entry from provided request address.")
        config_path = Path(CONFIG_FILE)
        with config_path.open(mode="w") as config_file_write:
            config_file_write.write(json.dumps(current_config, indent=4))
        try:
            keyring.set_password("geospock", self.profile + "-username", username)
            keyring.set_password("geospock", self.profile + "-password", password)
        except NoKeyringError:
            raise CLIError("No keyring found. Install a keyring and try again.")

    def write_logout(self):
        config = self.get_config()
        if self.profile != "default" and self.profile not in config:
            raise CLIError(f"The profile '{self.profile}' does not exist.")
        config.pop(self.profile, None)
        config_path = Path(CONFIG_FILE)
        with config_path.open(mode="w") as config_file_write:
            config_file_write.write(json.dumps(config, indent=4))
        try:
            keyring.delete_password("geospock", self.profile + "-username")
            keyring.delete_password("geospock", self.profile + "-password")
        except keyring.errors.PasswordDeleteError:
            pass

    @retry(reraise=True, stop=stop_after_attempt(3), wait=wait_fixed(2))
    def get_from_keyring(self):
        try:
            user = keyring.get_password("geospock", self.profile + "-username")
            password = keyring.get_password("geospock", self.profile + "-password")
            return user, password
        except NoKeyringError:
            raise CLIError("No keyring found. Install a keyring and try again.")

    def decode(self):
        try:
            user, password = self.get_from_keyring()
        except keyring.errors.KeyringError:
            raise CLIError("Cannot retrieve login details from Keyring")
        if user is None or password is None:
            raise CLIError(messages.insufficientLoginDetails)
        return user, password

    def get_config(self) -> dict:
        config_path = Path(CONFIG_FILE)
        if config_path.exists() and config_path.stat().st_size > 0:
            with config_path.open() as json_file:
                try:
                    config_all = json.load(json_file)
                except json.JSONDecodeError:
                    raise CLIError(messages.invalidConfig)
            return config_all
        else:
            return {}
