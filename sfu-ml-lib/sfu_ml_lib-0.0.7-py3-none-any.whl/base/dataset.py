import typing
from abc import ABC, abstractmethod
from typing import Tuple, Optional, Iterator, Iterable, TypeVar, Union

import numpy as np
import tensorflow as tf
from tensorflow import Tensor, TensorSpec, RaggedTensorSpec, SparseTensorSpec


T = TypeVar('T')

TensorType = Union[np.ndarray, Tensor]
TensorTuple = Union[TensorType, Tuple[TensorType, ...]]
BatchType = Union[
    Tuple[TensorTuple, None],
    Tuple[TensorTuple, TensorTuple],
    Tuple[TensorTuple, TensorTuple, TensorType],
]

Specification = Union[SparseTensorSpec, RaggedTensorSpec, TensorSpec]
Schema = Union[Specification, Iterable['Schema']]  # type: ignore


class Dataset(ABC):
    input_schema: Schema
    size: int
    targets: Optional[TensorType] = None

    @abstractmethod
    @typing.no_type_check
    def get_batches(self, *args) -> tf.data.Dataset:
        ...

    @abstractmethod
    def subset(self: T, indices: TensorType) -> T:
        ...

    def create_tf_dataset(self, iterator: Iterator[BatchType], queue_size: int = -1) -> tf.data.Dataset:
        return tf.data.Dataset.from_generator(iterator, output_signature=self.input_schema).prefetch(queue_size)
