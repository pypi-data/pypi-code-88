import numpy as np
from occamypy import Vector, Operator
from occamypy.utils import get_backend, get_vector_type


class Matrix(Operator):
    """Operator built upon a matrix"""
    
    def __init__(self, matrix, domain, range, outcore=False):
        """Class constructor
        :param matrix   : matrix to use
        :param domain   : domain vector
        :param range    : range vector
        :param outcore  : use outcore sep operators
        """
        if not isinstance(domain, Vector):
            raise TypeError("ERROR! Domain vector not a vector object")
        if not isinstance(range, Vector):
            raise TypeError("ERROR! Range vector not a vector object")
        # Setting domain and range of operator and matrix to use during application of the operator
        if not (type(domain) == type(range)):
            raise TypeError("ERROR! Domain and Range have to be the same vector type")
          
        if matrix.shape[1] != domain.size:
            raise ValueError
        if matrix.shape[0] != range.size:
            raise ValueError
        
        super().__init__(domain, range)
        self.backend = get_backend(domain)
        self.matrix_type = get_vector_type(matrix)
        
        self.M = matrix
        self.outcore = outcore
    
    def __str__(self):
        return "MatrixOp"
    
    def forward(self, add, model, data):
        """d = A * m"""
        self.checkDomainRange(model, data)
        if not add:
            data.zero()
        data[:] += self.backend.matmul(self.M, model[:].flatten()).reshape(data.shape)
        return
    
    def adjoint(self, add, model, data):
        """m = A' * d"""
        self.checkDomainRange(model, data)
        if not add:
            model.zero()
        model[:] += np.matmul(self.M.T.conj(), data[:].flatten()).reshape(model.shape)
        return
    
    def getNdArray(self):
        return np.array(self.M)
