from __future__ import annotations

import json
from hashlib import md5
from pathlib import Path
from typing import Any, Dict

from .mission import Mission


def _checksum(obj: object) -> str:
    return md5(str(obj).encode("utf-8")).hexdigest()


def _mission_file_path(mission_name: str) -> Path:
    file_path = Path(mission_name)

    if file_path.suffix != ".json":
        return file_path.with_suffix(".json")

    return file_path


def _decode_mission(json: Dict[str, Any]) -> Dict[str, Any]:
    for key in json:
        if isinstance(json[key], dict):
            json[key] = _decode_mission(json[key])
        elif isinstance(json[key], list):
            json[key] = tuple(json[key])

    return json


class StorageError(Exception):
    pass


class ValidationError(Exception):
    pass


def store_mission(mission: Mission, mission_name: str) -> None:
    """Store a mission in a file.

    Generates a checksum of the mission to ensure mission is not modified when reloaded. If the provided filename does
    not end in a json extension, one will be added.

    Args:
        mission: Mission to store
        file_name: Name of the file to store the mission to
    """

    data = mission.dict()
    checksum = _checksum(data)
    file_path = _mission_file_path(mission_name)

    with file_path.open("w") as mission_file:
        json.dump({"mission": data, "checksum": checksum}, mission_file)


def load_mission(mission_name: str) -> Mission:
    """Load a mission from a file

    If the provided file name does not include a json extension, it will be added. An exception will be raised if the
    json object in the file does not include the proper keys, or the mission data does not match the checksum.

    Args:
        file_name: The name of the file to load mission from

    Returns:
        mission: The validated mission
    """

    file_path = _mission_file_path(mission_name)

    if not file_path.exists():
        return Mission()
    elif not file_path.is_file():
        raise StorageError(f"{file_path.name} is not a file")

    with file_path.open("r") as mission_file:
        data = json.load(mission_file, object_hook=_decode_mission)

    required_keys = ["mission", "checksum"]
    has_required_keys = all(key in data for key in required_keys)

    if not has_required_keys:
        missing = [key for key in required_keys if key not in data]
        raise StorageError(f"Malformed mission file. Missing required key(s): {missing}")

    is_valid = _checksum(data["mission"]) == data["checksum"]

    if not is_valid:
        raise ValidationError("Mission data does not match checksum")

    return Mission.parse_obj(data["mission"])
