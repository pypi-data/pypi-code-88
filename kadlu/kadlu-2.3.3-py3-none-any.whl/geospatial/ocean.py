""" The ocean module provides an interface to fetching, loading 
    and interpolating ocean variables.
"""
import os
import logging
from datetime import timedelta
#from multiprocessing import Process, Queue
from queue import Queue

import numpy as np
from scipy.interpolate import NearestNDInterpolator

import kadlu
from kadlu import index
from kadlu.geospatial.interpolation             import (
        Interpolator2D,
        Interpolator3D,
        Uniform2D,
        Uniform3D,
    )
from kadlu.geospatial.data_sources.data_util    import (
        dt_2_epoch,
        fmt_coords,
        reshape_2D,
        reshape_3D,
        storage_cfg,
        verbosity,
    )
from kadlu.geospatial.data_sources.source_map   import (
        default_val,
        load_map,
        precip_type_map,
        var3d,
    )
from kadlu.geospatial.data_sources.hycom        import Hycom
from kadlu.geospatial.data_sources.era5         import Era5
from kadlu.geospatial.data_sources.wwiii        import Wwiii
from kadlu.utils import center_point


def worker(interpfcn, reshapefcn, cols, var, q):
    """ compute interpolation in parallel worker process

        interpfcn:
            callback function for interpolation
        reshapefcn:
            callback function for reshaping row data into matrix format
            for interpolation
        cols:
            data as returned from load function
        var:
            variable type. used as key in Ocean().interps dictionary
        q:
            shared queue object to pass interpolation back to parent
    """
    if verbosity() and isinstance(cols[0], (int, float)): logging.info(f'OCEAN {var.upper()}{"".join([" " for _ in range(11-len(var))])} loaded uniform value of {cols[0]} for interpolation')
    elif verbosity(): logging.info(f'OCEAN {var.upper()}{ "".join([" " for _ in range(11-len(var)) ]) } loaded {len(cols[0])} points for interpolation')
    obj = interpfcn(**reshapefcn(cols))
    q.put((var, obj))
    return


