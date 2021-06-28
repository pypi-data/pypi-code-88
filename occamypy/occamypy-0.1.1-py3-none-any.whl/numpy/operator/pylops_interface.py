import numpy as np
from occamypy import Operator, VectorNumpy, dask

try:
    import pylops
except ImportError:
    import os
    
    os.system("pip install --user pylops")
    import pylops


class FromPylops(Operator):
    
    def __init__(self, domain, range, op):
        """
        Cast a pylops LinearOperator to Operator
        """
        assert isinstance(op, pylops.LinearOperator), "op has to be a pylops.LinearOperator"
        assert op.shape[0] == range.size, "Range and operator rows mismatch"
        assert op.shape[1] == domain.size, "Domain and operator columns mismatch"
        
        self.name = op.__str__()
        self.op = op
        
        super(FromPylops, self).__init__(domain, range)
    
    def __str__(self):
        return self.name.replace('<', '').replace('>', '')
    
    def forward(self, add, model, data):
        self.checkDomainRange(model, data)
        if not add:
            data.zero()
        x = model.getNdArray().copy().ravel()
        y = self.op.matvec(x)
        data.getNdArray()[:] += y.reshape(data.shape)
        return
    
    def adjoint(self, add, model, data):
        self.checkDomainRange(model, data)
        if not add:
            model.zero()
        y = data.getNdArray().copy().ravel()
        x = self.op.rmatvec(y)
        model.getNdArray()[:] += x.reshape(model.shape)
        return


class ToPylops(pylops.LinearOperator):
    
    def __init__(self, op: Operator):
        """
        Cast an in-core Operator to pylops.LinearOperator
        :param op: `occamypy.Operator` object (or child)
        """
        self.explicit = False
        self.shape = (op.range.size, op.domain.size)
        self.dtype = op.domain.getNdArray().dtype
        
        assert isinstance(op, Operator), 'op has to be an Operator'
        self.op = op
        
        # these are just temporary vectors, used by forward and adjoint computations
        self.domain = op.domain.clone()
        self.range = op.range.clone()
    
    def _matvec(self, x):
        x_ = self.domain.clone()
        x_[:] = x.reshape(self.domain.shape).astype(self.dtype)
        y_ = self.range.clone()
        self.op.forward(False, x_, y_)
        return y_.getNdArray().ravel()
    
    def _rmatvec(self, y):
        y_ = self.range.clone()
        y_[:] = y.reshape(self.range.shape).astype(self.dtype)
        x_ = self.domain.clone()
        self.op.adjoint(False, x_, y_)
        return x_.getNdArray().ravel()


class DaskToPylops(pylops.LinearOperator):
    
    def __init__(self, op, chunks):
        """
        Cast a DaskOperator to pylops.LinearOperator
        :param op: `occamypy.DaskOperator` object (or child)
        """
        self.explicit = False
        self.shape = (op.range.size, op.domain.size)
        self.dtype = op.domain.getNdArray()[0].dtype
        
        assert isinstance(op, dask.DaskOperator), 'op has to be a DaskOperator'
        self.op = op
        self.chunks = chunks
    
    def _matvec(self, x):
        # create a dask vector from numpy array
        x_ = dask.DaskVector(self.op.client,
                             VectorNumpy(x.reshape(self.op.domain.shape[0]).astype(self.dtype)),
                             self.chunks)
        y_ = self.op.range.clone()
        self.op.forward(False, x_, y_)
        return y_.getNdArray().ravel()
    
    def _rmatvec(self, y):
        y_ = self.range.clone()
        y_[:] = y.reshape(self.range.shape).astype(self.dtype)
        x_ = self.op.domain.clone()
        self.op.adjoint(False, x_, y_)
        return x_.getNdArray().ravel()


