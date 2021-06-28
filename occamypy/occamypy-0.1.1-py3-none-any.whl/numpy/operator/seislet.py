from math import log, ceil
from itertools import accumulate
import numpy as np
from occamypy import Operator, VectorBaseIC
from .signal import ZeroPad
from scipy.ndimage import gaussian_filter


def slope_estimate(d: np.ndarray, dz: float, dx: float, smooth: float = 20) -> (np.ndarray, np.ndarray):
    r"""Local slope estimation

    Local slopes are estimated using the *Structure Tensor* algorithm [1]_.
    Note that slopes are returned as :math:`arctan(\theta)` where
    :math:`\theta` is an angle defined in a RHS coordinate system with z axis
    pointing upward.

    Parameters
    ----------
    d : Input dataset of size :math:`n_z \times n_x`
    dz : Sampling in z-axis
    dx : Sampling in x-axis
    smooth : Lenght of smoothing filter to be applied to the estimated gradients

    Returns
    -------
    slopes : :obj:`np.ndarray`
        Estimated local slopes
    linearity : :obj:`np.ndarray`
        Estimated linearity

    Notes
    -----
    For each pixel of the input dataset :math:`\mathbf{d}` the local gradients
    :math:`d \mathbf{d} / dz` and :math:`g_z = d\mathbf{d} \ dx` are computed
    and used to define the following three quantities:
    :math:`g_{zz} = (d\mathbf{d} / dz) ^ 2`,
    :math:`g_{xx} = (d\mathbf{d} / dx) ^ 2`, and
    :math:`g_{zx} = d\mathbf{d} / dz * d\mathbf{d} / dx`. Such quantities are
    spatially smoothed and at each pixel their smoothed versions are
    arranged in a :math:`2 \times 2` matrix called the *smoothed
    gradient-square tensor*:

    .. math::
        \mathbf{G} =
        \begin{bmatrix}
           g_{zz}  & g_{zx} \\
           g_{zx}  & g_{xx}
        \end{bmatrix}


    Local slopes can be expressed as
    :math:`p = arctan(\frac{\lambda_{max} - g_{xx}}{g_{zx}})`.

    .. [1] Van Vliet, L. J.,  Verbeek, P. W., "Estimators for orientation and
        anisotropy in digitized images", Journal ASCI Imaging Workshop. 1995.

    """
    nz, nx = d.shape
    gz, gx = np.gradient(d, dz, dx)
    gzz, gzx, gxx = gz * gz, gz * gx, gx * gx
    
    # smoothing
    gzz = gaussian_filter(gzz, sigma=smooth)
    gzx = gaussian_filter(gzx, sigma=smooth)
    gxx = gaussian_filter(gxx, sigma=smooth)
    
    slopes = np.zeros(d.shape)
    linearity = np.zeros(d.shape)
    for iz in range(nz):
        for ix in range(nx):
            l1 = 0.5 * (gzz[iz, ix] + gxx[iz, ix]) + \
                 0.5 * np.sqrt((gzz[iz, ix] - gxx[iz, ix]) ** 2 +
                               4 * gzx[iz, ix] ** 2)
            l2 = 0.5 * (gzz[iz, ix] + gxx[iz, ix]) - \
                 0.5 * np.sqrt((gzz[iz, ix] - gxx[iz, ix]) ** 2 +
                               4 * gzx[iz, ix] ** 2)
            slopes[iz, ix] = np.arctan((l1 - gzz[iz, ix]) / gzx[iz, ix])
            linearity[iz, ix] = 1 - l2 / l1
    return slopes, linearity


def _predict_trace(trace: np.ndarray, t:np.ndarray, dt: float, dx: float, slope:np.ndarray, adj:bool=False) -> np.ndarray:
    r"""Slope-based trace prediction.

    Resample a trace to a new time axis defined by the local slopes along the
    trace. Slopes do implicitly represent a time-varying time delay
    :math:`\Delta t (t) = dx*s(t)`.

    The input trace is interpolated using sinc-interpolation to a new time
    axis given by the following formula: :math:`t_{new} = t + dx*s(t)`.

    Parameters
    ----------
    trace : :obj:`numpy.ndarray`
        Trace
    t : :obj:`numpy.ndarray`
        Time axis
    dt : :obj:`float`
        Time axis sampling
    dx : :obj:`float`
        Spatial axis sampling
    slope : :obj:`numpy.ndarray`
        Slope field
    adj : :obj:`bool`, optional
        Perform forward (``False``) or adjoint (``True``) operation

    Returns
    -------
    tracenew : :obj:`numpy.ndarray`
        Resampled trace

    """
    newt = t - dx * slope
    sinc = np.tile(newt, (len(newt), 1)) - \
           np.tile(t[:, np.newaxis], (1, len(newt)))
    if adj:
        tracenew = np.dot(trace, np.sinc(sinc / dt).T)
    else:
        tracenew = np.dot(trace, np.sinc(sinc / dt))
    return tracenew


