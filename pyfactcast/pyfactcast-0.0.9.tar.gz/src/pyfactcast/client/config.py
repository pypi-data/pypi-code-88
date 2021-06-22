from dataclasses import dataclass
from typing import Dict, Optional, Union, cast
from pathlib import Path

import logging
import json
from os import environ as env


log_level = getattr(
    logging, env.get("FACTCAST_LOG_LEVEL", "WARNING").upper(), 30
)  # Setting a default here is pretty defensive. Anyhow nothing lost by doing it

log = logging.getLogger()
log.setLevel(log_level)

# Set grpc dns resolution to native. C-Ares is
env["GRPC_DNS_RESOLVER"] = "native"


@dataclass
class Credentials:
    username: str
    password: str

    def __post_init__(self) -> None:
        if self.username and not self.password:
            raise ValueError(
                "Username was provided without password. Please provide a non empty password."
            )
        if self.password and not self.username:
            raise ValueError(
                "Password was provided without a username. Please provide a non empty username."
            )
        if not self.username and not self.password:
            raise ValueError(
                "Both username and password are empty. Do not instantiate Credentials like this."
            )


@dataclass
class ClientConfiguration:
    server: Optional[str]
    root_cert_path: Optional[str] = None
    ssl_target_override: Optional[str] = None
    credentials: Optional[Credentials] = None
    insecure: bool = False
    default: bool = False

    def __post_init__(self) -> None:
        if not self.server:
            raise ValueError("Server connection string missing.")


def get_client_configuration(profile: str = "default") -> ClientConfiguration:
    log.info("Getting client configuration")

    file_based_config = _get_client_config_from_file()
    profile_from_file: Optional[Dict[str, Union[str, bool]]] = {}
    if file_based_config:
        profiles = file_based_config["profiles"]
        profile_from_file = profiles.get(profile)

        if profile != "default" and not profile_from_file:
            raise ValueError(f"The specified profile ({profile}) does not exist.")

    env_config = _get_client_config_from_env()

    combined_config = {**profile_from_file, **env_config}  # type: ignore # Upgrade 3.9 | notation

    username = cast(str, combined_config.get("grpc_user", ""))
    password = cast(str, combined_config.get("grpc_password", ""))
    credentials = None

    if username or password:
        log.debug("Setting up credentials")
        credentials = Credentials(username, password)

    return ClientConfiguration(
        server=str(combined_config.get("grpc_server", "")),
        credentials=credentials,
        root_cert_path=combined_config.get("grpc_root_cert_path"),  # type: ignore
        ssl_target_override=combined_config.get("grpc_cn_overwrite"),  # type: ignore
        insecure=bool(combined_config.get("grpc_insecure", False)),
    )


def _get_client_config_from_file(
    config_file_path: Optional[Path] = None,
) -> Optional[Dict[str, Dict[str, Dict[str, Union[str, bool]]]]]:

    if not config_file_path:
        config_file_path = Path.home().joinpath(".pyfactcast").absolute()

    if not config_file_path.exists():
        log.info("No configuration file found.")
        return None

    with open(config_file_path, "r") as f:
        config: Dict[str, Dict[str, Dict[str, Union[str, bool]]]] = json.load(f)

    return config


def _get_client_config_from_env() -> Dict[str, Optional[str]]:
    log.info("Getting client configuration from environment")
    result = {}

    # Upgrade 3.8 Walrus
    if env.get("GRPC_SERVER"):
        result["grpc_server"] = env.get("GRPC_SERVER")
    if env.get("GRPC_USER"):
        result["grpc_user"] = env.get("GRPC_USER")
    if env.get("GRPC_PASSWORD"):
        result["grpc_password"] = env.get("GRPC_PASSWORD")
    if env.get("GRPC_ROOT_CERT_PATH"):
        result["grpc_root_cert_path"] = env.get("GRPC_ROOT_CERT_PATH")
    if env.get("GRPC_CN_OVERWRITE"):
        result["grpc_cn_overwrite"] = env.get("GRPC_CN_OVERWRITE")
    if env.get("GRPC_INSECURE"):
        result["grpc_insecure"] = env.get("GRPC_INSECURE")

    return result
