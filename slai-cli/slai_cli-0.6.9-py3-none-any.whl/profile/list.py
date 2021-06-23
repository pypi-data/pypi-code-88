import yaml

from columnar import columnar
from pathlib import Path


from slai_cli import log


def list_profiles():
    headers = ["name", "client_id", "client_secret"]

    credentials_path = f"{Path.home()}/.slai"
    try:
        with open(f"{credentials_path}/credentials.yml", "r") as f_in:
            try:
                credentials = yaml.safe_load(f_in)
            except yaml.YAMLError:
                pass
    except:
        credentials = {}

    data = [
        [
            profile_name,
            credentials[profile_name]["client_id"],
            credentials[profile_name]["client_secret"],
        ]
        for profile_name in credentials.keys()
    ]
    try:
        table = columnar(data, headers, no_borders=True)
        log.info(table)
    except IndexError:
        log.warn("No profiles found.")
        return
