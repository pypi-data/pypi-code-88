"""
Information about the frontend package of the widgets.
"""
import json
from pathlib import Path

with open(Path(__file__).parents[1] / "package.json", "r") as f:
    package_info = json.load(f)

module_name = package_info["name"]
module_version = package_info['version']
