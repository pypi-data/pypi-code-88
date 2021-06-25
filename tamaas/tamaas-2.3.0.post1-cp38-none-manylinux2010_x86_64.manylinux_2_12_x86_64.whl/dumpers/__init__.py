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
Dumpers for the class tamaas.Model
"""
from pathlib import Path
from os import PathLike
import json
import io
import typing as ts
from collections.abc import Collection

import numpy as np

from .. import ModelDumper, model_type, mpi, type_traits, ModelFactory, Model
from ._helper import (
    step_dump, directory_dump, local_slice, _is_surface_field, _basic_types,
)

FileType = ts.Union[str, PathLike, io.TextIOBase]
NameType = ts.Union[str, PathLike]

_reverse_trait_map = {
    'model_type.' + t.__name__: mtype for mtype, t in type_traits.items()
}


def _get_attributes(model: Model):
    "Get model attributes"
    return {
        'model_type': str(model.type),
        'system_size': model.system_size,
        'discretization': model.global_shape,
    }


def _create_model(attrs: ts.MutableMapping):
    "Create a model from attribute dictionaty"
    mtype = _reverse_trait_map[attrs['model_type']]

    # netcdf4 converts 1-lists attributes to numbers
    for attr in ['system_size', 'discretization']:
        if not isinstance(attrs[attr], Collection):
            attrs[attr] = [attrs[attr]]
    return ModelFactory.createModel(mtype,
                                    attrs['system_size'],
                                    attrs['discretization'])


class MPIIncompatibilityError(RuntimeError):
    "Raised when code is not meant to be executed in MPI environment"


class ModelError(ValueError):
    "Raised when unexpected model is passed to a dumper with a state"


class ComponentsError(ValueError):
    "Raised when an unexpected number of components is encountred"


class ModelJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Model):
            model = obj
            attrs = _get_attributes(model)
            model_dict = {
                'attrs': attrs,
                'fields': {},
                'operators': [],
            }

            for field in model:
                model_dict['fields'][field] = model[field].tolist()

            for op in model.operators:
                model_dict['operators'].append(op)

            return model_dict

        return json.JSONEncoder.default(self, obj)


class JSONDumper(ModelDumper):
    def __init__(self, file_descriptor: FileType):
        super(JSONDumper, self).__init__()
        self.fd = file_descriptor

    def dump_to_file(self, fd, model: Model):
        json.dump(model, fd, cls=ModelJSONEncoder)

    def dump(self, model: Model):
        if isinstance(self.fd, (str, PathLike)):
            with open(self.fd, 'w') as fd:
                self.dump_to_file(fd, model)
        elif isinstance(self.fd, io.TextIOBase):
            self.dump_to_file(self.fd, model)
        else:
            raise TypeError(
                f"Expected a path or file descriptor, got {self.fd}")

    def read_from_file(self, fd: io.TextIOBase):
        properties = json.load(fd)
        model = _create_model(properties['attrs'])

        for name, field in properties['fields'].items():
            v = np.asarray(field)
            if model.type in _basic_types:
                v = v.reshape(list(v.shape) + [1])
            model[name] = v
        return model

    def read(self, file_descriptor: FileType):
        fd = file_descriptor
        if isinstance(fd, (str, PathLike)):
            with open(fd, 'r') as fd:
                return self.read_from_file(fd)
        if isinstance(fd, io.TextIOBase):
            return self.read_from_file(fd)
        raise TypeError(f"Expected a path or file descriptor, got {type(fd)}")


class FieldDumper(ModelDumper):
    """Abstract dumper for python classes using fields"""
    postfix = ''
    extension = ''
    name_format = "{basename}{postfix}.{extension}"

    def __init__(self, basename: NameType, *fields, **kwargs):
        """Construct with desired fields"""
        super(FieldDumper, self).__init__()
        self.basename = basename
        self.fields: ts.List[str] = list(fields)
        self.all_fields: bool = kwargs.get('all_fields', False)

    def add_field(self, field: str):
        """Add another field to the dump"""
        if field not in self.fields:
            self.fields.append(field)

    def dump_to_file(self, file_descriptor: FileType, model: Model):
        """Dump to a file (name or handle)"""
        raise NotImplementedError()

    def get_fields(self, model: Model):
        """Get the desired fields"""
        if not self.all_fields:
            requested_fields = self.fields
        else:
            requested_fields = list(model)

        return {field: model[field] for field in requested_fields}

    def dump(self, model: Model):
        "Dump model"
        self.dump_to_file(self.file_path, model)

    def read(self, file_descriptor: FileType):
        raise NotImplementedError(
            f'read() method not implemented in {type(self).__name__}')

    @property
    def file_path(self):
        """Get the default filename"""
        return self.name_format.format(basename=self.basename,
                                       postfix=self.postfix,
                                       extension=self.extension)


@directory_dump('numpys')
@step_dump
class NumpyDumper(FieldDumper):
    """Dumper to compressed numpy files"""
    extension = 'npz'

    def dump_to_file(self, file_descriptor: FileType, model: Model):
        """Saving to compressed multi-field Numpy format"""
        if mpi.size() > 1:
            raise MPIIncompatibilityError("NumpyDumper does not function "
                                          "at all in parallel")

        np.savez_compressed(file_descriptor, attrs=_get_attributes(model),
                            **self.get_fields(model))

    def read(self, file_descriptor: FileType):
        "Create model from Numpy file"
        data = np.load(file_descriptor, mmap_mode='r')
        model = _create_model(data['attrs'].item())

        for k, v in filter(lambda k: k[0] != 'attrs', data.items()):
            if model.type in _basic_types:
                v = v.reshape(list(v.shape) + [1])
            model[k] = v
        return model


try:
    import h5py

    @directory_dump('hdf5')
    @step_dump
    class H5Dumper(FieldDumper):
        """Dumper to HDF5 file format"""
        extension = 'h5'

        def _hdf5_args(self):
            if mpi.size() > 1:
                from mpi4py import MPI  # noqa
                mpi_args = dict(driver='mpio', comm=MPI.COMM_WORLD)
                comp_args = {}  # compression does not work in parallel
            else:
                mpi_args = {}
                comp_args = dict(compression='gzip', compression_opts=7)
            return mpi_args, comp_args

        def dump_to_file(self, file_descriptor: FileType, model: Model):
            """Saving to HDF5 with metadata about the model"""

            # Setup for MPI
            if not h5py.get_config().mpi and mpi.size() > 1:
                raise MPIIncompatibilityError("HDF5 does not have MPI support")

            mpi_args, comp_args = self._hdf5_args()

            with h5py.File(file_descriptor, 'w', **mpi_args) as handle:
                # Writing data
                for name, field in self.get_fields(model).items():
                    shape = list(field.shape)

                    if mpi.size() > 1:
                        xdim = 0 if _is_surface_field(field, model) else 1
                        shape[xdim] = mpi_args['comm'].allreduce(shape[xdim])

                    dset = handle.create_dataset(name, shape, field.dtype,
                                                 **comp_args)

                    dset[local_slice(field, model)] = field

                # Writing metadata
                for name, attr in _get_attributes(model).items():
                    handle.attrs[name] = attr

        def read(self, file_descriptor: FileType):
            "Create model from HDF5 file"
            mpi_args, _ = self._hdf5_args()

            with h5py.File(file_descriptor, 'r', **mpi_args) as handle:
                model = _create_model(handle.attrs)
                for k, v in handle.items():
                    if model.type in _basic_types:
                        v = np.asarray(v).reshape(list(v.shape) + [1])
                    model[k] = v[local_slice(v, model)]
                return model
except ImportError:
    pass

try:
    import uvw  # noqa

    @directory_dump('paraview')
    @step_dump
    class UVWDumper(FieldDumper):
        """Dumper to VTK files for elasto-plastic calculations"""
        extension = 'vtr'
        forbidden_fields = ['traction', 'gap']

        def dump_to_file(self, file_descriptor: FileType, model: Model):
            """Dump displacements, plastic deformations and stresses"""
            if mpi.size() > 1:
                raise MPIIncompatibilityError("UVWDumper does not function "
                                              "properly in parallel")

            bdim = len(model.boundary_shape)

            # Local MPI size
            lsize = model.shape
            gsize = mpi.global_shape(model.boundary_shape)
            gshape = gsize

            if len(lsize) > bdim:
                gshape = [model.shape[0]] + gshape

            # Space coordinates
            coordinates = [np.linspace(0, L, N, endpoint=False)
                           for L, N in zip(model.system_size, gshape)]

            # If model has subsurfce domain, z-coordinate is always first
            dimension_indices = np.arange(bdim)
            if len(lsize) > bdim:
                dimension_indices += 1
                dimension_indices = np.concatenate((dimension_indices, [0]))
                coordinates[0] = \
                    np.linspace(0, model.system_size[0], gshape[0])

            offset = np.zeros_like(dimension_indices)
            offset[0] = mpi.local_offset(gsize)

            rectgrid = uvw.RectilinearGrid if mpi.size() == 1 \
                else uvw.parallel.PRectilinearGrid

            # Creating rectilinear grid with correct order for components
            coordlist = [coordinates[i][o:o+lsize[i]]
                         for i, o in zip(dimension_indices, offset)]

            grid = rectgrid(
                file_descriptor, coordlist,
                compression=True,
                offsets=offset,
            )

            # Iterator over fields we want to dump
            fields_it = filter(lambda t: t[0] not in self.forbidden_fields,
                               self.get_fields(model).items())

            # We make fields periodic for visualization
            for name, field in fields_it:
                array = uvw.DataArray(field, dimension_indices, name)
                grid.addPointData(array)

            grid.write()

    @directory_dump('paraview')
    class UVWGroupDumper(FieldDumper):
        "Dumper to ParaViewData files"
        extension = 'pvd'

        def __init__(self, basename: NameType, *fields, **kwargs):
            """Construct with desired fields"""
            super(UVWGroupDumper, self).__init__(basename, *fields, **kwargs)

            subdir = Path('paraview') / f'{basename}-VTR'
            subdir.mkdir(parents=True, exist_ok=True)

            self.uvw_dumper = UVWDumper(
                Path(f'{basename}-VTR') / basename, *fields, **kwargs
            )

            self.group = uvw.ParaViewData(self.file_path, compression=True)

        def dump_to_file(self, file_descriptor, model):
            self.group.addFile(
                self.uvw_dumper.file_path.replace('paraview/', ''),
                timestep=self.uvw_dumper.count
            )
            self.group.write()
            self.uvw_dumper.dump(model)
except ImportError:
    pass


try:
    from netCDF4 import Dataset

    @directory_dump('netcdf')
    class NetCDFDumper(FieldDumper):
        """Dumper to netCDF4 files"""

        extension = "nc"
        boundary_fields = ['traction', 'gap']

        def _file_setup(self, grp, model: Model):
            grp.createDimension('frame', None)

            # Attibutes
            for k, v in _get_attributes(model).items():
                grp.setncattr(k, v)

            # Local dimensions
            voigt_dim = type_traits[model.type].voigt
            components = type_traits[model.type].components
            self._vec = grp.createDimension('spatial', components)
            self._tens = grp.createDimension('Voigt', voigt_dim)
            self.model_info = model.global_shape, model.type
            global_boundary_shape = mpi.global_shape(model.boundary_shape)

            # Create boundary dimensions
            for label, size, length in zip(
                    "xy",
                    global_boundary_shape,
                    model.boundary_system_size
            ):
                grp.createDimension(label, size)
                coord = grp.createVariable(label, 'f8', (label,))
                coord[:] = np.linspace(0, length, size, endpoint=False)

            self._create_variables(
                grp, model,
                lambda f: _is_surface_field(f[1], model),
                global_boundary_shape, "xy"
            )

            # Create volume dimension
            if model.type in {model_type.volume_1d, model_type.volume_2d}:
                size = model.shape[0]
                grp.createDimension("z", size)
                coord = grp.createVariable("z", 'f8', ("z",))
                coord[:] = np.linspace(0, model.system_size[0], size)

                self._create_variables(
                    grp, model,
                    lambda f: not _is_surface_field(f[1], model),
                    model.global_shape, "zxy"
                )

            self.has_setup = True

        def dump_to_file(self, file_descriptor: NameType, model: Model):
            if mpi.size() > 1:
                raise MPIIncompatibilityError("NetCDFDumper does not function "
                                              "properly in parallel")

            mode = 'a' if Path(file_descriptor).is_file() \
                and getattr(self, 'has_setup', False) else 'w'

            with Dataset(file_descriptor, mode,
                         format='NETCDF4_CLASSIC',
                         parallel=mpi.size() > 1) as rootgrp:
                if rootgrp.dimensions == {}:
                    self._file_setup(rootgrp, model)

                if self.model_info != (model.global_shape, model.type):
                    raise ModelError(f"Unexpected model {mode}")

                self._dump_generic(rootgrp, model)

        def _create_variables(self, grp, model, predicate,
                              shape, dimensions):
            field_dim = len(shape)
            fields = list(filter(predicate, self.get_fields(model).items()))
            dim_labels = list(dimensions[:field_dim])

            for label, data in fields:
                local_dim = []

                # If we have an extra component
                if data.ndim > field_dim:
                    if data.shape[-1] == self._tens.size:
                        local_dim = [self._tens.name]
                    elif data.shape[-1] == self._vec.size:
                        local_dim = [self._vec.name]
                    else:
                        raise ComponentsError(
                            f"{label} has unexpected number of components "
                            f"({data.shape[-1]})")

                grp.createVariable(label, 'f8',
                                   ['frame'] + dim_labels + local_dim,
                                   zlib=True)

        def _dump_generic(self, grp, model):
            fields = self.get_fields(model).items()

            new_frame = grp.dimensions['frame'].size
            for label, data in fields:
                var = grp[label]
                slice_in_global = (new_frame,) + local_slice(data, model)
                var[slice_in_global] = np.array(data, dtype=np.double)

        def read(self, file_descriptor: NameType):
            "Create model with last frame"
            with Dataset(file_descriptor, 'r',
                         format='NETCDF4_CLASSIC') as rootgrp:
                attrs = {k: rootgrp.getncattr(k) for k in rootgrp.ncattrs()}
                model = _create_model(attrs)
                dims = rootgrp.dimensions.keys()
                for k, v in filter(lambda k: k[0] not in dims,
                                   rootgrp.variables.items()):
                    v = v[-1, :]
                    if model.type in _basic_types:
                        v = np.asarray(v).reshape(list(v.shape) + [1])
                    model[k] = v
                return model


except ImportError:
    pass
