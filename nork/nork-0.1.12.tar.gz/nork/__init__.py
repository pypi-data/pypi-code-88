"""
                              $$\ 
                              $$ |
$$$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |
$$ |  $$ |$$ /  $$ |$$ |  \__|$$$$$$  / 
$$ |  $$ |$$ |  $$ |$$ |      $$  _$$<  
$$ |  $$ |\$$$$$$  |$$ |      $$ | \$$\ 
\__|  \__| \______/ \__|      \__|  \__|
"""
from nork.core import paths
import toml

__version__ = "0.1.12"

config = dict()

try:
    config = toml.load(f=f"{paths.PROJECT_PATH}/nork.toml")
except Exception as exception:
    pass
