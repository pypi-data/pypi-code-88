import inspect
import json
import os
from pathlib import Path
from typing import Dict

from ruamel.yaml import YAML

from cognite.air.constants import AIR_DATA_MODEL_NAME, AIR_DATA_PATH_TO_YAML, SA_EXT_ID
from cognite.air.utils import strip_patch_from_version


def get_local_testing(data):
    if SA_EXT_ID in data.keys():
        return False
    yaml_path = path_to_yaml(data)
    definitions = [i["id"] for i in json.loads(retrieve_field_definitions(yaml_path))]
    for i in definitions:
        if i not in data.keys():
            return False
    return True


def path_to_yaml(data: Dict) -> Path:
    if data.get(AIR_DATA_PATH_TO_YAML, False):
        path_to_yaml = Path(data[AIR_DATA_PATH_TO_YAML])
    else:
        path_to_yaml = _local_config_path()
    return path_to_yaml


def _load_yaml(path: Path) -> Dict:
    yaml = YAML(typ="safe").load(path)
    assert isinstance(yaml, dict)
    return yaml


def _local_config_path() -> Path:
    stack = inspect.stack()
    function_dir = [f[1] for f in stack if "handler.py" in f[1]][0]
    function_path = Path(function_dir)
    while function_path.parts[-1] != "function":
        function_path = function_path.parent
        if function_path == Path("/"):
            raise BaseException("Could not find function folder.")
    print(function_path)
    return function_path / Path("config.yaml")


def retrieve_field_definitions(path_to_config: Path):
    fields: Dict = _load_yaml(path_to_config).get("fields", {})
    output = []
    for i in fields.keys():
        output.append({**{"id": i}, **fields[i]})
    return json.dumps(output)


def retrieve_backfilling(data):
    path_to_config = path_to_yaml(data)
    return _load_yaml(path_to_config).get("modelSettings").get("backfill")


def retrieve_model_name(data: Dict):
    if data.get(AIR_DATA_MODEL_NAME, False):
        return data[AIR_DATA_MODEL_NAME]
    cwd = os.getcwd()
    print(cwd)
    model_name = Path(cwd).parent.parent.parts[-1]
    print(model_name)
    return model_name


def retrieve_model_version(data):
    path_to_config = path_to_yaml(data)
    model_version = _load_yaml(path_to_config).get("modelSettings").get("modelVersion")
    return strip_patch_from_version(model_version)


def create_fake_backfilling_asset():
    pass
