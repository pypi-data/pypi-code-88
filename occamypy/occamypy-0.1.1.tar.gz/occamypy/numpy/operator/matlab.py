import numpy as np
from scipy.io import loadmat, savemat
from occamypy.vector import Vector, VectorIC, superVector
from occamypy.utils import sep
from occamypy.operator import Operator

# try:
#     from oct2py import Oct2Py
# except ModuleNotFoundError:
#     import subprocess
#     import sys
#     subprocess.call([sys.executable, "-m", "pip", "install", "--user", "oct2py"])
#     from oct2py import Oct2Py
#
# octave = Oct2Py()

# _forward = "function y = Forward(x)\n"\
#            "    y = x-5"\
#            "end"

try:
    import matlab.engine as ME
except ModuleNotFoundError:
    print("MATLAB Engine API not installed."
          "Please find your `matlabroot` and run\n\t"
          "python matlabroot/extern/engines/python/setup.py install")


class Matlab(Operator):
    """Operator built upon a pair of matlab script"""
    
    def __init__(self, domain, range, forward, adjoint):
        """Class constructor
        :param domain  : domain vector
        :param range   : range vector
        :param forward : matlab script for forward operation
        :param adjoint : matlab script for adjoint operation
        """
        if not isinstance(domain, Vector):
            raise TypeError("ERROR! Domain vector not a vector object")
        if not isinstance(range, Vector):
            raise TypeError("ERROR! Range vector not a vector object")
        # Setting domain and range of operator and matrix to use during application of the operator
        self.setDomainRange(domain, range)
        
        eng = ME.start_matlab()
    
    def __str__(self):
        return "MatlabOp"
    
    def forward(self, add, model, data):
        """d = A * m"""
        self.checkDomainRange(model, data)
        if not add:
            data.zero()
        model_arr = model.getNdArray()
        data_arr = data.getNdArray()
        matlab_result = eng.
        data_arr +=
        return
    
    def adjoint(self, add, model, data):
        """m = A' * d"""
        self.checkDomainRange(model, data)
        if not add:
            model.zero()
        data_arr = data.getNdArray()
        if self.outcore:
            [model_arr, model_axis] = sep.read_file(model.vecfile)
            model_arr += np.matmul(self.M.H, data_arr.ravel()).reshape(model_arr.shape)
            sep.write_file(model.vecfile, model_arr, model_axis)
        else:
            model_arr = model.getNdArray()
            model_arr += np.matmul(self.M.T.conj(), data_arr.ravel()).reshape(model_arr.shape)
        return


if __name__ == '__main__':
    nx = 201
    x = VectorIC((nx,)).zero()
    x.getNdArray()[20:30] = 10.
    x.getNdArray()[50:75] = -5.
    x.getNdArray()[100:150] = 2.5
    x.getNdArray()[175:180] = 7.5
    
    print(0)
