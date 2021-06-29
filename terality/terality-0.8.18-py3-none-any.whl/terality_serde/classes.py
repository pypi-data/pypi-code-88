from abc import ABC, abstractmethod
import base64
from datetime import datetime, time
from io import BytesIO
from pathlib import Path, PosixPath
from typing import Any

import numpy as np
import pandas as pd

# noinspection PyProtectedMember
from dateutil.parser import ParserError
from pandas._libs import missing, OutOfBoundsDatetime, tslibs
import pyarrow


class ExternalTypeSerializer(ABC):
    class_: type
    class_name: str

    @classmethod
    @abstractmethod
    def to_json(cls, value: Any) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_json(cls, **kwargs):
        pass


class TypeSerde(ExternalTypeSerializer):
    class_ = type
    class_name = "type"

    mapping = {
        "bool": bool,
        "int": int,
        "float": float,
        "str": str,
        "float32": np.float32,
        "AssertionError": AssertionError,
        "AttributeError": AttributeError,
        "IndexError": IndexError,
        "OutOfBoundsDatetime": OutOfBoundsDatetime,
        "ParserError": ParserError,
        "ValueError": ValueError,
        "TypeError": TypeError,
        "ZeroDivisionError": ZeroDivisionError,
    }

    @classmethod
    def to_json(cls, value: type) -> dict:
        return {"value": value.__name__}

    @classmethod
    def from_json(cls, value: str) -> type:  # type: ignore
        return cls.mapping[value]


class TupleSerde(ExternalTypeSerializer):
    class_ = tuple
    class_name = "tuple"

    @classmethod
    def to_json(cls, value: tuple) -> dict:
        return {"as_list": list(value)}

    @classmethod
    def from_json(cls, as_list: list) -> tuple:  # type: ignore
        return tuple(as_list)


class RangeSerde(ExternalTypeSerializer):
    class_ = range
    class_name = "range"

    @classmethod
    def to_json(cls, value: range) -> dict:
        return {"as_list": [value.start, value.stop, value.step]}

    @classmethod
    def from_json(cls, as_list: list) -> range:  # type: ignore
        return range(*as_list)


class SliceSerde(ExternalTypeSerializer):
    class_ = slice
    class_name = "slice"

    @classmethod
    def to_json(cls, value: slice) -> dict:
        return {"as_list": [value.start, value.stop, value.step]}

    @classmethod
    def from_json(cls, as_list: list) -> slice:  # type: ignore
        return slice(*as_list)


class TimeSerde(ExternalTypeSerializer):
    class_ = time
    class_name = "datetime.time"

    @classmethod
    def to_json(cls, value: time) -> dict:
        return {"isoformat": value.isoformat()}

    @classmethod
    def from_json(cls, isoformat: str) -> time:  # type: ignore
        return time.fromisoformat(isoformat)


class DateTimeSerde(ExternalTypeSerializer):
    class_ = datetime
    class_name = "datetime"

    @classmethod
    def to_json(cls, value: datetime) -> dict:
        return {"isoformat": value.isoformat()}

    @classmethod
    def from_json(cls, isoformat: str) -> datetime:  # type: ignore
        return datetime.fromisoformat(isoformat)


class TimeStampSerde(ExternalTypeSerializer):
    class_ = pd.Timestamp
    class_name = "timestamp"

    @classmethod
    def to_json(cls, value: pd.Timestamp) -> dict:
        return {"isoformat": value.isoformat()}

    @classmethod
    def from_json(cls, isoformat: str) -> datetime:  # type: ignore
        return pd.Timestamp.fromisoformat(isoformat)


class PathSerde(ExternalTypeSerializer):
    class_ = PosixPath
    class_name = "path"

    @classmethod
    def to_json(cls, value: Path) -> dict:
        return {"path_as_str": str(value)}

    @classmethod
    def from_json(cls, path_as_str: str) -> Path:  # type: ignore
        return Path(path_as_str)


class NumpyArray(ExternalTypeSerializer):
    class_ = np.ndarray
    class_name = "np.ndarray"

    @classmethod
    def to_json(cls, value: np.ndarray) -> dict:
        return {
            "buffer": base64.b64encode(value.tobytes()).decode("ascii"),
            "dtype": str(value.dtype),
        }

    @classmethod
    def from_json(cls, buffer: str, dtype: str) -> np.number:  # type: ignore
        return np.frombuffer(base64.b64decode(buffer.encode("ascii")), dtype=dtype)


