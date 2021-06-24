import math
from typing import Tuple, Generator, Optional, List, Union, TypeVar

import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit, StratifiedKFold, KFold, ShuffleSplit

from sfu_ml_lib.base.dataset import Dataset


SizeType = Union[int, float]
DatasetType = TypeVar('DatasetType', bound=Dataset)


def get_dataset_folds(
        dataset: DatasetType,
        number_folds: int = 10,
        validation_size: Optional[SizeType] = None,
        random_state: int = 110069) -> Generator[Tuple[DatasetType, Optional[DatasetType], DatasetType], None, None]:
    """
    Creates multiple folds suitable for cross-validation, meaning there's no overlap of example within the test sets
    produced in each fold.
    :param dataset: A `Dataset` object.
    :param number_folds: Number of folds to use.
    :param validation_size: If float this is the proportion of the training split to use as validation. Having it
    set to None or zero means there is no validation set.
    :param random_state: A seed for random number generation.
    :return: A generator of size `number_folds` with a tuple of up to three datasets corresponding to the splits.
    """
    train_test_folder = KFold(n_splits=number_folds, shuffle=True, random_state=random_state)

    for train_validation_indices, test_indices in train_test_folder.split(np.empty(dataset.size, dtype=np.bool)):
        test_dataset = dataset.subset(test_indices)

        if not validation_size:
            train_dataset = dataset.subset(train_validation_indices)

            yield train_dataset, None, test_dataset

        else:
            train_validation_splitter = ShuffleSplit(n_splits=1, test_size=validation_size, random_state=random_state)

            train_validation_inputs = np.empty(train_validation_indices.size, dtype=np.bool)
            subset_train_indices, subset_validation_indices = next(train_validation_splitter.split(
                X=train_validation_inputs,
            ))

            train_dataset = dataset.subset(train_validation_indices[subset_train_indices])
            validation_dataset = dataset.subset(train_validation_indices[subset_validation_indices])

            yield train_dataset, validation_dataset, test_dataset


def get_dataset_splits(
        dataset: DatasetType,
        train_size: SizeType,
        validation_size: Optional[SizeType] = None,
        test_size: Optional[SizeType] = None,
        number_splits: int = 10,
        random_state: int = 110069) -> Generator[
            Tuple[DatasetType, Optional[DatasetType], Optional[DatasetType]],
            None,
            None]:
    """
    Creates multiple splits of the dataset.
    :param dataset: A `Dataset` object.
    :param train_size: Number of examples or a proportion of the dataset.
    :param validation_size: Number of examples or a proportion of the dataset. Having it set to None means it uses the
    complement of the train set and the test set. If both `validation_size` and `test_size` are None then
    a validation set is created with the complement of the train set.
    :param test_size: Number of examples or a proportion of the dataset. Having it set to None means it uses the
    complement of the train set and the validation set. If both `validation_size` and `test_size` are None then
    a test set is not created.
    :param number_splits: Number of splits to generate.
    :param random_state: A seed for random number generation.
    :return: A generator of size `number_splits` with a tuple of up to three datasets corresponding to the splits.
    """
    train_size, validation_size, test_size = get_sizes(dataset.size, train_size, validation_size, test_size)

    train_test_splitter = ShuffleSplit(
        n_splits=number_splits,
        train_size=train_size,
        test_size=validation_size + test_size,
        random_state=random_state,
    )

    for train_indices, validation_test_indices in train_test_splitter.split(np.empty(dataset.size, dtype=np.bool)):
        train_dataset = dataset.subset(train_indices)

        if not validation_size and not test_size:
            yield train_dataset, None, None

        if not test_size:
            validation_dataset = dataset.subset(validation_test_indices)

            yield train_dataset, validation_dataset, None

        else:
            validation_test_splitter = ShuffleSplit(
                n_splits=1,
                train_size=validation_size,
                test_size=test_size,
                random_state=random_state,
            )

            validation_test_inputs = np.empty(validation_test_indices.size, dtype=np.bool)
            subset_validation_indices, subset_test_indices = next(validation_test_splitter.split(
                X=validation_test_inputs,
            ))

            validation_dataset = dataset.subset(validation_test_indices[subset_validation_indices])
            test_dataset = dataset.subset(validation_test_indices[subset_test_indices])

            yield train_dataset, validation_dataset, test_dataset


