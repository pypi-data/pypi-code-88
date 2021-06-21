# modify from https://github.com/thuml/Transfer-Learning-Library
from .imagelist import ImageList
from .office31 import Office31
from .officehome import OfficeHome
from .visda2017 import VisDA2017
from .officecaltech import OfficeCaltech
from .domainnet import DomainNet
from .digit import Digit
from .open_set import open_set_wrapper
from .partial_set import partial_set_wrapper

__all__ = [
    "ImageList", "Office31", "OfficeHome", "VisDA2017", "OfficeCaltech",
    "DomainNet", "Digit", "open_set_wrapper", "partial_set_wrapper"
]
