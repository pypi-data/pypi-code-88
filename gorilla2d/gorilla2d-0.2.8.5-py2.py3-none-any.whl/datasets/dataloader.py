# Copyright (c) Gorilla-Lab. All rights reserved.
import os.path as osp
from PIL import Image

import torch
import torchvision.transforms as transforms

from gorilla import DATASETS, build_dataloader
from gorilla2d.datasets import ResizeImage, RandAugment
from gorilla2d.datasets import open_set_wrapper, partial_set_wrapper
from .dataset_wrappers import repeat_dataset_wrapper

def default_loader(path):
    # open path as file to avoid ResourceWarning (https://github.com/python-pillow/Pillow/issues/835)
    with open(path, 'rb') as f:
        img = Image.open(f)
        img_PIL = img.convert('RGB')

    return img_PIL


def _select_image_process(dataset, DATA_TRANSFORM_TYPE="simple"):
    if dataset in ["Digit"]:
        return _select_image_process_digit(DATA_TRANSFORM_TYPE=DATA_TRANSFORM_TYPE)
    elif dataset in ["CIFAR10", "CIFAR100"]:
        # TODO: add support for SVHN and STL-10
        return _select_image_process_ssl(dataset, DATA_TRANSFORM_TYPE=DATA_TRANSFORM_TYPE)

    normalize = transforms.Normalize(mean=(0.485, 0.456, 0.406),
                                     std=(0.229, 0.224, 0.225
                                          ))  # the mean and std of ImageNet

    if DATA_TRANSFORM_TYPE == "old":
        transform_train = transforms.Compose([
            transforms.Resize(256),
            transforms.RandomCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize,
        ])
    elif DATA_TRANSFORM_TYPE == "simple":
        transform_train = transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize,
        ])
    elif DATA_TRANSFORM_TYPE == "long":
        transform_train = transforms.Compose([
            ResizeImage(256),
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize
        ])
    elif DATA_TRANSFORM_TYPE == "strong":
        transform_train = dict(
            img_weak = transforms.Compose([
                transforms.Resize(224),
                transforms.ToTensor(),
                normalize,
            ]),
            img_strong = transforms.Compose([
                transforms.Resize(224),
                RandAugment(2, 10),
                transforms.ToTensor(),
                normalize,
            ]))
    else:
        raise NotImplementedError("DATA_TRANSFORM_TYPE: {}".format(DATA_TRANSFORM_TYPE))

    transform_test = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        normalize,
    ])

    return transform_train, transform_test