def get_stratified_dataset_folds(
        dataset: DatasetType,
        number_folds: int = 10,
        validation_size: Optional[SizeType] = None,
        random_state: int = 110069) -> Generator[Tuple[DatasetType, Optional[DatasetType], DatasetType], None, None]:
    """
    Creates multiple folds suitable for cross-validation, meaning there's no overlap of example within the test sets
    produced in each fold.
    Tries to maintain the same distribution of classes in the dataset across types and folds.
    :param dataset: A `Dataset` object.
    :param number_folds: Number of folds to use.
    :param validation_size: If float this is the proportion of the training split to use as validation. Having it
    set to None or zero means there is no validation set.
    :param random_state: A seed for random number generation.
    :return: A generator of size `number_folds` with a tuple of up to three datasets corresponding to the splits.
    """
    assert dataset.targets is not None

    train_test_folder = StratifiedKFold(n_splits=number_folds, shuffle=True, random_state=random_state)

    fake_data = np.zeros_like(dataset.targets)

    for train_validation_indices, test_indices in train_test_folder.split(fake_data, dataset.targets):
        test_dataset = dataset.subset(test_indices)

        if not validation_size:
            train_dataset = dataset.subset(train_validation_indices)

            yield train_dataset, None, test_dataset

        else:
            train_validation_splitter = StratifiedShuffleSplit(
                n_splits=1,
                test_size=validation_size,
                random_state=random_state,
            )

            train_validation_targets = dataset.targets[train_validation_indices]

            subset_train_indices, subset_validation_indices = next(train_validation_splitter.split(
                X=np.zeros_like(train_validation_targets),
                y=train_validation_targets,
            ))

            train_indices = train_validation_indices[subset_train_indices]
            validation_indices = train_validation_indices[subset_validation_indices]

            train_dataset = dataset.subset(train_indices)
            validation_dataset = dataset.subset(validation_indices)

            yield train_dataset, validation_dataset, test_dataset


def get_stratified_dataset_splits(
        dataset: DatasetType,
        train_size: SizeType,
        validation_size: Optional[SizeType] = None,
        test_size: Optional[SizeType] = None,
        number_splits: int = 10,
        random_state: int = 110069) -> Generator[
            Tuple[DatasetType, Optional[DatasetType], Optional[DatasetType]],
            None,
            None]:
    """
    Creates multiple splits of the dataset.
    Tries to maintain the same distribution of classes in the dataset across types and splits.
    :param dataset: A `Dataset` object.
    :param train_size: Number of examples or a proportion of the dataset.
    :param validation_size: Number of examples or a proportion of the dataset. Having it set to None means it uses the
    complement of the train set and the test set. If both `validation_size` and `test_size` are None then
    a validation set is created with the complement of the train set.
    :param test_size: Number of examples or a proportion of the dataset. Having it set to None means it uses the
    complement of the train set and the validation set. If both `validation_size` and `test_size` are None then
    a test set is not created.
    :param number_splits: Number of splits to generate.
    :param random_state: A seed for random number generation.
    :return: A generator of size `number_splits` with a tuple of up to three datasets corresponding to the splits.
    """
    assert dataset.targets is not None

    train_size, validation_size, test_size = get_sizes(dataset.size, train_size, validation_size, test_size)

    train_test_splitter = StratifiedShuffleSplit(
        n_splits=number_splits,
        train_size=train_size,
        test_size=validation_size + test_size,
        random_state=random_state,
    )

    fake_data = np.zeros_like(dataset.targets)

    for train_indices, validation_test_indices in train_test_splitter.split(fake_data, dataset.targets):
        train_dataset = dataset.subset(train_indices)

        if not validation_size and not test_size:
            yield train_dataset, None, None

        if not test_size:
            validation_dataset = dataset.subset(validation_test_indices)

            yield train_dataset, validation_dataset, None

        else:
            validation_test_splitter = StratifiedShuffleSplit(
                n_splits=1,
                train_size=validation_size,
                test_size=test_size,
                random_state=random_state,
            )

            validation_test_targets = dataset.targets[validation_test_indices]

            subset_validation_indices, subset_test_indices = next(validation_test_splitter.split(
                X=np.zeros_like(validation_test_targets),
                y=validation_test_targets,
            ))

            validation_indices = validation_test_indices[subset_validation_indices]
            test_indices = validation_test_indices[subset_test_indices]

            validation_dataset = dataset.subset(validation_indices)
            test_dataset = dataset.subset(test_indices)

            yield train_dataset, validation_dataset, test_dataset


def get_sizes(
        dataset_size: int,
        train_size: SizeType,
        validation_size: Optional[SizeType],
        test_size: Optional[SizeType]) -> Tuple[int, int, int]:

    if isinstance(train_size, float):
        train_size = math.floor(dataset_size * train_size)

    if isinstance(validation_size, float):
        validation_size = math.floor(dataset_size * validation_size)

    if isinstance(test_size, float):
        test_size = math.floor(dataset_size * test_size)

    if validation_size is None and test_size is None:
        validation_size, test_size = dataset_size - train_size, 0

    elif validation_size and test_size is None:
        test_size = dataset_size - (train_size + validation_size)

    elif validation_size is None and test_size:
        validation_size = dataset_size - (train_size + test_size)

    validation_size = validation_size if validation_size else 0
    test_size = test_size if test_size else 0

    return train_size, validation_size, test_size


def train_test_split(
        data: List[np.ndarray],
        data_size: int,
        percentage: float) -> Tuple[List[np.ndarray], List[np.ndarray]]:

    threshold = int(data_size * percentage)

    return [i[:threshold] for i in data], [i[threshold:] for i in data]
