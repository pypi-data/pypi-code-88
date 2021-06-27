import typing
from abc import ABC, abstractmethod
from typing import Tuple, Optional, Iterable, TypeVar, Union

import numpy as np
import tensorflow as tf
from tensorflow import Tensor, TensorSpec, RaggedTensorSpec, SparseTensorSpec


T = TypeVar('T')

TensorType = Union[np.ndarray, Tensor]
TensorTuple = Union[TensorType, Tuple[TensorType, ...]]
BatchType = Union[
    Tuple[TensorTuple],
    Tuple[TensorTuple, TensorTuple],
    Tuple[TensorTuple, TensorTuple, TensorType],
]

SpecificationType = Union[SparseTensorSpec, RaggedTensorSpec, TensorSpec]
SpecificationTuple = Union[SpecificationType, Tuple[SpecificationType, ...]]
SchemaType = Union[
    Tuple[SpecificationTuple],
    Tuple[SpecificationTuple, SpecificationTuple],
    Tuple[SpecificationTuple, SpecificationTuple, SpecificationTuple],
]


class Dataset(ABC):
    size: int
    targets: Optional[TensorType] = None
    schema: Optional[SchemaType] = None

    @abstractmethod
    @typing.no_type_check
    def get_batches(self, *args) -> tf.data.Dataset:
        ...

    @abstractmethod
    def subset(self: T, indices: TensorType) -> T:
        ...

    def create_tf_dataset(self, iterator: Iterable[BatchType], queue_size: int = -1) -> tf.data.Dataset:
        assert self.schema

        dataset = tf.data.Dataset.from_generator(iterator, output_signature=self.schema).prefetch(queue_size)

        return dataset