def _select_image_process_digit(DATA_TRANSFORM_TYPE="simple"):
    # NOTE: transform_train and transform_test here are mappings, not Compose
    transform_train = {'svhn': {}, 'mnist': {}, 'usps': {}}

    transform_train['svhn']['mnist'] = transforms.Compose([
                                        transforms.ToTensor(),
                                        # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                                        ])
    transform_train['svhn']['usps'] = transform_train['svhn']['mnist']
    transform_train['mnist']['svhn'] = transforms.Compose([
                                        transforms.Resize(32),
                                        # transforms.RandomCrop(32, padding=4),
                                        # transforms.RandomRotation(10),
                                        transforms.Lambda(lambda x: x.convert("RGB")),
                                        transforms.ToTensor(),
                                        # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                                        ])
    transform_train['mnist']['usps'] = transforms.Compose([
                                        # transforms.RandomCrop(28, padding=4),
                                        # transforms.RandomRotation(10),
                                        transforms.ToTensor(),
                                        # transforms.Normalize((0.5,), (0.5,))
                                        ])
    transform_train['usps']['svhn'] = transform_train['mnist']['svhn']
    transform_train['usps']['mnist'] = transforms.Compose([
                                        transforms.Resize(28),
                                        # transforms.RandomCrop(28, padding=4),
                                        # transforms.RandomRotation(10),
                                        transforms.ToTensor(),
                                        # transforms.Normalize((0.5,), (0.5,))
                                        ])

    transform_test = {'svhn': {}, 'mnist': {}, 'usps': {}}

    transform_test['svhn']['mnist'] = transforms.Compose([
                                        transforms.ToTensor(),
                                        # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                                        ])
    transform_test['svhn']['usps'] = transform_test['svhn']['mnist']
    transform_test['mnist']['svhn'] = transforms.Compose([
                                        transforms.Resize(32),
                                        transforms.Lambda(lambda x: x.convert("RGB")),
                                        transforms.ToTensor(),
                                        # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                                        ])
    transform_test['mnist']['usps'] = transforms.Compose([
                                        transforms.ToTensor(),
                                        # transforms.Normalize((0.5,), (0.5,))
                                        ])
    transform_test['usps']['svhn'] = transform_test['mnist']['svhn']
    transform_test['usps']['mnist'] = transforms.Compose([
                                        transforms.Resize(28),
                                        transforms.ToTensor(),
                                        # transforms.Normalize((0.5,), (0.5,))
                                        ])

    return transform_train, transform_test

# modified from https://github.com/kekmodel/FixMatch-pytorch/blob/master/dataset/cifar.py
def _select_image_process_ssl(dataset, DATA_TRANSFORM_TYPE="simple"):
    # mean and std of CIFAR10 and CIFAR100 are copied from `FixMatch-pytorch`
    if dataset == "CIFAR10":
        mean = (0.4914, 0.4822, 0.4465)
        std = (0.2471, 0.2435, 0.2616)
    elif dataset == "CIFAR100":
        mean = (0.5071, 0.4867, 0.4408)
        std = (0.2675, 0.2565, 0.2761)
    else:
        raise NotImplementedError(f"Data normalization of dataset {dataset}")
    normalize = transforms.Normalize(mean=mean, std=std)

    if DATA_TRANSFORM_TYPE == "simple":
        # TODO: fill in the blank
        transform_labeled = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomCrop(size=32, padding=4, padding_mode='reflect'),
            transforms.ToTensor(),
            normalize
        ])
        transform_unlabeled = transform_labeled
    elif DATA_TRANSFORM_TYPE == "RandAug":
        # copied from `FixMatch-pytorch`
        transform_labeled = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomCrop(size=32, padding=4, padding_mode='reflect'),
            transforms.ToTensor(),
            normalize
        ])

        transform_unlabeled = dict(
            img_weak = transform_labeled,
            img_strong = transforms.Compose([
                transforms.RandomHorizontalFlip(),
                transforms.RandomCrop(size=32, padding=4, padding_mode='reflect'),
                RandAugment(2, 10, cutout_size=16),
                transforms.ToTensor(),
                normalize,
            ]))
    else:
        raise NotImplementedError("DATA_TRANSFORM_TYPE: {}".format(DATA_TRANSFORM_TYPE))

    transform_test = transforms.Compose([
        transforms.ToTensor(),
        normalize
    ])

    return transform_labeled, transform_unlabeled, transform_test


def build_dataloaders(cfg):
    if "task" not in cfg or cfg.task == "DA":
        return build_dataloaders_da(cfg)
    elif cfg.task == "SSL":
        return build_dataloaders_ssl(cfg)
    else:
        raise NotImplementedError(f"task: {cfg.task}")


def build_dataloaders_da(cfg):
    r"""Build dataloaders of source and target domain for training and testing."""
    if "da_setting" in cfg and cfg.da_setting != "close":
        if cfg.da_setting == "open":
            return build_dataloaders_openset(cfg)
        elif cfg.da_setting == "partial":
            return build_dataloaders_partialset(cfg)
        else:
            raise ValueError(f"da_setting should be in ['close', 'open', 'partial'], but got {cfg.da_setting}")

    Dataset = DATASETS.get(cfg.dataset)
    if cfg.dataset == "Digit":
        transform_train, transform_test = _select_image_process_digit(cfg.transform_type)
    else:
        transform_train, transform_test = _select_image_process(cfg.transform_type)

    cfg.train_set = True # only used for Digit dataset
    train_dataset_source = Dataset(root=osp.join(cfg.data_root, cfg.dataset),
                                   domain=cfg.source,
                                   transform=transform_train,
                                   cfg=cfg)
    cfg.num_classes = train_dataset_source.num_classes
    # at torch version above 1.0.0, it will cause many warnings like:
    # OMP: Warning #190: Forking a process while a parallel region is active is potentially unsafe.
    # when pin_memory=True, so it is turned to False
    train_dataset_cfg = dict(batch_size=cfg.samples_per_gpu,
                             shuffle=True,
                             num_workers=cfg.workers_per_gpu,
                             pin_memory=False,
                             sampler=None,
                             drop_last=True)
    train_loader_source = build_dataloader(train_dataset_source, train_dataset_cfg)

    train_dataset_target = Dataset(root=osp.join(cfg.data_root, cfg.dataset),
                                   domain=cfg.target,
                                   transform=transform_train,
                                   cfg=cfg)
    train_loader_target = build_dataloader(train_dataset_target, train_dataset_cfg)

    cfg.train_set = False # only used for Digit dataset
    test_dataset_target = Dataset(root=osp.join(cfg.data_root, cfg.dataset),
                                   domain=cfg.target,
                                   transform=transform_test,
                                   cfg=cfg)

    test_dataset_cfg = dict(batch_size=cfg.samples_per_gpu,
                            shuffle=False,
                            num_workers=cfg.workers_per_gpu,
                            pin_memory=False,
                            sampler=None)
    test_loader_target = build_dataloader(test_dataset_target, test_dataset_cfg)

    return {
        "train_src": train_loader_source,
        "train_tgt": train_loader_target,
        "test_tgt": test_loader_target,
    }


def build_dataloaders_openset(cfg):
    Dataset = DATASETS.get(cfg.dataset)
    if cfg.dataset == "Digit":
        transform_train, transform_test = _select_image_process_digit(cfg.transform_type)
    else:
        transform_train, transform_test = _select_image_process(cfg.transform_type)
    public_classes = cfg.public_classes if "public_classes" in cfg else ()
    private_classes_src = cfg.private_classes_src if "private_classes_src" in cfg else ()
    private_classes_tgt = cfg.private_classes_tgt if "private_classes_tgt" in cfg else ()

    SrcDataset = open_set_wrapper(Dataset, public_classes, private_classes_src, source=True)
    TgtDataset = open_set_wrapper(Dataset, public_classes, private_classes_tgt, source=False)

    cfg.train_set = True # only used for Digit dataset
    train_dataset_source = SrcDataset(root=osp.join(cfg.data_root, cfg.dataset),
                                                    domain=cfg.source,
                                                    transform=transform_train,
                                                    cfg=cfg)

    cfg.num_classes = train_dataset_source.num_classes
    # at torch version above 1.0.0, it will cause many warnings like:
    # OMP: Warning #190: Forking a process while a parallel region is active is potentially unsafe.
    # when pin_memory=True, so it is turned to False
    train_dataset_cfg = dict(batch_size=cfg.samples_per_gpu,
                             shuffle=True,
                             num_workers=cfg.workers_per_gpu,
                             pin_memory=False,
                             sampler=None,
                             drop_last=True)
    train_loader_source = build_dataloader(train_dataset_source, train_dataset_cfg)

    train_dataset_target = TgtDataset(root=osp.join(cfg.data_root, cfg.dataset),
                                                    domain=cfg.target,
                                                    transform=transform_train,
                                                    cfg=cfg)
    train_loader_target = build_dataloader(train_dataset_target, train_dataset_cfg)

    cfg.train_set = False # only used for Digit dataset
    test_dataset_target = TgtDataset(root=osp.join(cfg.data_root, cfg.dataset),
                                                   domain=cfg.target,
                                                   transform=transform_test,
                                                   cfg=cfg)

    test_dataset_cfg = dict(batch_size=cfg.samples_per_gpu,
                            shuffle=False,
                            num_workers=cfg.workers_per_gpu,
                            pin_memory=False,
                            sampler=None)
    test_loader_target = build_dataloader(test_dataset_target, test_dataset_cfg)

    return {
        "train_src": train_loader_source,
        "train_tgt": train_loader_target,
        "test_tgt": test_loader_target,
    }


def build_dataloaders_partialset(cfg):
    Dataset = DATASETS.get(cfg.dataset)
    if cfg.dataset == "Digit":
        transform_train, transform_test = _select_image_process_digit(cfg.transform_type)
    else:
        transform_train, transform_test = _select_image_process(cfg.transform_type)
    partial_classes = cfg.partial_classes if "partial_classes" in cfg else ()

    TgtDataset = partial_set_wrapper(Dataset, partial_classes)

    cfg.train_set = True # only used for Digit dataset
    train_dataset_source = Dataset(root=osp.join(cfg.data_root, cfg.dataset),
                                   domain=cfg.source,
                                   transform=transform_train,
                                   cfg=cfg)

    cfg.num_classes = train_dataset_source.num_classes
    # at torch version above 1.0.0, it will cause many warnings like:
    # OMP: Warning #190: Forking a process while a parallel region is active is potentially unsafe.
    # when pin_memory=True, so it is turned to False
    train_dataset_cfg = dict(batch_size=cfg.samples_per_gpu,
                             shuffle=True,
                             num_workers=cfg.workers_per_gpu,
                             pin_memory=False,
                             sampler=None,
                             drop_last=True)
    train_loader_source = build_dataloader(train_dataset_source, train_dataset_cfg)

    train_dataset_target = TgtDataset(root=osp.join(cfg.data_root, cfg.dataset),
                                                    domain=cfg.target,
                                                    transform=transform_train,
                                                    cfg=cfg)
    train_loader_target = build_dataloader(train_dataset_target, train_dataset_cfg)

    cfg.train_set = False # only used for Digit dataset
    test_dataset_target = TgtDataset(root=osp.join(cfg.data_root, cfg.dataset),
                                                   domain=cfg.target,
                                                   transform=transform_test,
                                                   cfg=cfg)

    test_dataset_cfg = dict(batch_size=cfg.samples_per_gpu,
                            shuffle=False,
                            num_workers=cfg.workers_per_gpu,
                            pin_memory=False,
                            sampler=None)
    test_loader_target = build_dataloader(test_dataset_target, test_dataset_cfg)

    return {
        "train_src": train_loader_source,
        "train_tgt": train_loader_target,
        "test_tgt": test_loader_target,
    }


def build_dataloaders_ssl(cfg):
    r"""Build dataloaders for training and testing in semi-supervised learning task."""
    if cfg.dataset in ["CIFAR10", "CIFAR100"]:
        # compatibility processing of CIFAR dataset in supervised and semi-supervised tasks
        SSLDataset = DATASETS.get(cfg.dataset + "SSL")
        Dataset = DATASETS.get(cfg.dataset)
    else:
        Dataset = DATASETS.get(cfg.dataset)

    transform_labeled, transform_unlabeled, transform_test = _select_image_process(
        cfg.dataset, cfg.transform_type)

    # NOTE: unlabeled data contains all data including labeled data (https://github.com/kekmodel/FixMatch-pytorch/issues/10)
    unlabeled_dataset = Dataset(root=osp.join(cfg.data_root, cfg.dataset),
                                train=True,
                                transform=transform_unlabeled)

    cfg.num_classes = unlabeled_dataset.num_classes
    # at torch version above 1.0.0, it will cause many warnings like:
    # OMP: Warning #190: Forking a process while a parallel region is active is potentially unsafe.
    # when pin_memory=True, so it is turned to False
    train_dataset_cfg = dict(batch_size=cfg.mu * cfg.samples_per_gpu,
                             shuffle=True,
                             num_workers=cfg.workers_per_gpu,
                             pin_memory=False,
                             sampler=None,
                             drop_last=True)
    unlabeled_loader = build_dataloader(unlabeled_dataset, train_dataset_cfg)

    # use repeat_dataset_wrapper to enlarge labeled dataset
    SSLDataset = repeat_dataset_wrapper(SSLDataset, int(len(unlabeled_dataset) / unlabeled_dataset.num_classes / cfg.num_labeled_per_class))
    labeled_dataset = SSLDataset(root=osp.join(cfg.data_root, cfg.dataset),
                              train=True,
                              transform=transform_labeled,
                              seed=cfg.data_seed,
                              num_labeled_per_class=cfg.num_labeled_per_class)
    train_dataset_cfg["batch_size"] = cfg.samples_per_gpu
    labeled_loader = build_dataloader(labeled_dataset, train_dataset_cfg)

    test_dataset = Dataset(root=osp.join(cfg.data_root, cfg.dataset),
                               train=False,
                               transform=transform_test)

    test_dataset_cfg = dict(batch_size=cfg.samples_per_gpu,
                            shuffle=False,
                            num_workers=cfg.workers_per_gpu,
                            pin_memory=False,
                            sampler=None)
    test_loader = build_dataloader(test_dataset, test_dataset_cfg)

    return {
        "train_label": labeled_loader,
        "train_unlabel": unlabeled_loader,
        "test": test_loader,
    }
