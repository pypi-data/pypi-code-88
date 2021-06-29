import numpy as np
from core.satellite import Satellite


class Mission:
    """
    Interface with the user

    Attributes
    ----------
    name : str
        Name of the mission
    SSP : list (5) of floats
        Scan strategy parameters [alpha (deg), beta (deg), spin period (min), precesion period (min), delta (deg)]
    """
    
    #default options
    options = {'name' : "Default_mission",
               'SSP' : [45., 50., 10., 93., 7.5],
               }

    def __init__(self, **kwargs):
        """
        Constructor

        Parameters
        ----------
        name : str
            Name of the mission
        SSP : list (5) of floats
            Scan strategy parameters [alpha (deg), beta (deg), spin period (min), precesion period (min), delta (deg)]
        delta_detector : float
            Half-angle of the detector fov (degrees)
        Nx : int 
            Number of horizontal detectors (rectangular array)
        Ny : int
            Number of vertical detectors (rectangular array)
        layout : str
            Type of array layout (circular/rectangular/custome)
        Nd : int
            Number of detectors of the circular array
        file_name : str
            File with detectors positions    
        """

        #makes sure that SSP elements are floats 
        try:
            kwargs['SSP'] = list(map(float, kwargs['SSP']))
        except KeyError:
            pass

        #update default_options
        self.options.update(kwargs)
    
        self.name = self.options['name']
        self.SSP = self.options['SSP']

        self.sat = Satellite(**kwargs)
