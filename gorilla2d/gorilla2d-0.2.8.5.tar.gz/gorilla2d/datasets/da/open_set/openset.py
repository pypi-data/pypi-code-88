# modified from: https://github.com/thuml/Transfer-Learning-Library/blob/master/common/vision/datasets/openset/__init__.py
from ..imagelist import ImageList
from ..office31 import Office31
from ..officehome import OfficeHome
from ..visda2017 import VisDA2017

from typing import Optional, Sequence
from copy import deepcopy

def open_set_wrapper(dataset_class: ImageList,
                     public_classes: Optional[Sequence[str]] = (),
                     private_classes: Optional[Sequence[str]] = (),
                     source: bool = True) -> ImageList:
    """
    A wrapper to convert a dataset into its open-set version.

    In other words, those samples which doesn't belong to `private_classes` will be marked as "unknown".
    Be aware that `open_set` will change the label number of each category.

    Args:
        dataset_class (class): Dataset class. Only subclass of ``ImageList`` can be open-set.
            Currently, dataset_class must be one of
            :class:`~gorilla2d.datasets.office31.Office31`,
            :class:`~gorilla2d.datasets.officehome.OfficeHome`,
            :class:`~gorilla2d.datasets.visda2017.VisDA2017`.
        public_classes (sequence[str]): A sequence of which categories need to be kept in the open-set dataset.
            Each element of `public_classes` must belong to the `classes` list of `dataset_class`.
        private_classes (sequence[str], optional): A sequence of which categories need to be marked as "unknown"
            in the open-set dataset. Each element of `private_classes` must belong to the `classes` list of
            `dataset_class`. Default: ().
        source (bool): Only useful when `public_classes` and `private_classes` are not given.
            Whether the dataset is used for source domain or not.

    Examples:
        >>> public_classes = ['back_pack', 'bike', 'calculator', 'headphones', 'keyboard']
        >>> private_classes = ['laptop_computer', 'monitor', 'mouse', 'mug', 'projector']
        >>> # create a open-set dataset class which has classes
        >>> # 'back_pack', 'bike', 'calculator', 'headphones', 'keyboard' and 'unknown'.
        >>> OpenSetOffice31 = open_set_wrapper(Office31, public_classes, private_classes)
        >>> # create an instance of the open-set dataset
        >>> dataset = OpenSetOffice31(root="data/office31", domain="A")
        >>> # if `public_classes` and `private_classes` are not given, they will follow default
        >>> # spliting method, and `source` is needed
        >>> OpenSetOffice31 = open_set_wrapper(Office31, source=True)

    """
    if not (issubclass(dataset_class, ImageList)):
        raise Exception("Only subclass of ImageList can be openset")

    if len(public_classes) == 0 and len(private_classes) == 0:
        # Default spliting setting used in some open-set paper.
        if dataset_class == Office31:
            public_classes = Office31.classes[:20]
            if source:
                private_classes = ()
            else:
                private_classes = Office31.classes[20:]
        elif dataset_class == OfficeHome:
            public_classes = sorted(OfficeHome.classes)[:25]
            if source:
                private_classes = ()
            else:
                private_classes = sorted(OfficeHome.classes)[25:]
        elif dataset_class == VisDA2017:
            public_classes = ('bicycle', 'bus', 'car', 'motorcycle', 'train', 'truck')
            if source:
                private_classes = ()
            else:
                private_classes = ('aeroplane', 'horse', 'knife', 'person', 'plant', 'skateboard')
        else:
            raise NotImplementedError("Unknown openset domain adaptation dataset: {}".format(dataset_class.__name__))

    class OpenSetDataset(dataset_class):
        def __init__(self, **kwargs):
            super(OpenSetDataset, self).__init__(**kwargs)
            assert all([c in self.classes for c in public_classes]
                ), "Some words of `public_classes` is not in `self.classes`, please check `public_classes` again."
            assert all([c in self.classes for c in private_classes]
                ), "Some words of `private_classes` is not in `self.classes`, please check `private_classes` again."
            paths, targets = [], []
            all_classes = list(public_classes) + ["unknown"]
            for (path, label) in zip(self.paths, self.targets):
                class_name = self.classes[label]
                if class_name in public_classes:
                    paths.append(path)
                    targets.append(all_classes.index(class_name))
                elif class_name in private_classes:
                    paths.append(path)
                    targets.append(all_classes.index("unknown"))
            self.paths = paths
            self.targets = targets
            self.classes = all_classes
            self.class_to_idx = {cls: idx for idx, cls in enumerate(self.classes)}

    return OpenSetDataset
