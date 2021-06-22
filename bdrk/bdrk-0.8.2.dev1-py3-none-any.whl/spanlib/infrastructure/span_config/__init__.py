import os
import re

config_version_path = os.path.dirname(__file__)

VALID_SPAN_CONFIG_VERSIONS = [
    file
    for file in os.listdir(config_version_path)
    if os.path.isdir(os.path.join(config_version_path, file)) and re.search(r"^v\d", file)
]
