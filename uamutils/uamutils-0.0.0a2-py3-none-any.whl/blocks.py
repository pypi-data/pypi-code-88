import numpy as np
import xarray as xr

from .shared import DatasetID, BlockName, TimeMoment
from .config import param_attributes


class Sphere:
    def __init__(self, mod4, time_moment):
        self.id = DatasetID(BlockName.sphere, time_moment)

        self.time = mod4.timestamp(self.id)

        self.colatitudes = mod4.colatitudes(self.id.block_name)
        self.longitudes = mod4.longitudes()  
        # convert from cm to km
        self.altitudes = mod4.altitudes(self.id.block_name) / 1e5

        self.params = ["N(O2)", "N(N2)", "N(O)", "N(NO)", "N(N)", "N(XY+)",
                       "Tn", "Ti", "Te", "Vr", "Vt", "Vd",
                       "q(O2+)", "q(N2+)", "q(NO+)", "q(O+)"]
        
        data_1d = mod4.dataset(self.id)
        dims = (self.params, self.altitudes, self.colatitudes, self.longitudes)
        shape = tuple(len(dim) for dim in dims)
        self.data = data_1d.reshape(shape, order='F')

    def __str__(self):
        return '<br/>'.join([f'{key}:: {value}' for key, value in self.__dict__.items()])

    def as_xarray(self):
        coords = {'altkm': self.altitudes, 'colat': self.colatitudes, 'lon': self.longitudes}
        arrays = {param: xr.DataArray(self.data[i], name=param, dims=('altkm', 'colat', 'lon'), coords=coords) 
                  for i, param in enumerate(self.params)}

        for param in self.params:
            arrays[param].attrs['long_name'] = param_attributes[param]['long_name']
            arrays[param].attrs['units'] = param_attributes[param]['units']

        # arrays['N(N2)'].attrs['long_name'] = 'N2 number density' 
        # arrays['N(N2)'].attrs['units'] = 'cm-3'
        # arrays['N(N2)'].attrs['description'] = 'optional description'

        # TODO? decide on units format
        attrs = {'altitude_units': 'km', 'reference_frame': 'geomag', 
                 'longitude_units': 'mag. deg.', 'colatitude_units': 'mag. deg.',
                 'time_started': self.time.started,
                 'time_finished': self.time.finished}
        # attrs = {'units': 'altitude - km; longitude - mag. deg.; colatitude - mag. deg.'}
        
        return xr.Dataset(arrays, attrs=attrs)


class Potential:
    def __init__(self, mod4, time_moment):
        self.id = DatasetID(BlockName.potential, time_moment)

        self.time = mod4.timestamp(self.id)

        self.colatitudes = mod4.colatitudes(self.id.block_name)
        self.longitudes = mod4.longitudes()  

        self.params = ['pot']

        # TODO: check the order of colat/lon
        data_1d = mod4.dataset(self.id)
        shape = tuple(len(dim) for dim in [self.longitudes, self.colatitudes])
        self.data = data_1d.reshape(shape, order='F')

    def as_xarray(self):
        coords = {'colat': self.colatitudes, 'lon': self.longitudes}
        
        array = {"pot": xr.DataArray(self.data, name="pot", dims=('lon', 'colat'), coords=coords)}


        for param in self.params:
            array[param].attrs['long_name'] = param_attributes[param]['long_name']
            array[param].attrs['units'] = param_attributes[param]['units']

        # array['pot'].attrs['long_name'] = 'N2 number density' 
        # array['pot'].attrs['units'] = '? (СГС или СИ?)'

        attrs = {'reference_frame': 'geomag', 
                 'longitude_units': 'mag. deg.', 'colatitude_units': 'mag. deg.',
                 'time_started': self.time.started,
                 'time_finished': self.time.finished}

        return xr.Dataset(array, attrs=attrs)


class Tube:
    def __init__(self, mod4, time_moment):
        block_name = BlockName.tube
        self.id = DatasetID(block_name, time_moment)

        self.time = mod4.timestamp(self.id)

        self.longitudes = mod4.longitudes()

        nodes, nodes_raw = mod4.tube_nodes()
        self.nodes = nodes
        self.nodes_raw = nodes_raw

        self.tubes_count = mod4.info.tubes_count
        # how nodes are split by tubes
        self.nodes_split = mod4.info.tube_nodes_split

        self.params = ['N(O+)', 'N(H+)', '*N(He+)', 'Vq(O+)', 'Vq(H+)', '*Vq(He+)', 'Ti', 'Te']

        # iterate over all in 1d data and add meta-info (coords, tube index, point idx, etc.)
        # so that you can easily find closest point -> get tube -> get closest point in this tube

        data_1d = mod4.dataset(self.id)
        shape = (len(self.params), len(self.nodes), len(self.longitudes))
        data_iter = iter(data_1d)
        self.data = np.array(data_1d).reshape(shape, order='F')

        # arr = []
        # # FIXME: this is purely for testing purposes, we can extract it into a test later on        
        # for long_idx in range(len(self.longitudes)):
        #     for tube_idx in range(self.tubes_count):
        #         node_start = sum(self.nodes_split[:tube_idx])
        #         for point_idx in range(self.nodes_split[tube_idx]):
        #             node_idx = node_start + point_idx
        #             alt, colat = self.nodes_raw[node_idx]   
        #             for param_idx in range(len(self.params)):
        #                 arr.append({'lon': self.longitudes[long_idx], 
        #                 'tube': tube_idx, 
        #                 'node': (alt, colat, node_idx), 'node_local': point_idx, 
        #                 'param': self.params[param_idx], 'val': next(data_iter)})
        # self.data_labeled = arr


class TubeInterped:
    '''Tube data interped to spherical coordinates grid'''
    def __init__(self, mod4, time_moment):
        block_name = BlockName.tube_to_sphere
        self.id = DatasetID(block_name, time_moment)

        self.time = mod4.timestamp(self.id)

        self.colatitudes = mod4.colatitudes(self.id.block_name)
        self.longitudes = mod4.longitudes()  
        # convert from cm to km
        self.altitudes = mod4.altitudes(self.id.block_name) / 1e5

        self.params = ['N(O+)', 'Vr(O+)', 'Vt(O+)', 'Vd(O+)', 'Te']

        data_1d = mod4.dataset(self.id)
        dims = (self.params, self.altitudes, self.colatitudes, self.longitudes)
        shape = tuple(len(dim) for dim in dims)
        self.data = data_1d.reshape(shape, order='F')

    def as_xarray(self):
        coords = {'altkm': self.altitudes, 'colat': self.colatitudes, 'lon': self.longitudes}
        arrays = {param: xr.DataArray(self.data[i], name=param, dims=('altkm', 'colat', 'lon'), coords=coords) 
                  for i, param in enumerate(self.params)}


        attrs = {'altitude_units': 'km', 'reference_frame': 'geomag', 
                 'longitude_units': 'mag. deg.', 'colatitude_units': 'mag. deg.',
                 'time_started': self.time.started,
                 'time_finished': self.time.finished}
        # attrs = {'units': 'altitude - km; longitude - mag. deg.; colatitude - mag. deg.'}
        

        for param in self.params:
            arrays[param].attrs['long_name'] = param_attributes[param]['long_name']
            arrays[param].attrs['units'] = param_attributes[param]['units']

        # arrays['N(O+)'].attrs['long_name'] = '?' 
        # arrays['N(O+)'].attrs['units'] = '?'

        return xr.Dataset(arrays, attrs=attrs)


