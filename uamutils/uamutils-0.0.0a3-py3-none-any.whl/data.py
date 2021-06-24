
    
import numpy as np
from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
# import matplotlib

from .mod4 import MOD4

from .shared import *
from .blocks import Sphere, Tube, TubeInterped, Potential


# NOTE(arthur): cartopy should be an optional dependency and this is the fastest way to make it work.
#  When a user without cartopy tries to call data.plot(), he will get "name is not defined" errors.
#  Installing cartopy with pip alone is problematic, but it's really simple with conda - 
#    perhaps we need to make a conda package.
try:
    import cartopy.crs as ccrs
    from cartopy.util import add_cyclic_point
    from cartopy.feature.nightshade import Nightshade, _solar_position
except ModuleNotFoundError:
    pass

def listify(a):
    if type(a) == list:
        return a
    return [a]


# class Point:
#     def __init__(self, altkm, colat, lon):
#         self.altkm = altkm
#         self.lon = lon
#         self.colat = colat
#         self.ref_frame = 'geom'

# TODO?: use dataclass?
# TODO?: call this UAMCoords
class Coords:
    def __init__(self, altkm=None, colat=None, lon=None, ref_frame='geom'):
        self.altkm = altkm
        self.lon = lon
        self.colat = colat
        # reference frame can be spherical geomagnetic / geodetic.
        self.ref_frame = ref_frame

    def as_geom(self):
        # TODO: geod <-> geom
        return self 

    def xr_query(self):
        d = dict(altkm=self.altkm, colat=self.colat, lon=self.lon)
        return {k: d[k] for k in d if d[k] is not None}    

    def __str__(self):
        return class_contents(self) +'\n' + str(self.xr_query())

    def __repr__(self):
        return self.__str__()

class UAMValues:
    def __init__(self, values_xr, time, ref_frame, interp):
        self.param = f"{values_xr.name} ({values_xr.attrs['long_name']})"  
        self.units = values_xr.attrs['units']
        self.ref_frame = ref_frame
        self.interp = interp 
        self.time = time 

        self.coords = values_xr.coords
        self.values = values_xr.values
    
    # def plot(self):
    #     pass

    # NOTE(arthur): you can get some great ideas from xarray.DataArray.__str__()
    def __str__(self):
        # TODO: custom respresentation
        # return class_contents(self)
        
        frame = 'spherical geomagnetic' if self.ref_frame == 'geomag' else self.ref_frame

        res = ''
        res += f'Param: {self.param}\n'
        res += f'Units: {self.units}\n'
        res += f'Reference frame: {frame}\n'
        res += f'Interpolation: {self.interp}\n'
        res += f'Time: {self.time}\n\n'
        res += self.coords.__repr__() + '\n\n' #f'Coords:\n{self.coords}'
        res += f'Values:\n{self.values}'

        return res

    def __repr__(self):
        return self.__str__()