def _predict_haar(traces, dt, dx, slopes, repeat=0, backward=False, adj=False):
    """Predict set of traces given time-varying slopes (Haar basis function)

    A set of input traces are resampled based on local slopes. If the number
    of traces in ``slopes`` is twice the number of traces in ``traces``, the
    resampling is done only once per trace. If the number of traces in
    ``slopes`` is a multiple of 2 of the number of traces in ``traces``,
    the prediction is done recursively or in other words the output traces
    are obtained by resampling the input traces followed by ``repeat-1``
    further resampling steps of the intermediate results.

    Parameters
    ----------
    traces : :obj:`numpy.ndarray`
        Input traces of size :math:`n_x \times n_t`
    dt : :obj:`float`
        Time axis sampling of the slope field
    dx : :obj:`float`
        Spatial axis sampling of the slope field
    slopes: :obj:`numpy.ndarray`
        Slope field of size :math:`n_x * 2^{repeat} \times n_t`
    repeat : :obj:`int`, optional
        Number of repeated predictions
    backward : :obj:`bool`, optional
        Predicted trace is on the right (``False``) or on the left (``True``)
        of input trace
    adj : :obj:`bool`, optional
        Perform forward (``False``) or adjoint (``True``) operation

    Returns
    -------
    pred : :obj:`numpy.ndarray`
        Predicted traces

    """
    if backward:
        iback = 1
        idir = -1
    else:
        iback = 0
        idir = 1
    slopejump = 2 ** (repeat + 1)
    repeat = 2 ** repeat

    nx, nt = traces.shape
    t = np.arange(nt) * dt
    pred = np.zeros_like(traces)
    for ix in range(nx):
        pred_tmp = traces[ix]
        if adj:
            for irepeat in range(repeat - 1, -1, -1):
                #print('Slope at', ix * slopejump + iback * repeat + idir * irepeat)
                pred_tmp = \
                    _predict_trace(pred_tmp, t, dt, idir * dx,
                                   slopes[ix * slopejump + iback * repeat + idir * irepeat],
                                   adj=True)
        else:
            for irepeat in range(repeat):
                #print('Slope at', ix * slopejump + iback * repeat + idir * irepeat)
                pred_tmp = \
                    _predict_trace(pred_tmp, t, dt, idir * dx,
                                   slopes[ix * slopejump + iback * repeat + idir * irepeat])
        pred[ix] = pred_tmp
    return pred


