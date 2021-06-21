# modified from: https://github.com/thuml/Transfer-Learning-Library/blob/master/common/vision/datasets/partial/__init__.py
from ..imagelist import ImageList
from ..office31 import Office31
from ..officehome import OfficeHome
from ..visda2017 import VisDA2017
from ..officecaltech import OfficeCaltech
from typing import Optional, Sequence


# TODO: add 'CaltechImageNet' and 'ImageNetCaltech' from dalib
def partial_set_wrapper(dataset_class: ImageList,
                        partial_classes: Optional[Sequence[str]] = ()) -> ImageList:
    """
    A wrapper to convert a dataset into its partial-set version.

    In other words, those samples which doesn't belong to `partial_classes` will be discarded.
    Yet `partial` will not change the label space of `dataset_class`.

    Args:
        dataset_class (class): Dataset class. Only subclass of ``ImageList`` can be partial.
            Currently, dataset_class must be one of
            :class:`~gorilla2d.datasets.office31.Office31`,
            :class:`~gorilla2d.datasets.officehome.OfficeHome`,
            :class:`~gorilla2d.datasets.visda2017.VisDA2017`.        
        partial_classes (sequence[str]): A sequence of which categories need to be kept in the partial dataset.\
            Each element of `partial_classes` must belong to the `classes` list of `dataset_class`.

    Examples:
        >>> partial_classes = ['back_pack', 'bike', 'calculator', 'headphones', 'keyboard']
        >>> # create a partial dataset class which has classes
        >>> # 'back_pack', 'bike', 'calculator', 'headphones', 'keyboard'
        >>> PartialOffice31 = partial_set_wrapper(Office31, partial_classes)
        >>> # create an instance of the partial dataset
        >>> dataset = PartialOffice31(root="data/office31", domain="A")
        >>> # if `partial_classes` is not given, it will follow default spliting method
        >>> PartialOffice31 = partial_set_wrapper(Office31)

    """
    if not (issubclass(dataset_class, ImageList)):
        raise Exception("Only subclass of ImageList can be partial")

    if len(partial_classes) == 0:
        # Default spliting setting used in some partial-set paper.
        if dataset_class == Office31:
            partial_classes = OfficeCaltech.classes
        elif dataset_class == OfficeHome:
            partial_classes = sorted(OfficeHome.classes)[:25]
        elif dataset_class == VisDA2017:
            partial_classes = sorted(VisDA2017.classes)[:6]
        else:
            raise NotImplementedError("Unknown partial domain adaptation dataset: {}".format(dataset_class.__name__))

    class PartialDataset(dataset_class):
        def __init__(self, **kwargs):
            super(PartialDataset, self).__init__(**kwargs)
            assert all([c in self.classes for c in partial_classes]
                ), "Some words of `partial_classes` is not in `self.classes`, please check `partial_classes` again."
            paths, targets = [], []
            for (path, label) in zip(self.paths, self.targets):
                class_name = self.classes[label]
                if class_name in partial_classes:
                    paths.append(path)
                    targets.append(label)
            self.paths = paths
            self.targets = targets
            self.classes = partial_classes
            self.class_to_idx = {cls: self.class_to_idx[cls] for cls in partial_classes}

    return PartialDataset
