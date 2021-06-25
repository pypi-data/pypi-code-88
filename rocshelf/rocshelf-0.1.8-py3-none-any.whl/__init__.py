""" rocshelf - препроцессор для компиляции веб-страниц из составляющих частей с параллельной модернизацией.

За основу взята идея максимального разделение кода на независимые части, которые сливаются в единое целое при компиляции.

"""

from rcore.utils import gen_user_workspace

from rocshelf import main
from rocshelf.main import set_config, set_path, start_cli
from rocshelf.middleware import UICompile, UIRoute, UIShelves, UIIntegration

# alpha release
__version__ = '0.1.8'