def _predict_lin(traces, dt, dx, slopes, repeat=0, backward=False, adj=False):
    """Predict set of traces given time-varying slopes (Linear basis function)

    See _predict_haar for details.
    """
    if backward:
        iback = 1
        idir = -1
    else:
        iback = 0
        idir = 1
    slopejump = 2 ** (repeat + 1)
    repeat = 2 ** repeat

    nx, nt = traces.shape
    t = np.arange(nt) * dt
    pred = np.zeros_like(traces)
    for ix in range(nx):
        pred_tmp = traces[ix]
        #print('Data+ at', ix * slopejump)
        if adj:
            if not ((ix == 0 and not backward) or (ix == nx - 1 and backward)):
                pred_tmp1 = traces[ix - idir]
            #if ix > 0: print('Data- at', (ix - idir) * slopejump)
            for irepeat in range(repeat - 1, -1, -1):
                if (ix == 0 and not backward) or (ix == nx - 1 and backward):
                    #print('Slope+ at', ix * slopejump + iback * repeat + idir * irepeat)
                    pred_tmp = \
                        _predict_trace(pred_tmp, t, dt, idir * dx,
                                       slopes[ix * slopejump + iback * repeat + idir * irepeat],
                                       adj=True)
                    pred_tmp1 = 0
                else:
                    #print('Slope+ at', ix * slopejump + iback * repeat + idir * irepeat)
                    #print('Slope- at', ix * slopejump + iback * repeat - idir * irepeat)
                    pred_tmp = \
                        _predict_trace(pred_tmp, t, dt, idir * dx,
                                       slopes[ix * slopejump + iback * repeat + idir * irepeat],
                                       adj=True)
                    pred_tmp1 = \
                        _predict_trace(pred_tmp1, t, dt, (-idir) * dx,
                                       slopes[ix * slopejump + iback * repeat - idir * irepeat],
                                       adj=True)
        else:
            if not ((ix == nx - 1 and not backward) or (ix == 0 and backward)):
                pred_tmp1 = traces[ix + idir]
            #if ix < nx - 1: print('Data- at', (ix + idir) * slopejump)
            for irepeat in range(repeat):
                if (ix == nx - 1 and not backward) or (ix == 0 and backward):
                    #print('Slope+ at', ix * slopejump + iback * repeat + idir * irepeat)
                    pred_tmp = \
                        _predict_trace(pred_tmp, t, dt, idir * dx,
                                       slopes[ix * slopejump + iback * repeat + idir * irepeat])
                    pred_tmp1 = 0
                else:
                    #print('Slope+ at', ix * slopejump + iback * repeat + idir * irepeat)
                    #print('Slope- at', (ix + idir) * slopejump + iback * repeat - idir * irepeat)
                    pred_tmp = \
                        _predict_trace(pred_tmp, t, dt, idir * dx,
                                       slopes[ix * slopejump + iback * repeat + idir * irepeat])
                    pred_tmp1 = \
                        _predict_trace(pred_tmp1, t, dt, (-idir) * dx,
                                       slopes[(ix + idir) * slopejump + iback * repeat - idir * irepeat])

        #if (adj and ((ix == 0 and not backward) or (ix == nx - 1 and backward))) or
        #    (ix == nx - 1 and not backward) or (ix == 0 and backward):
        #    pred[ix] = pred_tmp
        #else:
        if ix == nx - 1:
            pred[ix] = pred_tmp + pred_tmp1 / 2.
        else:
            pred[ix] = (pred_tmp + pred_tmp1) / 2.
    return pred


