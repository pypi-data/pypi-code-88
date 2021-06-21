# modify from https://github.com/thuml/Transfer-Learning-Library
from ._utils import download as download_data, check_exits
from .da import ImageList
from .da import Office31, OfficeHome, VisDA2017, OfficeCaltech, DomainNet, Digit
from .da import open_set_wrapper, partial_set_wrapper
# CIFAR10 and CIFAR100 in cls.py are registered manually, so they should not be import here to avoid register twice
from . import cls
from .ssl import CIFAR10SSL, CIFAR100SSL

# Registry mechanism support defining custom Dataset class in a project.
# auto_registry should be placed behind all Dataset class and in front of
# other class (it doesn't matter for functions)
from gorilla import DATASETS, auto_registry
auto_registry(DATASETS, globals())

from .transforms import ResizeImage
from .randaugment import RandAugment
# this command should be bottom to avoid that some packages have not been imported when used
from .dataset_wrappers import repeat_dataset_wrapper, ClassBalancedDataset
from .dataloader import build_dataloaders

__all__ = ["ImageList", "Office31", "OfficeHome", "VisDA2017", "OfficeCaltech", "DomainNet"]
