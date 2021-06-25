# -*- mode:python; coding: utf-8 -*-
#
# Copyright (©) 2016-2021 EPFL (École Polytechnique Fédérale de Lausanne),
# Laboratory (LSMS - Laboratoire de Simulation en Mécanique des Solides)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Helper functions for dumpers
"""
from functools import wraps
from pathlib import Path
import numpy as np

from .. import model_type, type_traits, mpi

__all__ = ["step_dump", "directory_dump"]

_basic_types = [t for t, trait in type_traits.items() if trait.components == 1]


def _is_surface_field(field, model):
    bn = model.boundary_shape
    # Testing works for both local and global fields
    return list(field.shape[:len(bn)]) == bn \
        or list(field.shape[:len(bn)]) == mpi.global_shape(bn)


def local_slice(field, model):
    n = model.shape
    bn = model.boundary_shape

    gshape = mpi.global_shape(bn)
    offsets = np.zeros_like(gshape)
    offsets[0] = mpi.local_offset(gshape)

    if not _is_surface_field(field, model) and len(n) > len(bn):
        gshape = [n[0]] + gshape
        offsets = np.concatenate(([0], offsets))

    shape = bn if _is_surface_field(field, model) else n
    if len(field.shape) > len(shape):
        shape += field.shape[len(shape):]

    def sgen(pair):
        offset, size = pair
        return slice(offset, offset + size, None)

    def sgen_basic(pair):
        offset, size = pair
        return slice(offset, offset + size)

    slice_gen = sgen_basic if model_type in _basic_types else sgen
    return tuple(map(slice_gen, zip(offsets, shape)))


def step_dump(cls):
    """
    Decorator for dumper with counter for steps
    """
    orig_init = cls.__init__
    orig_dump = cls.dump

    @wraps(cls.__init__)
    def __init__(obj, *args, **kwargs):
        orig_init(obj, *args, **kwargs)
        obj.count = 0

    def postfix(obj):
        return "_{:04d}".format(obj.count)

    @wraps(cls.dump)
    def dump(obj, *args, **kwargs):
        orig_dump(obj, *args, **kwargs)
        obj.count += 1

    cls.__init__ = __init__
    cls.dump = dump
    cls.postfix = property(postfix)

    return cls


def directory_dump(directory=""):
    "Decorator for dumper in a directory"
    directory = Path(directory)

    def actual_decorator(cls):
        orig_dump = cls.dump
        orig_filepath = cls.file_path.fget

        @wraps(cls.dump)
        def dump(obj, *args, **kwargs):
            if mpi.rank() == 0:
                directory.mkdir(parents=True, exist_ok=True)

            orig_dump(obj, *args, **kwargs)

        @wraps(cls.file_path.fget)
        def file_path(obj):
            return str(directory / orig_filepath(obj))

        cls.dump = dump
        cls.file_path = property(file_path)

        return cls

    return actual_decorator


def hdf5toVTK(inpath, outname):
    "Convert HDF5 dump of a model to VTK"
    import h5py as h5  # noqa

    from .. import ModelFactory  # noqa
    from . import UVWDumper  # noqa

    type_translate = {
        'model_type.basic_1d': model_type.basic_1d,
        'model_type.basic_2d': model_type.basic_2d,
        'model_type.surface_1d': model_type.surface_1d,
        'model_type.surface_2d': model_type.surface_2d,
        'model_type.volume_1d': model_type.volume_1d,
        'model_type.volume_2d': model_type.volume_2d,
    }

    with h5.File(inpath, 'r') as h5file:
        model_t = h5file.attrs['model_type']
        system_size = list(h5file.attrs['system_size'])
        n = list(h5file.attrs['discretization'])

        model = ModelFactory.createModel(type_translate[model_t],
                                         system_size, n)

        fields = []
        for field in h5file:
            model.registerField(field, h5file[field][:])
            fields.append(field)

        uvw_dumper = UVWDumper(outname, *fields)
        uvw_dumper << model
