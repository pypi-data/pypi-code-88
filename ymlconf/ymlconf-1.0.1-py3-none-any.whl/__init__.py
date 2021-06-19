"""Top-level package for yamlconf."""

from ._version import get_versions
from .attribute import Attribute
from .yaml_config_manager import YamlConfigError, YamlConfigManager

__author__ = """qin hong wei"""
__email__ = "1039954093@qq.com"
__version__ = get_versions()["version"]
del get_versions

__all__ = [
    "Attribute",
    "YamlConfigError",
    "YamlConfigManager",
]
