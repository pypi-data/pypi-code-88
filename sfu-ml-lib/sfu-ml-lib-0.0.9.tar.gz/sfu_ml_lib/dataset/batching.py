import random
from typing import List, Generator

import numpy as np


def get_batches(
        data: List[np.ndarray],
        batch_size: int,
        pad_batch: bool = False) -> Generator[List[np.ndarray], None, None]:
    """
    Get a batch iterator.
    :param data: List of data you like to create batches from. The first dimension
    of the array represents number of data points.
    :param batch_size: The size of each batch.
    :param pad_batch: True if all batches need to be the same size
    """
    data_size = len(data)

    if pad_batch:
        delta = data_size - batch_size * int(data_size / batch_size)
        data.extend(random.sample(data, delta))

    for start_index in range(0, data_size, batch_size):
        yield data[start_index:start_index + batch_size]
