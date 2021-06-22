# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:01:13 2021

@author: Nikolay Dimitrov, DTU Wind Energy
"""


class turb_field:
    def __init__(self,**kwargs):
        ''' Parse inputs
        '''
        if 'params' in kwargs:
            self.params = kwargs['params']
        else:
            self.params = {'BaseName': 'Turb_py',
                           'alphaepsilon': 1.0,                           
                           'L' : 29.4,
                           'Gamma': 3.9,
                           'SeedNo': 1,
                           'Nx': 8192,
                           'Ny': 32,
                           'Nz': 32,
                           'dx': 1,
                           'dy': 1,
                           'dz': 1,
                           'HighFreqComp': 0,
                           'SaveToFile': 0
                           }

        # Parameters directly included as inputs will override the "params" dictionary
        if 'Nx' in kwargs:
            self.params['Nx'] = kwargs['Nx']
        if 'Ny' in kwargs:
            self.params['Ny'] = kwargs['Ny']            
        if 'Nz' in kwargs:
            self.params['Nz'] = kwargs['Nz']            
        if 'dx' in kwargs:
            self.params['dx'] = kwargs['dx']
        if 'dy' in kwargs:
            self.params['dy'] = kwargs['dy']            
        if 'dz' in kwargs:
            self.params['dz'] = kwargs['dz']
        if 'L' in kwargs:
            self.params['L'] = kwargs['L']
        if 'Gamma' in kwargs:
            self.params['Gamma'] = kwargs['Gamma']            
        if 'alphaepsilon' in kwargs:
            self.params['alphaepsilon'] = kwargs['alphaepsilon']           
        if 'SeedNo' in kwargs:
            self.params['SeedNo'] = kwargs['SeedNo']
        if 'SaveToFile' in kwargs:
            self.params['SaveToFile'] = kwargs['SaveToFile']
        if 'HighFreqComp' in kwargs:
            self.params['HighFreqComp'] = kwargs['HighFreqComp']
                   
            

            
    def generate(self):

        from hipersim.turbgen.generate_field import generate_field
        
        u, v, w = generate_field(
                                 BaseName = self.params['BaseName'],
                                 alphaepsilon = self.params['alphaepsilon'],
                                 L = self.params['L'],
                                 Gamma = self.params['Gamma'],
                                 SeedNo = self.params['SeedNo'],
                                 Nx = self.params['Nx'], 
                                 Ny = self.params['Ny'],
                                 Nz = self.params['Nz'],
                                 dx = self.params['dx'],
                                 dy = self.params['dy'],
                                 dz = self.params['dz'],
                                 HighFreqComp = self.params['HighFreqComp'],
                                 SaveToFile = self.params['SaveToFile']
                                 )
        self.u = u
        self.v = v
        self.w = w
        
        
        return u, v, w
    
    def constrain(self, Constraints = None):
        if Constraints is None:
            Constraints = self.Constraints
        else:
            self.Constraints = Constraints
            
        from hipersim.turbgen.constrain_field import constrain_field

        TurbOptions = {
                        'HighFreqComp': self.params['HighFreqComp'],
                        'SeedNo': self.params['SeedNo']}
        
        if ((hasattr(self,'u')==False) | (hasattr(self,'v') == False) | (hasattr(self,'w') == False)):
            self.generate()
        u, v, w = constrain_field(Constraints,
                                  self.u,
                                  self.v,
                                  self.w,
                                  BaseName = self.params['BaseName'],
                                  alphaepsilon = self.params['alphaepsilon'],
                                  L = self.params['L'],
                                  Gamma = self.params['Gamma'],
                                  Nx = self.params['Nx'], 
                                  Ny = self.params['Ny'],
                                  Nz = self.params['Nz'],
                                  dx = self.params['dx'],
                                  dy = self.params['dy'],
                                  dz = self.params['dz'],
                                  SaveToFile = self.params['SaveToFile'],
                                  UseNormalization = 0,
                                  TurbOptions = TurbOptions)
        self.u = u
        self.v = v
        self.w = w
        
        
        return u, v, w    