class Seislet(Operator):
    r"""2D Seislet operator.

    Apply 2D-Seislet Transform to an input array given an
    estimate of its local ``slopes``. In forward mode, the input array is
    reshaped into a two-dimensional array of size :math:`n_x \times n_t` and
    the transform is performed along the first (spatial) axis (see Notes for
    more details).

    Parameters
    ----------
    slopes : Slope field of size :math:`n_t \times n_x`.
    dt : Sampling steps in t-axis.
    dx : Sampling steps in x-axis.
    level : Number of scaling levels (must be >=0).
    kind : Basis function used for predict and update steps: ``haar`` or
        ``linear``.
    inverse : Apply inverse transform when invoking the adjoint (``True``)
        or not (``False``). Note that in some scenario it may be more
        appropriate to use the exact inverse as adjoint of the Seislet
        operator even if this is not an orthogonal operator and the dot-test
        would not be satisfied (see Notes for details). Otherwise, the user
        can access the inverse directly as method of this class.

    Raises
    ------
    NotImplementedError
        If ``kind`` is different from haar or linear

    Notes
    -----
    The Seislet transform [1]_ is implemented using the lifting scheme.

    In its simplest form (i.e., corresponding to the Haar basis function for
    the Wavelet transform) the input dataset is separated into even
    (:math:`\mathbf{e}`) and odd (:math:`\mathbf{o}`) traces. Even traces are
    used to forward predict the odd traces using local slopes and the
    new odd traces (also referred to as residual) is defined as:

    .. math::
        \mathbf{o}^{i+1} = \mathbf{r}^i = \mathbf{o}^i - P(\mathbf{e}^i)

    where :math:`P = P^+` is the slope-based forward prediction operator
    (which is here implemented as a sinc-based resampling).
    The residual is then updated and summed to the even traces to obtain the
    new even traces (also referred to as coarse representation):

    .. math::
        \mathbf{e}^{i+1} = \mathbf{c}^i = \mathbf{e}^i + U(\mathbf{o}^{i+1})

    where :math:`U = P^- / 2` is the update operator which performs a
    slope-based backward prediction. At this point
    :math:`\mathbf{e}^{i+1}` becomes the new data and the procedure is repeated
    `level` times (at maximum until :math:`\mathbf{e}^{i+1}` is a single trace.
    The Seislet transform is effectively composed of all residuals and
    the coarsest data representation.

    In the inverse transform the two operations are reverted. Starting from the
    coarsest scale data representation :math:`\mathbf{c}` and residual
    :math:`\mathbf{r}`, the even and odd parts of the previous scale are
    reconstructed as:

    .. math::
        \mathbf{e}^i = \mathbf{c}^i - U(\mathbf{r}^i)
        = \mathbf{e}^{i+1} - U(\mathbf{o}^{i+1})

    and:

    .. math::
        \mathbf{o}^i  = \mathbf{r}^i + P(\mathbf{e}^i)
        = \mathbf{o}^{i+1} + P(\mathbf{e}^i)

    A new data is formed by interleaving :math:`\mathbf{e}^i` and
    :math:`\mathbf{o}^i` and the procedure repeated until the new data as the
    same number of traces as the original one.

    Finally the adjoint operator can be easily derived by writing the lifting
    scheme in a matricial form:

    .. math::
        \begin{bmatrix}
           \mathbf{r}_1  \\ \mathbf{r}_2  \\ ... \\ \mathbf{r}_N \\
           \mathbf{c}_1  \\ \mathbf{c}_2  \\ ... \\ \mathbf{c}_N
        \end{bmatrix} =
        \begin{bmatrix}
           \mathbf{I} & \mathbf{0} & ... & \mathbf{0} & -\mathbf{P} & \mathbf{0}  & ... & \mathbf{0}  \\
           \mathbf{0} & \mathbf{I} & ... & \mathbf{0} & \mathbf{0}  & -\mathbf{P} & ... & \mathbf{0}  \\
           ...        & ...        & ... & ...        & ...         & ...         & ... & ...         \\
           \mathbf{0} & \mathbf{0} & ... & \mathbf{I} & \mathbf{0}  & \mathbf{0}  & ... & -\mathbf{P} \\
           \mathbf{U} & \mathbf{0} & ... & \mathbf{0} & \mathbf{I}-\mathbf{UP} & \mathbf{0}  & ... & \mathbf{0}  \\
           \mathbf{0} & \mathbf{U} & ... & \mathbf{0} & \mathbf{0}  & \mathbf{I}-\mathbf{UP} & ... & \mathbf{0}  \\
           ...        & ...        & ... & ...        & ...         & ...         & ... & ...         \\
           \mathbf{0} & \mathbf{0} & ... & \mathbf{U} & \mathbf{0}  & \mathbf{0}  & ... & \mathbf{I}-\mathbf{UP} \\
        \end{bmatrix}
        \begin{bmatrix}
           \mathbf{o}_1  \\ \mathbf{o}_2  \\ ... \\ \mathbf{o}_N \\
           \mathbf{e}_1  \\ \mathbf{e}_2  \\ ... \\ \mathbf{e}_N \\
        \end{bmatrix}

    Transposing the operator leads to:

    .. math::
        \begin{bmatrix}
           \mathbf{o}_1  \\ \mathbf{o}_2  \\ ... \\ \mathbf{o}_N \\
           \mathbf{e}_1  \\ \mathbf{e}_2  \\ ... \\ \mathbf{e}_N \\
        \end{bmatrix} =
        \begin{bmatrix}
           \mathbf{I} & \mathbf{0} & ... & \mathbf{0} & -\mathbf{U^T} & \mathbf{0}  & ... & \mathbf{0}  \\
           \mathbf{0} & \mathbf{I} & ... & \mathbf{0} & \mathbf{0} & -\mathbf{U^T} & ... & \mathbf{0}  \\
           ...        & ...        & ... & ...        & ...        & ...        & ... & ...         \\
           \mathbf{0} & \mathbf{0} & ... & \mathbf{I} & \mathbf{0} & \mathbf{0} & ... & -\mathbf{U^T} \\
           \mathbf{P^T} & \mathbf{0} & ... & \mathbf{0} & \mathbf{I}-\mathbf{P^TU^T} & \mathbf{0} & ... & \mathbf{0}  \\
           \mathbf{0} & \mathbf{P^T} & ... & \mathbf{0} & \mathbf{0} & \mathbf{I}-\mathbf{P^TU^T} & ... & \mathbf{0}  \\
           ...        & ...        & ... & ...          & ...        & ...        & ... & ...         \\
           \mathbf{0} & \mathbf{0} & ... & \mathbf{P^T} & \mathbf{0} & \mathbf{0} & ... & \mathbf{I}-\mathbf{P^TU^T} \\
        \end{bmatrix}
        \begin{bmatrix}
           \mathbf{r}_1  \\ \mathbf{r}_2  \\ ... \\ \mathbf{r}_N \\
           \mathbf{c}_1  \\ \mathbf{c}_2  \\ ... \\ \mathbf{c}_N
        \end{bmatrix}

    which can be written more easily in the following two steps:

    .. math::
        \mathbf{o} = \mathbf{r} + \mathbf{U}^H\mathbf{c}

    and:

    .. math::
        \mathbf{e} = \mathbf{c} - \mathbf{P}^H(\mathbf{r} + \mathbf{U}^H(\mathbf{c})) =
                     \mathbf{c} - \mathbf{P}^H\mathbf{o}

    Similar derivations follow for more complex wavelet bases.

    .. [1] Fomel, S.,  Liu, Y., "Seislet transform and seislet frame",
       Geophysics, 75, no. 3, V25-V38. 2010.

    """
    
    def __init__(self, slopes: VectorBaseIC, dt: float = 1., dx: float = 1.,
                 level: bool = None, kind: str = 'haar', inverse: bool = False):
        
        # define predict and update steps
        if kind == 'haar':
            self.predict_fn = _predict_haar
        elif kind == 'linear':
            self.predict_fn = _predict_lin
        else:
            raise NotImplementedError('kind should be haar or linear')
    
        # define padding for length to be power of 2
        dims = slopes.shape
        ndimpow2 = 2 ** ceil(log(dims[0], 2))
        pad = [(0, 0)] * len(dims)
        pad[0] = (0, ndimpow2 - dims[0])
        self.padding = ZeroPad(slopes, pad)
        self.dims = list(dims)
        self.dims[0] = ndimpow2
        self.nx, self.nt = self.dims
    
        # define levels
        nlevels_max = int(np.log2(self.dims[0]))
        self.levels_size = np.flip(np.array([2 ** i for i in range(nlevels_max)]))
        if level is not None:
            self.levels_size = self.levels_size[:level]
        else:
            self.levels_size = self.levels_size[:-1]
            level = nlevels_max - 1
        self.level = level
        self.levels_cum = np.cumsum(self.levels_size)
        self.levels_cum = np.insert(self.levels_cum, 0, 0)
    
        self.dx, self.dt = dx, dt
        self.slopes = self.padding * slopes
        self.slopes_arr = self.slopes.getNdArray()
        self.inverse = inverse
        super(Seislet, self).__init__(domain=slopes, range=self.slopes)
    
    def forward(self, add, model, data):
        """Forward operator"""
        self.checkDomainRange(model, data)
        if not add:
            data.zero()
        # get Ndarrays
        x = (self.padding * model).getNdArray()
        
        # compute with numpy
        y = np.zeros(self.nt, (np.sum(self.levels_size) + self.levels_size[-1], self.nt))
        for ilevel in range(self.level):
            odd = x[:, 1::2]
            even = x[:, ::2]
            res = odd - self.predict_fn(even, dt=self.dt, dx=self.dx, slopes=self.slopes_arr, repeat=ilevel, backward=False)
            x = even + self.predict_fn(res, dt=self.dt, dx=self.dx, slopes=self.slopes_arr, repeat=ilevel, backward=True) / 2.
            y[self.levels_cum[ilevel]:self.levels_cum[ilevel + 1]] = res
        y[self.levels_cum[-1]:] = x
        
        # write to data
        data.getNdArray()[:] += y.T
        return
    
    def adjoint(self, add, model, data):
        self.checkDomainRange(model, data)
        if not add:
            model.zero()
        
        x = data.getNdArray()
        
        # now we work with np.ndarrays
        if not self.inverse:
            y = x[self.levels_cum[-1]:]
            for ilevel in range(self.level, 0, -1):
                res = x[self.levels_cum[ilevel - 1]:self.levels_cum[ilevel]]
                odd = res + self.predict_fn(y, self.dt, self.dx, self.slopes_arr,
                                            repeat=ilevel - 1, backward=True,
                                            adj=True) / 2.
                even = y - self.predict_fn(odd, self.dt, self.dx, self.slopes_arr,
                                           repeat=ilevel - 1, backward=False,
                                           adj=True)
                y = np.zeros((2 * even.shape[0], self.nt))
                y[1::2] = odd
                y[::2] = even
        else:
            y = x[self.levels_cum[-1]:]
            for ilevel in range(self.level, 0, -1):
                res = x[self.levels_cum[ilevel - 1]:self.levels_cum[ilevel]]
                even = y - self.predict_fn(res, self.dt, self.dx, self.slopes_arr,
                                           repeat=ilevel - 1, backward=True) / 2.
                odd = res + self.predict_fn(even, self.dt, self.dx, self.slopes_arr,
                                            repeat=ilevel - 1, backward=False)
                y = np.zeros((2 * even.shape[0], self.nt))
                y[1::2] = odd
                y[::2] = even
        
        # convert to VectorIC
        y = self.padding.T * VectorBaseIC(y)
        model + y
        return


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    from pathlib import Path
    
    PLOT = False
    
    inputfile = Path('../../tutorials/data/sigmoid.npz')
    # we want a (nt, nx) vector, C-ordered
    data = VectorBaseIC(np.load(inputfile)['sigmoid'])
    
    nx, nt = data.shape
    dt, dx = 0.004, 8
    t, x = np.arange(nt) * dt, np.arange(nx) * dx
    
    # slope estimation (dz,dx)
    slope = data.clone().zero()
    slope.getNdArray()[:] = -slope_estimate(data.getNdArray().T, dz=dt, dx=dx, smooth=6)[0].T
    
    if PLOT:
        clip = 0.5 * np.max(np.abs(data.arr))
        clip_s = np.max(np.abs(slope.arr))
        opts = dict(aspect='auto', extent=(x[0], x[-1], t[-1], t[0]))
        
        fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True, sharex=True)
        axs[0].imshow(data.getNdArray().T, cmap='gray', vmin=-clip, vmax=clip, **opts)
        axs[0].set(xlabel='Position [m]', ylabel='Time [s]', title='Data')
        axs[0].axis('tight')
        im = axs[1].imshow(slope.getNdArray().T, cmap='jet', vmin=-clip_s, vmax=clip_s, **opts)
        axs[1].set(xlabel='Position [m]', title='Slopes')
        axs[1].axis('tight')
        cax = make_axes_locatable(axs[1]).append_axes('right', size='5%', pad=0.1)
        cb = fig.colorbar(im, cax=cax, orientation='vertical')
        cb.set_label('[m/s]')
        fig.tight_layout()
        plt.show()
    
    # Seislet operator
    Sop = Seislet(slope, dt=dt, dx=dx, kind='haar')

    seis = Sop * data
    # seis = seis.reshape(nx, nt)

    nlevels_max = int(np.log2(nx))
    levels_size = np.flip(np.array([2 ** i for i in range(nlevels_max)]))
    levels_cum = np.cumsum(levels_size)

    plt.figure(figsize=(14, 5))
    plt.imshow(seis.getNdArray(), cmap='gray', vmin=-clip, vmax=clip,
               extent=(1, seis.shape[0], t[-1], t[0]))
    for level in levels_cum:
        plt.axvline(level + 0.5, color='w')
    plt.xlabel('Scale')
    plt.ylabel('Time [s]')
    plt.title('Seislet transform')
    plt.colorbar()
    plt.axis('tight')
    plt.tight_layout(pad=.5)
    plt.show()
    
    # keep the strongest 25% of transform coefficients and reconstruct the data
    perc = 0.25
    seis_strong_idx = np.argsort(-np.abs(seis.ravel()))
    seis_strong = np.abs(seis.ravel())[seis_strong_idx]

    fig, ax = plt.subplots()
    ax.plot(range(1, len(seis_strong) + 1),
            seis_strong / seis_strong[0], label='Seislet')
    ax.set(xlabel="n", ylabel="Coefficient strength [%]",
           title="Transform Coefficients")
    ax.axvline(np.rint(len(seis_strong) * perc),
               color='k', label=f'{100 * perc:.0f}%')
    ax.legend()
    fig.tight_layout()

    seis1 = np.zeros_like(seis.ravel())
    seis_strong_idx = seis_strong_idx[:int(np.rint(len(seis_strong) * perc))]
    seis1[seis_strong_idx] = seis.ravel()[seis_strong_idx]
    d_seis = Sop.inverse(seis1)
    d_seis = d_seis.reshape(nx, nt)
    
    if PLOT:
        opts.update(dict(cmap='gray', vmin=-clip, vmax=clip))
        fig, axs = plt.subplots(1, 3, figsize=(14, 7), sharex=True, sharey=True)
        axs[0].imshow(data.T, **opts)
        axs[0].set(title='Data')
        axs[1].imshow(d_seis.T, **opts)
        axs[1].set(title=f'Rec. from Seislet ({100 * perc:.0f}% of coeffs.)')
        axs[2].imshow((data - d_seis).T, **opts)
        axs[2].set(title='Error from Seislet Rec.')
        for i in range(3):
            axs[i].set(xlabel='Position [m]')
        plt.tight_layout(pad=.5)
        plt.show()