if __name__ == '__main__':
    from occamypy import Scaling
    import matplotlib.pyplot as plt

    # shape = (3, 5)
    # x = VectorNumpy(shape).set(1.)
    #
    # # test FromPylops
    # d = np.arange(x.size)
    # D = FromPylops(x, x, pylops.Diagonal(d))
    # D.dotTest(True)
    #
    # # test ToPylops
    # S = ToPylops(Scaling(x, 2.))
    # pylops.utils.dottest(S, x.size, x.size, tol=1e-6, complexflag=0, verb=True)
    # print("\t", np.isclose((S * x.arr.ravel()).reshape(x.shape), 2.*x.arr).all())
    
    # # from interesting pylops
    # # https://pylops.readthedocs.io/en/latest/tutorials/ctscan.html#sphx-glr-tutorials-ctscan-py
    # def radoncurve(x, r, theta):
    #     return (r - ny // 2) / (np.sin(np.deg2rad(theta)) + 1e-15) + np.tan(np.deg2rad(90 - theta)) * x + ny // 2
    #
    # x = np.load('../../tutorials/data/shepp_logan_phantom.npy')
    # x = x / x.max()
    # ny, nx = x.shape
    #
    # ntheta = 150
    # theta = np.linspace(0., 180., ntheta, endpoint=False)
    #
    # RLop = pylops.signalprocessing.Radon2D(np.arange(ny), np.arange(nx),
    #                                        theta, kind=radoncurve,
    #                                        centeredh=True, interp=False,
    #                                        engine='numpy', dtype='float64')
    #
    # y = RLop.H * x.T.ravel()
    # y = y.reshape(ntheta, ny).T
    #
    # xrec = RLop * y.T.ravel()
    # xrec = xrec.reshape(nx, ny).T
    
    # fig, axs = plt.subplots(1, 3, figsize=(10, 4))
    # axs[0].imshow(x, vmin=0, vmax=1, cmap='gray')
    # axs[0].set_title('Model')
    # axs[0].axis('tight')
    # axs[1].imshow(y, cmap='gray')
    # axs[1].set_title('Data')
    # axs[1].axis('tight')
    # axs[2].imshow(xrec, cmap='gray')
    # axs[2].set_title('Adjoint model')
    # axs[2].axis('tight')
    # fig.tight_layout()
    # plt.show()
    
    # # TODO why the fuck they need to be transposed?
    # x_T = VectorNumpy(x).transpose()
    # y_T = VectorNumpy((ntheta, ny))
    # R_T = FromPylops(x_T, y_T, RLop.H)
    # y_T = R_T * x_T
    # xrec_T = R_T.H * y_T
    #
    # fig, axs = plt.subplots(1, 3, figsize=(10, 4))
    # axs[0].imshow(x_T[:], vmin=0, vmax=1, cmap='gray')
    # axs[0].set_title('Model')
    # axs[0].axis('tight')
    # axs[1].imshow(y_T[:], cmap='gray')
    # axs[1].set_title('Data')
    # axs[1].axis('tight')
    # axs[2].imshow(xrec_T[:], cmap='gray')
    # axs[2].set_title('Adjoint model')
    # axs[2].axis('tight')
    # fig.tight_layout()
    # plt.show()
    
    # now with dask
    from occamypy import dask
    
    client = dask.DaskClient(local_params={"processes": True}, n_wrks=4)
    print("Number of workers = %d" % client.getNworkers())
    print("Workers Ids = %s" % client.getWorkerIds())
    
    vec = VectorNumpy(np.load('../../tutorials/data/shepp_logan_phantom.npy') * 1.).scale(1 / 255)
    
    # method 1: instantiate a vector template and spread it using the chunk parameter
    vec_ = dask.DaskVector(client,
                           vector_template=vec,
                           chunks=(2, 3, 5, 10))
    
    # method 2: instantiate multiple vectors and spreading them to the given workers
    vecD = dask.DaskVector(client,
                           vectors=[VectorNumpy(vec[:50]),
                                    VectorNumpy(vec[50:150]),
                                    VectorNumpy(vec[150:])],
                           chunks=(1, 1, 0, 1))
    
    # Instantiating Dask operator: FirstDerivative from pylops
    # D_ = dask.DaskOperator(
    #     client,
    #     FromPylops,
    #     [(v, v, pylops.FirstDerivative(np.prod(shape))) for v, shape in zip(vec_.vecDask, vec_.shape)],
    #     vec_.chunks)
    DD = dask.DaskOperator(
        client,
        FromPylops,
        [(v, v, pylops.FirstDerivative(np.prod(shape))) for v, shape in zip(vecD.vecDask, vecD.shape)],
        vecD.chunks)
    
    # Dot-product test
    DD.dotTest(True)
    # # Power method
    # max_eig = D_.powerMethod()
    # print("\nMaximum eigenvalue = %s" % max_eig)
    
    Spread = dask.DaskSpread(client, vec, [1]*client.getNworkers())
    # Collect a dask vector to a in-core vector
    Collect = dask.DaskCollect(vecD, vec)
    
    # TODO cast a DaskOperator to Pylops
    A_ = dask.DaskOperator(client,
                           Scaling,
                           [(v, 10) for v in vec_.vecDask],
                           vec_.chunks)
    # A_.dotTest(True)
    
    A = DaskToPylops(A_, vec_.chunks)
    y = A * np.ones(vec_.size)
    
    # pylops.utils.dottest(A)
    pylops.utils.dottest(A, *A.shape)
    
    print(0)

__all__ = [
    "ToPylops",
    "FromPylops",
]
