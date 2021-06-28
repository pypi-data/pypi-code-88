import math
from typing import Tuple, Generator

import numba
import numpy as np


@numba.njit
def compute_target_rates(targets: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Computes the counts and rates of a target vector.

    >>> compute_target_rates(np.array([0, 0, 0, 0, 1]))
    (array([1., 4.], dtype=float32), array([4, 1], dtype=int32))

    :param targets: A Numpy vector of target indices.
    :return: A tuple with rates and counts.
    """
    num_classes = np.max(targets) + 1

    counts = np.zeros(num_classes, dtype=np.int32)
    for target in targets:
        counts[target] += 1

    rates = (np.max(counts) / counts).astype(np.float32)

    return rates, counts


@numba.njit
def get_oversampled_indices(targets: np.ndarray) -> np.ndarray:
    rates, counts = compute_target_rates(targets)

    quotients = np.array([math.floor(value) for value in rates], dtype=np.int32)
    remainders = [round(value) for value in (rates - quotients) * counts]

    indexed_targets = np.array(list(enumerate(targets)), dtype=targets.dtype)
    np.random.shuffle(indexed_targets)

    indices = []

    for index, target in indexed_targets:
        for _ in range(quotients[target]):
            indices.append(index)

        if remainders[target] > 0:
            indices.append(index)
            remainders[target] -= 1

    indices = np.array(indices, np.int32)

    return indices


@numba.njit
def get_undersampled_indices(targets: np.ndarray, batch_size: int) -> Generator[np.ndarray, None, None]:
    num_classes = np.max(targets) + 1

    class_indices = [
        numba.typed.List.empty_list(numba.types.int64)
        for _ in range(num_classes)
    ]

    for index, target in enumerate(targets):
        class_indices[target].append(index)

    while True:
        class_size = min(math.floor(batch_size / num_classes), min([len(indices) for indices in class_indices]))

        if class_size == 0:
            break

        batch_indices = []

        for _ in range(class_size):
            for indices in class_indices:
                batch_indices.append(indices.pop())

        yield np.array(batch_indices, dtype=np.int32)


def get_oversampled_indices_subset(indices: np.ndarray, targets: np.ndarray, balance: bool = True) -> np.ndarray:
    if not balance:
        return indices

    oversampled_indices = get_oversampled_indices(targets[indices])
    indices = indices[oversampled_indices]

    return indices


def get_undersampled_indices_subset(
        indices: np.ndarray,
        targets: np.ndarray,
        batch_size: int,
        balance: bool) -> np.ndarray:

    if balance:
        for batch_indices in get_undersampled_indices(targets[indices], batch_size):
            yield indices[batch_indices]

    else:
        for start_index in range(0, indices.size, batch_size):
            yield indices[start_index:start_index + batch_size]
