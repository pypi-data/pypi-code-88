from albumentations.augmentations.transforms import VerticalFlip, \
    HorizontalFlip, Flip, Normalize, ToFloat, RandomRotate90
from albumentations.core.composition import Compose, OneOf, OneOrOther

from .rotate_extended import Rotate
import logging

__all__ = ['Rotate', 'build_pipeline', 'VerticalFlip',
           'HorizontalFlip', 'Flip', 'Normalize',
           'ToFloat', 'RandomRotate90', 'OneOf',
           'OneOrOther', 'Compose']


def build_pipeline(args):
    """Create train and val augmentation pipelines from args.

    Parameters
    ----------
    args : dict
        Arguments dictionary.

    Returns
    -------
    Compose,Compose
        (train pipeline,val pipeline)
    """
    logging.debug("Enter build_pipeline routine")
    train_aug_dict = args.train_augs
    val_aug_dict = args.val_augs
    train_aug_pipeline = process_aug_dict(train_aug_dict)
    val_aug_pipeline = process_aug_dict(val_aug_dict)

    logging.debug("Exit build_pipeline routine")
    return train_aug_pipeline, val_aug_pipeline


def _check_augs(augs):
    """Check if augmentations are loaded in already or not.

    Parameters
    ----------
    augs : dict/Compose
        loaded/unloaded augmentations.

    Returns
    -------
    Compose
        loaded augmentations.

    """
    logging.debug("Enter _check_augs routine")
    if isinstance(augs, dict):
        return process_aug_dict(augs)
    elif isinstance(augs, Compose):
        return augs


def process_aug_dict(pipeline_dict, meta_augs_list=['oneof', 'oneorother']):
    """Create a Compose object from an augmentation config dict.

    Parameters
    ----------
    pipeline_dict : dict
        augmentation config dictionary.
    meta_augs_list : type
        list of meta augmentations.

    Returns
    -------
    Compose
        Compose object formed from augmentation dictionary.

    """
    logging.debug("Enter process_aug_dict routine")
    if pipeline_dict is None:
        return None
    p = pipeline_dict.get('p', 1.0)  # probability of applying augs in pipeline
    xforms = pipeline_dict['augmentations']
    composer_list = get_augs(xforms, meta_augs_list)
    logging.debug("Exit process_aug_dict routine")
    return Compose(composer_list, p=p)


def get_augs(aug_dict, meta_augs_list=['oneof', 'oneorother']):
    """Get the set of augmentations contained in a dict.

    Parameters
    ----------
    aug_dict : dict
        dictionary containing augmentations.
    meta_augs_list : list
        list of meta augmentations.

    Returns
    -------
    list
        list of augmentations.

    """
    logging.debug("Enter get_augs routine")
    aug_list = []
    if aug_dict is not None:
        for aug, params in aug_dict.items():
            if aug.lower() in meta_augs_list:
                # recurse into sub-dict
                aug_list.append(aug_matcher[aug](get_augs(aug_dict[aug])))
            else:
                aug_list.append(_get_aug(aug, params))
    logging.debug("Exit get_augs routine")
    return aug_list


def _get_aug(aug, params):
    """Get augmentations (recursively if needed) from items in the aug_dict.

    Parameters
    ----------
    aug : str
        string describing augmentation.
    params : dict
        dictionary of augmentation parameters.

    Returns
    -------
    albumentations.augmentations.transforms
        augmentation object.

    """
    aug_obj = aug_matcher[aug.lower()]
    if params is None:
        return aug_obj()
    elif isinstance(params, dict):
        return aug_obj(**params)
    else:
        raise ValueError(
            '{} is not a valid aug param (must be dict of args)'.format(params))


"""Enumeration mapping augmentations to their respective classes"""
aug_matcher = {
    'verticalflip': VerticalFlip, 'horizontalflip': HorizontalFlip,
    'flip': Flip, 'normalize': Normalize, 'tofloat': ToFloat,
    'randomrotate90': RandomRotate90, 'rotate': Rotate, 'oneof': OneOf
}