class UAMData:
    def __init__(self, mod4_path=None):
        self._mod4 = None
        self.blocks = None

        if mod4_path is not None:
            self.load(mod4_path)
    
    def coords(self, param_name):
        if param_name in self.blocks['sphere'].data_vars:
            return Coords(*[np.array(x) for x in self.blocks['sphere'].coords.values()])
        elif param_name in self.blocks['tube'].data_vars:
            return Coords(*[np.array(x) for x in self.blocks['tube'].coords.values()])
        elif param_name == 'pot':
            return Coords(None, *[np.array(x) for x in self.blocks['potential'].coords.values()])
            # return self.blocks['potential'].coords.values()
        return None            

    def infer_block(self, param_name, coords):
        if param_name == 'Te':
            # FIXME: handle this overlapping param 
            # if alt > ~130 (?) - take it from tube, otherwise - from sphere
            return 'tube'
        elif param_name in self.blocks['sphere'].data_vars:
            return 'sphere'
        elif param_name in self.blocks['tube'].data_vars:
            return 'tube'
        elif param_name == 'pot':
            return 'potential'
        return None
    
    # NOTE(arthur): this method is included to allow querying tube's irregular grid 
    #   potentially you can make this data accesible with general .select / .interp interface, but 
    #   I don't have the time to figure it out right now.
    def select_point(self, param_name, point):
        pass
    def interp_point(self, param_name, point):
        pass

    # TODO?: add 'tolerance' param? (see xarray.sel)
    # TODO: factor out code shared by self.select()
    def select(self, param_name, coords=None, block_name=None):
        if block_name is None:
            block_name = self.infer_block(param_name, coords)

        if coords is None:
            coords = self.coords(param_name)

        block = self.blocks[block_name]
        param = block[param_name]            

        try:
            pxr = param.sel(coords.as_geom().xr_query())
        except KeyError:
            # FIXME: change to ValueError or something like custom CoordinateError
            # TODO: more elaborate report - which value is missing
            raise ValueError('No such coordinates in mod4 data.') from None

        return UAMValues(pxr, ref_frame=block.attrs['reference_frame'], time=block.attrs['time_finished'], 
                         interp=None)

    # TODO: do interp the way UAM does it
    #   for sphere: start from finding closest height (not treating hor and vert coords the same)
    #   for tube: implement bilinear interp that is prototyped in tube_kd-tree.ipynb
    def interp(self, param_name, coords: Coords, method='nearest', block_name=None):
        if block_name is None:
            block_name = self.infer_block(param_name, coords)

        block = self.blocks[block_name]
        param = block[param_name]

        coords = coords.as_geom().xr_query()

        # handle lons passed in a list, e.g. lons=[100, 120]
        if 'lon' in coords:
            lons = listify(coords['lon'])
            new_lons = []

            for i in range(len(lons)):
                lon = lons[i]
                grid_lons = block.coords['lon']

                if grid_lons.max() < lon < 360:
                    if abs(360 - lon) < abs(grid_lons.max() - lon):
                        new_lons.append(grid_lons.min())
                new_lons.append(lon)
            coords['lon'] = new_lons
            

        if method == 'nearest':
            pxr = param.sel(coords, method='nearest')
        elif method == 'bilinear':
            # FIXME: start from picking height, then do a 2d interp.
            #   scipy.interp2d(kind='linear') might be the right thing,
            #   but perhaps scipy.interpn(method='linear') that is useb by xarray is satisfactory
            pxr = param.interp(coords)
        
        return UAMValues(pxr, ref_frame=block.attrs['reference_frame'], time=block.attrs['time_finished'], 
                         interp=method)

    # NOTE(arthur): this is a temporary quick-and-dirty implementation,
    #  plotting will be factored out into a separate module
    #   (or completely removed, and instead plotting examples will be provided as documentation)  
    def plot(self, param, altkm, proj='geomagnetic', interp='nearest'):
        projs = ['geographic', 'geomagnetic', 'geostationary', 'orthographic']
        if proj not in projs:
            raise ValueError(f'Provided projection argument({proj}) is not supported. '\
                f'Available projections are: {", ".join(projs)}') from None

        # TODO: other profiles
        c = 'altkm'

        if interp == 'none':
            data = self.select(param, Coords(altkm=altkm))
        else:
            data = self.interp(param, Coords(altkm=altkm), method=interp)

        vals, lons = add_cyclic_point(data.values, coord=data.coords['lon'])

        fig = Figure()
        ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

        if proj == 'orthographic':
            ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.Orthographic(0, 90))
            ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.Orthographic(180, -90))
        elif proj == 'geostationary':
            ax1 = fig.add_subplot(1, 2, 1,
                        projection=ccrs.Geostationary(central_longitude=270.0))
            ax2 = fig.add_subplot(1, 2, 2,
                        projection=ccrs.Geostationary(central_longitude=90.0))


        fig.set_size_inches(11.7, 8.3)

        # ax.set_global()

        colats = 90 - data.coords['colat']

        if proj == 'geographic':
            ax.coastlines() 
            ax.gridlines(draw_labels=True)

            # NOTE(arthur): next section of code transforms geomagnetic to geodetic coordinates
            #  and draws that with matplotlib's tricontourf
            #  (we also need to insert some closest-neighbour points 
            #    where geomagnetic poles belong to avoid blank spaces)
              
            lon_geo = []
            lat_geo = []

            # FIXME: it can be calculated only once and stored in memory upon Data.__init__ or, better yet,
            #   upon visualization class init.
            # FIXME: this is kinda slow, perhaps vectorize it?
            for c in colats:
                for l in lons:
                    lg, cg = mag2geo(l, c)

                    lon_geo.append(lg)
                    # lat_geo.append(cg)
                    lat_geo.append(90.0 - cg)
                
            '''
            geo_to_mag :: (geo_lon, geo_lat) -> (mag_lon, mag_lat)

            geo_to_mag( 180,  90) => (180,  78.7)
            geo_to_mag(-180,  90) => (180,  78.7)
            geo_to_mag(-180, -90) =>   (0, -78.7)
            geo_to_mag( 180, -90) =>   (0, -78.7)

            78.7 lat == 11.3 colat
            -78.7 lat == 168.7 colat
            '''

            ext_lon = lon_geo + [180, -180, 180, -180]
            ext_lat = lat_geo + [90, 90, -90, -90]

            val_1 = self.interp(param, Coords(altkm=altkm, colat=168.7, lon=180)).values[0]
            val_2 = self.interp(param, Coords(altkm=altkm, colat=11.3, lon=0)).values[0]

            fill_values = [val_1, val_1, val_2, val_2]

            cntr = ax.tricontourf(ext_lon, ext_lat, 
                    np.append(vals.reshape(-1), fill_values),
                    transform=ccrs.PlateCarree(), levels=100, extend='both')

            title_pad = 20
            ax.text(-0.07, 0.55, 'Geographic latitude', va='bottom', ha='center',
                    rotation='vertical', rotation_mode='anchor', transform=ax.transAxes, fontsize=14)
            ax.text(0.5, -0.2, 'Geographic longitude', va='bottom', ha='center',
                    rotation='horizontal', rotation_mode='anchor', transform=ax.transAxes, fontsize=14)

            
            ax.gridlines(draw_labels=True)
            cntr = ax.contourf(lons, colats, vals,
                               transform=ccrs.PlateCarree())

            fig.colorbar(cntr, ax=ax, fraction=0.025, pad=0.08)

            # plot day-night terminator
            nightshade = Nightshade(data.time, alpha=0.2)
            xy = nightshade._geoms[0].exterior.coords

            x, y = zip(*xy)

            for color, linewidth in (('black', 6), ('white', 4), ('black', 2)):
                ax.plot(x, y, transform=nightshade._crs, color=color,
                        linestyle='solid', linewidth=linewidth)

            # plot sun
            sun_lat, sun_lon = _solar_position(data.time)

            for marker, size in (('ko', 12), ('wo', 5), ('ko', 2)):
                ax.plot(sun_lon, sun_lat, marker, markersize=size)



        elif proj == 'geomagnetic':
            title_pad = 20
            ax.text(-0.07, 0.55, 'Magnetic latitude', va='bottom', ha='center',
                    rotation='vertical', rotation_mode='anchor', transform=ax.transAxes, fontsize=14)
            ax.text(0.5, -0.2, 'Magnetic longitude', va='bottom', ha='center',
                    rotation='horizontal', rotation_mode='anchor', transform=ax.transAxes, fontsize=14)

            
            ax.gridlines(draw_labels=True)
            cntr = ax.contourf(lons, colats,
                                vals,
                                transform=ccrs.PlateCarree())

            fig.colorbar(cntr, ax=ax, fraction=0.025, pad=0.08)

        else:
            # ax.set_visible(False)
            ax.set_frame_on(False)
            for axis in (ax1, ax2):
                axis.set_global()
                axis.gridlines(draw_labels=True, alpha=0.5)


                cntr = axis.contourf(lons, colats, vals, levels=12, transform=ccrs.PlateCarree())

            colorbar_axes = fig.add_axes([0.85, 0.25, 0.05, 0.5])
            fig.colorbar(cntr, cax=colorbar_axes)
            fig.subplots_adjust(right=0.8)  # otherwise colorbar overlaps with plot

            if proj == 'orthographic':
                title_pad=40
                ax1.set_title('Northern hemisphere', pad=10)
                ax2.set_title('Southern hemisphere', pad=10)

                # FIXME: MLT overlaps with gridlines, so we gonna comment this out for now
                # time = data.time
                # hour = time.hour + time.minute/60 - 78.7/15.0
                # bbox = {'color': 'white', 'boxstyle': 'circle, pad=0.0'}
                # for axis in (ax1, ax2):
                #     for deg, mltHour in [(0, '0'), (90, '6'), (180, '12'), (270, '18')]:
                #         axis.text(-hour * 15 + deg, 0, mltHour + ' MLT', fontsize=8,
                #                 transform=ccrs.PlateCarree(), bbox=bbox)


            elif proj == 'geostationary':
                title_pad = 40
                # NOTE(arthur): we neeed more pad to even titles out, 
                #   because cartopy omits 90E in the left axis labels 
                ax1.set_title('Eastern hemisphere', pad=20) 
                ax2.set_title('Western hemisphere', pad=10)



        title = f"{param} ({data.units}) at {round(float(data.coords['altkm']), 1)} km altitude\n{data.time}"
        ax.set_title(title, pad=title_pad, fontsize=18)


        return fig, data


    def load(self, mod4_path):
        self._mod4 = MOD4(mod4_path)

        time = TimeMoment.current

        sphere = Sphere(self._mod4, time)
        pot = Potential(self._mod4, time)
        tube = TubeInterped(self._mod4, time)

        self.blocks = {'sphere': sphere.as_xarray(), 'tube': tube.as_xarray(), 
                       'potential': pot.as_xarray()}
        