class Ocean():
    """ class for handling ocean data requests 

        data will be loaded using the given data sources and boundaries
        from arguments. an interpolation for each variable will be computed in 
        parallel

        data will be averaged over time frames for interpolation. for finer
        temporal resolution, define smaller time boundaries

        any of the below load_args may also accept a callback function instead
        of a string or array value if you wish to write your own data loading
        function. the boundary arguments supplied here will be passed to the 
        callable, i.e. north, south, west, east, top, bottom, start, end

        callables or array arguments must be ordered by [val, lat, lon] for 2D 
        data, or [val, lat, lon, depth] for 3D data

        args:
            north, south:
                latitude boundaries (float)
            west, east:
                longitude boundaries (float)
            top, bottom:
                depth range in metres (float)
                only applies to salinity and temperature
            start, end:
                time range for data load query (datetime)
                if multiple times exist within range, they will be averaged
                before computing interpolation
            **loadvars:
                keyword args supplied as 'load_{v}' where v is either a integer,
                float, array of [val, lat, lon[, time[, depth]]], or a data source
                string as described by the source_map

        attrs:
            interps: dict
                Dictionary of data interpolators
            origin: tuple(float, float)
                Latitude and longitude coordinates of the centre point of the 
                geographic bounding box. This point serves as the origin of the 
                planar x-y coordinate system.
            boundaries: dict
                Bounding box for the ocean volume in space and time
    """

    def __init__(self, *, 
            south=kadlu.defaults['south'],   west=kadlu.defaults['west'], 
            north=kadlu.defaults['north'],   east=kadlu.defaults['east'], 
            bottom=kadlu.defaults['bottom'], top=kadlu.defaults['top'],      
            start=kadlu.defaults['start'],   end=kadlu.defaults['end'], 
            **loadvars,
            ):

        logging.debug(f'''south = {south}, north = {north}, west = {west}, east = {east}, top = {top}, bottom = {bottom}''')

        # legacy support
        if 'load_bathy' in loadvars.keys(): loadvars['load_bathymetry'] = loadvars['load_bathy']; del loadvars['load_bathy']
        if 'load_temp' in loadvars.keys(): loadvars['load_temperature'] = loadvars['load_temp']; del loadvars['load_temp']
        if 'load_bathymetry' not in loadvars.keys(): loadvars['load_bathymetry'] = 'gebco'

        callbacks = []
        vartypes = np.unique([f.rsplit('_', 1)[0] for f in load_map.keys()])
        for key in loadvars.keys(): 
            if not key.lstrip('load_') in vartypes and not key == 'load_precip_type': 
                raise TypeError(f'{key} is not a valid argument. valid datasource args include:\n{", ".join([f"load_{v}" for v in vartypes])}')
        load_args = [loadvars[f'load_{v}'] if f'load_{v}' in loadvars.keys() else 0 for v in vartypes]
        
        # if load_args are not callable, convert it to a callable function
        for v, load_arg, ix in zip(vartypes, load_args, range(len(vartypes))):
            if callable(load_arg): callbacks.append(load_arg)

            elif isinstance(load_arg, str):
                key = f'{v}_{load_arg.lower()}'
                assert key in load_map.keys(), f'no map for {key} in load map: \n{load_map}'
                callbacks.append(load_map[key])
                with index(storagedir=storage_cfg(), south=south, north=north, west=west, east=east, top=top, bottom=bottom, start=start, end=end) as fetchmap:
                    fetchmap(callback=load_map[f'{v}_{load_arg.lower()}'])

            elif isinstance(load_arg, (int, float)):
                callbacks.append(lambda val, south, west, start, top, **_: [val, south, west, dt_2_epoch(start), top])

            elif isinstance(load_arg, (list, tuple, np.ndarray)):
                if len(load_arg) not in (3, 4):
                    raise ValueError(f'invalid array shape for load_{v}. '
                    'arrays must be ordered by [val, lat, lon] for 2D data, or '
                    '[val, lat, lon, depth] for 3D data')
                callbacks.append(lambda val, **_: val)

            else: raise TypeError(f'invalid type for load_{v}. '
                  'valid types include string, float, array, and callable')

        #q = Queue()
        attributes = []


        # prepare data pipeline
        is_3D = [v in var3d for v in vartypes]
        is_arr = [not isinstance(arg, (int, float)) for arg in load_args]
        columns = [fcn(val=val, south=south, north=north, west=west, east=east, top=top, bottom=bottom, start=start, end=end) for fcn,val in zip(callbacks, load_args)]
        intrpmap = [(Uniform2D, Uniform3D), (Interpolator2D, Interpolator3D)]
        reshapers = [reshape_3D if v else reshape_2D for v in is_3D]
        # map interpolations to dictionary
        self.interps = {}
        interpolators = map(lambda x, y: intrpmap[x][y], is_arr, is_3D)
        #interpolations = map(
        #    lambda i,r,c,v,q=q: Process(target=worker, args=(i,r,c,v,q)),
        #    interpolators, reshapers, columns, vartypes
        #)

        # assert that no empty arrays were returned by load function
        for col, var in zip(columns, vartypes):
            if isinstance(col, dict) or isinstance(col[0], (int, float)): continue
            assert len(col[0]) > 0, (
                    f'no data found for {var} in region {fmt_coords(dict(south=south, north=north, west=west, east=east, top=top, bottom=bottom, start=start, end=end))}. '
                    f'consider expanding the region')


        #if not os.environ.get('LOGLEVEL') == 'DEBUG':
        #    for i in interpolations: i.start()
        #    set_attributes() 
        #    for i in interpolations: i.join()

        # debug mode: disable parallelization for nicer stack trace
        #elif os.environ.get('LOGLEVEL') == 'DEBUG':
        #logging.debug('OCEAN DEBUG MSG: parallelization disabled')
        for i,r,c,v in zip(interpolators, reshapers, columns, vartypes):
            logging.debug(f'interpolating {v}')
            logging.debug(f'i = {i}\n r = {r}\nc = {c}\nv = {v}')
            obj = i(**r(c))
            #q.put((v, obj))
            attributes.append((v, obj))
        #set_attributes() 
        #def set_attributes(q):

        self.boundaries = dict(south=south, north=north, west=west, east=east, top=top, bottom=bottom, start=start, end=end)  
        self.origin = center_point(lat=[south, north], lon=[west, east])
        #for v in vartypes: self.interps[v].origin = self.origin
        self.precip_src = loadvars['load_precip_type'] if 'load_precip_type' in loadvars.keys() else None
        #x = 0
        #while x <= len(vartypes):
        while len(attributes) > 0:
            #x = x + 1
            #obj = q.get()
            obj = attributes.pop()
            self.interps[obj[0]] = obj[1]
            setattr(self, obj[0],         eval(f'lambda lat, lon, {"depth," if (obj[0] in var3d) else ""} grid=False, **kw: obj[1].interp(lat, lon, {"depth," if (obj[0] in var3d) else ""} grid, **kw)', dict(obj=obj)))
            setattr(self, f'{obj[0]}_xy', eval(f'lambda x, y,     {"z,"     if (obj[0] in var3d) else ""} grid=False, **kw: obj[1].interp_xy(x, y,  {"z,"     if (obj[0] in var3d) else ""} grid, **kw)', dict(obj=obj)))

        #q.close()

        return


    def bathymetry_deriv(self, lat, lon, axis, grid=False):
        assert axis in ('lat', 'lon'), 'axis must be \'lat\' or \'lon\''
        return self.interps['bathymetry'].interp(lat, lon, grid, lat_deriv_order=(axis=='lat'), lon_deriv_order=(axis=='lon'))

    def bathymetry_deriv_xy(self, x, y, axis, grid=False):
        assert axis in ('x', 'y'), 'axis must be \'x\' or \'y\''
        return self.interps['bathymetry'].interp_xy(x, y, grid, x_deriv_order=(axis=='x'), y_deriv_order=(axis=='y'))

    def precip_type(self, lat, lon, epoch, grid=False):
        callback, varmap = precip_type_map[self.precip_src]
        v,y,x,t = callback(west=min(lon), east=max(lon), south=min(lat), north=max(lat), start=self.boundaries['start'], end=self.boundaries['end'])
        return np.array([varmap[v] for v in NearestNDInterpolator((y,x,t), v)(lat,lon,epoch)])

    def precip_type_xy(self, x, y, epoch, grid=False):
        callback, varmap = precip_type_map[self.precip_src]
        v,yy,xx,t = callback(west=min(x), east=max(x), south=min(y), north=max(y), start=self.boundaries['start'], end=self.boundaries['end'])
        return np.array([varmap[v] for v in NearestNDInterpolator((xx,yy,t), v)(x,y,epoch)])

    # legacy support
    def bathy(self, *args, **kwargs): return self.bathymetry(*args, **kwargs)
    def bathy_xy(self, *args, **kwargs): return self.bathymetry_xy(*args, **kwargs)
    def bathy_deriv(self, *args, **kwargs): return self.bathymetry_deriv(*args, **kwargs)
    def bathy_deriv_xy(self, *args, **kwargs): return self.bathymetry_deriv_xy(*args, **kwargs)
    def temp(self, *args, **kwargs): return self.temperature(*args, **kwargs)
    def temp_xy(self, *args, **kwargs): return self.temperature_xy(*args, **kwargs)
