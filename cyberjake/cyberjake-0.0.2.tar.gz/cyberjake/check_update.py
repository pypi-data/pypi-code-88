"""Script to check for available updates."""
import json
from distutils.version import LooseVersion
import requests


def check_update(project_name: str, current_version: str) -> bool:
    """
    Check version against pypi.org information

    **Requires Requests**

    :param project_name: Name of project to check
    :param current_version: Current version of project. Usually from __version__
    :return: Latest version is newer. Returns false if project can't be found
    :rtype: bool
    """
    try:
        latest = LooseVersion(
            requests.get(f"https://pypi.org/pypi/{project_name}/json").json()["info"]["version"]
        )
    except json.decoder.JSONDecodeError:
        return False
    return latest > current_version
