from __future__ import annotations

import abc
from typing import Any, Union

import h5py
import numpy as np

__all__ = [
    'AbstractLoader',
    'CellLoader',
    'CharLoader',
    'LogicalLoader',
    'NumericLoader',
    'StructLoader',
]


def row_major_index(index):
    if isinstance(index, tuple):
        return index[::-1]
    else:
        return index


H5Object = Union[h5py.Dataset, h5py.Group]


class AbstractLoader(abc.ABC):
    def __init__(self, h5object: H5Object, parent):
        self.h5object = h5object
        self.parent = parent

    #=============================================
    # Representation and metadata
    #=============================================
    def __repr__(self) -> str:
        return f'<MATLAB {self.matlab_class} "{self.name}": shape {self.shape}>'

    @property
    def matlab_class(self):
        return self.h5object.attrs['MATLAB_class'].decode()

    @property
    def name(self):
        return self.h5object.name.split('/')[-1]

    @property
    @abc.abstractmethod
    def shape(self):
        ...

    def is_empty(self):
        return 'MATLAB_empty' in self.h5object.attrs

    #=============================================
    # Loading interface
    #=============================================
    def __getitem__(self, index):
        return self.load(index)

    @abc.abstractmethod
    def load(self, index) -> Any:
        """Load the specified item from disk."""
        ...


class StructLoader(AbstractLoader):
    """Loader for MATLAB type `struct`. Returns arrays of dict."""
    h5object: h5py.Group

    @property
    def shape(self):
        if self._is_struct_array():
            return self._get_struct_array_shape()
        else:
            return (1, 1)

    def _get_struct_array_shape(self):
        pointers = dict(self.h5object)
        _, refarray = pointers.popitem()
        return refarray.shape[::-1]

    def load(self, index) -> np.ndarray:
        if self._is_struct_array():
            s = self._load_array(index)
        else:
            s = self._load_scalar(index)
        return self.parent._process(s)

    def _load_scalar(self, index):
        d = {
            fieldname: self.parent.get_loader(item)[()]
            for fieldname, item in self.h5object.items()
        }
        return np.array([[d]], dtype='O')[index]

    def _load_array(self, index):
        c_index = row_major_index(index)

        # Get an item from the struct to figure out how big it is, then stick it
        # back in the dict. I have no idea if there's a cleaner way, I just need
        # to inspect a single item *before* looping!
        pointers = dict(self.h5object)
        fieldname, refarray = pointers.popitem()
        pointers[fieldname] = refarray

        # Figure out how much we're pulling out by indexing the sample refarray
        sample_refs = refarray[c_index]

        if isinstance(sample_refs, h5py.Reference):
            # Indexing pulled out a single item from the array, just return a
            # dict
            return {
                fieldname: self.parent.get_loader(refarray[c_index])[()]
                for fieldname, refarray in pointers.items()
            }

        # Initialize array of dict
        a = np.empty(sample_refs.shape, dtype='O')
        for i, _ in enumerate(a.flat):
            a[i] = dict()

        for fieldname, refarray in pointers.items():
            for i, ref in enumerate(refarray[c_index].flat):
                a.flat[i][fieldname] = self.parent.get_loader(ref)[()]

        return a

    def _is_struct_array(self):
        """Determine whether the given MATLAB struct is scalar or not."""
        for field in self.h5object.values():
            # MATLAB represents scalar structs and struct arrays differently
            # within HDF5. Scalar structs are ordinary groups with named
            # datasets and/or subgroups. Struct arrays, however, are represented
            # by a group with arrays of references. The arrays all have the same
            # size (that of the struct array itself), and are grouped by field
            # name.
            #
            # If the fields in the struct are *not* assigned a MATLAB_class,
            # then they're not actual objects. This is what differentiates a
            # struct array from a cell array -- the cell array is assigned a
            # MATLAB_class, and the fields of a struct array are not.
            try:
                matlab_class = field.attrs['MATLAB_class']
            except KeyError:
                isarray = True
                break
        else:
            # Executes if break doesn't fire
            isarray = False

        return isarray


class DatasetLoader(AbstractLoader):
    h5object: h5py.Dataset

    @property
    def shape(self):
        if self.is_empty():
            return ()
        else:
            return self.h5object.shape[::-1]


class CellLoader(DatasetLoader):
    """Loader for the MATLAB type `cell`. Returns arrays with dtype 'object'."""
    def load(self, index) -> np.ndarray:
        cellrefs = self.h5object[row_major_index(index)]
        if isinstance(cellrefs, h5py.Reference):
            # Indexed a single item, completely extracting it from the array
            return self.parent.get_loader(cellrefs)[()]

        a = np.empty(cellrefs.shape, dtype='O')
        for i, ref in enumerate(cellrefs.flat):
            a.flat[i] = self.parent.get_loader(ref)[()]
        return self.parent._process(a)


class NumericLoader(DatasetLoader):
    """Loader for MATLAB numeric types."""
    def load(self, index) -> np.ndarray:
        if 'MATLAB_empty' in self.h5object.attrs:
            return np.array([], dtype=self.h5object.dtype)
        return self.parent._process(self.h5object[row_major_index(index)])


class LogicalLoader(NumericLoader):
    """Loader for MATLAB type `logical`."""
    def load(self, index) -> np.ndarray:
        return super().load(index).astype('bool8')


class CharLoader(DatasetLoader):
    """Loader for the MATLAB type `char`. Returns str.

    Multi-dimensional `char` arrays are flattened to 1-D and returned as str.
    """
    def load(self, index) -> str:
        if self.is_empty():
            return ''
        c_index = row_major_index(index)
        return self.h5object[c_index].tobytes('F').decode('utf-16')