class NumpyScalarSerde(ExternalTypeSerializer):
    @classmethod
    def to_json(cls, value: np.number) -> dict:
        return {"value": value.item(), "class_name": type(value).__name__}

    @classmethod
    def from_json(cls, value: str, class_name: str) -> np.number:  # type: ignore  # pylint: disable=unused-argument
        return cls.class_(value)


class NumpyBoolSerde(NumpyScalarSerde):
    class_ = np.bool_
    class_name = "np.bool_"


class NumpyU8Serde(NumpyScalarSerde):
    class_ = np.uint8
    class_name = "np.uint8"


class NumpyU16Serde(NumpyScalarSerde):
    class_ = np.uint16
    class_name = "np.uint16"


class NumpyU32Serde(NumpyScalarSerde):
    class_ = np.uint32
    class_name = "np.uint32"


class NumpyU64Serde(NumpyScalarSerde):
    class_ = np.uint64
    class_name = "np.uint64"


class NumpyI8Serde(NumpyScalarSerde):
    class_ = np.int8
    class_name = "np.int8"


class NumpyI16Serde(NumpyScalarSerde):
    class_ = np.int16
    class_name = "np.int16"


class NumpyI32Serde(NumpyScalarSerde):
    class_ = np.int32
    class_name = "np.int32"


class NumpyI64Serde(NumpyScalarSerde):
    class_ = np.int64
    class_name = "np.int64"


class NumpyF32Serde(ExternalTypeSerializer):
    class_ = np.float32
    class_name = "np.float32"

    @classmethod
    def to_json(cls, value: np.float32) -> dict:
        bytes_io = BytesIO()
        # noinspection PyTypeChecker
        np.save(bytes_io, value)
        o_bytes = bytes_io.getvalue()
        o_str = base64.b64encode(o_bytes).decode()
        return {"float_as_array": o_str}

    @classmethod
    def from_json(cls, float_as_array: str) -> np.float32:  # type: ignore
        bytes_io = BytesIO(base64.b64decode(float_as_array.encode()))
        # Numpy signature does  not list all variants
        # noinspection PyTypeChecker
        return np.load(bytes_io).flatten()[0]


class NumpyF64Serde(NumpyScalarSerde):
    class_ = np.float64
    class_name = "np.float64"


class PandasMissingSerde(ExternalTypeSerializer):
    value: Any

    @classmethod
    def to_json(cls, value: np.number) -> dict:
        return {}

    @classmethod
    def from_json(cls) -> np.number:  # type: ignore
        return cls.value


class PandasNASerde(PandasMissingSerde):
    class_ = missing.NAType  # pylint: disable=c-extension-no-member
    class_name = "pd.NA"
    value = pd.NA


class PandasNaTSerde(PandasMissingSerde):
    class_ = tslibs.NaTType
    class_name = "pd.NaT"
    value = pd.NaT


class PyarrowDataType(ExternalTypeSerializer):
    class_ = pyarrow.DataType
    class_name = "pyarrow_data_type"

    _mapping = {
        data_type.id: data_type
        for data_type in [
            pyarrow.null(),
            pyarrow.string(),
            pyarrow.date32(),
            pyarrow.date64(),
        ]
    }

    @classmethod
    def to_json(cls, value: pyarrow.DataType) -> dict:
        return {"value": value.id}

    @classmethod
    def from_json(cls, value: str) -> type:  # type: ignore
        return cls._mapping[value]


scalar_types = [
    DateTimeSerde,
    TimeStampSerde,
    TimeSerde,
    NumpyBoolSerde,
    NumpyU8Serde,
    NumpyU16Serde,
    NumpyU32Serde,
    NumpyU64Serde,
    NumpyI8Serde,
    NumpyI16Serde,
    NumpyI32Serde,
    NumpyI64Serde,
    NumpyF32Serde,
    NumpyF64Serde,
    NumpyArray,
    PandasNASerde,
    PandasNaTSerde,
]


_other_types = [
    TypeSerde,
    PyarrowDataType,
    TupleSerde,
    SliceSerde,
    RangeSerde,
    PathSerde,
]

all_external_types = scalar_types + _other_types
