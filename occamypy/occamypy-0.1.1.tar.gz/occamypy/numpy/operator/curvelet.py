import numpy as np
from math import floor, ceil, log2
from occamypy import Operator, VectorBaseIC


def _fft_direct(x):
    return np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(x)) / np.sqrt(np.prod(x.shape)))


def _fft_inverse(x):
    return np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(x))) * np.sqrt(np.prod(x.shape))


def _fdct_wrapping_window(x):
    """
    Create the two halves of a C^inf compactly supported window
    
    :param x : :obj:`np.ndarray´
        vector of abscissae, the relevant ones from 0 to 1
    :return wl, wr: vectors of samples of the left and right halves of the window
    """
    wl = np.zeros_like(x)
    wr = np.zeros_like(x)
    
    wr[(x > 0) & (x < 1)] = np.exp(1 - 1. / (1 - np.exp(1 - 1. / x[(x > 0) & (x < 1)])))
    wr[x <= 0] = 1
    wl[(x > 0) & (x < 1)] = np.exp(1 - 1. / (1 - np.exp(1 - 1. / (1 - x[(x > 0) & (x < 1)]))))
    wl[x >= 1] = 1
    
    norm_vector = np.sqrt(wl ** 2 + wr ** 2)
    
    return wl / norm_vector, wr / norm_vector


class Curvelet2D(Operator):
    """
    2D Fast Discrete Curvelet Transform

    :param model : :obj:`Vector`
        2D domain vector
    :param finest_curvelet : :obl:`bool`
        Use curvelets at the finest level instead of wavelets (False by default)
    :param num_scales : :obj:`int`, optional
        Number of scales including the coarsest wavelet level (ceil(log2(min(M,N))-3 by default)
    :param num_angles_coarse : :obj:`int`, optional
        Number of angles at the second coarsest wavelet level; must be >= 8 and multiple of 4 (16 by default)
    :param is_real : :obj:`bool`, optional
        Use the real-valued transform (False by default)

    Note
    ----
    Porting by Francesco Picetti based on the code of Emmanuel Candes, 2003--2004
    """
    
    def __init__(self, model, num_scales=None, num_angles_coarse=16, finest_curvelet=False, is_real=False):
        
        assert model.ndim == 2, 'model has to be a 2D Vector'
        
        self.N1, self.N2 = model.shape
        
        self.num_scales = num_scales if num_scales is not None else ceil(log2(min(N1, N2)) - 3)
        
        assert num_angles_coarse >= 8, 'num_angles_coarse has to be >= 8'
        assert num_angles_coarse % 4 == 0, 'num_angles_coarse has to be multiple of 4'
        self.num_angles_coarse = num_angles_coarse
        
        self.finest_curvelet = finest_curvelet
        self.is_real = is_real
        
        # data structure
        self.num_angles = np.insert(
            self.num_angles_coarse * 2 ** (np.ceil((self.num_scales - np.arange(self.num_scales, 1, -1)) / 2)), 0,
            1).astype(int)
        
        if not self.finest_curvelet:
            self.num_angles[self.num_scales] = 1
        
        self.C = [None] * self.num_scales
        for s in range(self.num_scales):
            self.C[s] = [None] * self.num_angles[s]
        
        self.scales = np.arange(self.num_scales, 1, -1) if self.finest_curvelet else np.arange(self.num_scales - 1, 1,
                                                                                               -1)
        
        self.num_quad = 2 if self.is_real else 4
        self.num_angles_per_quad = self.num_angles / 4
        
        super(Curvelet2D, self).__init__(domain=VectorBaseIC(np.zeros(model.shape, dtype=np.complex)),
                                         range=VectorBaseIC(np.zeros(shape=dims_fft, dtype=np.complex)))
    
    def __str__(self):
        return 'Curvelet'
    
    def _compute_filters(self, m1, m2):
        window_length_1 = floor(2 * m1) - floor(m1) - 1
        window_length_2 = floor(2 * m2) - floor(m2) - 1
        coord_1 = np.linspace(0, 1, num=window_length_1, endpoint=True)
        coord_2 = np.linspace(0, 1, num=window_length_2, endpoint=True)
        wl_1, wr_1 = _fdct_wrapping_window(coord_1)
        wl_2, wr_2 = _fdct_wrapping_window(coord_2)
        lowpass_1 = np.concatenate((wl_1, np.ones(2 * floor(m1) + 1), wr_1))
        lowpass_2 = np.concatenate((wl_2, np.ones(2 * floor(m2) + 1), wr_2))
        
        lowpass = lowpass_1.conj().T @ lowpass_2
        hipass = np.sqrt(1 - lowpass ** 2)
        return lowpass, hipass
    
    def forward(self, add, model, data):
        self.checkDomainRange(model, data)
        if not add:
            data.zero()
        modelNd = model.getNdArray()
        dataNd = data.getNdArray()
        
        # Loop: pyramidal scale decomposition
        M1 = self.N1 / 3
        M2 = self.N2 / 3
        
        if self.finest_curvelet:
            pass
        else:
            # last scale
            X = _fft_direct(modelNd)
            
            M1, M2 = M1 / 2, M2 / 2
            l1 = np.arange(-floor(2 * M1), floor(2 * M1)) + ceil((self.N1 + 1) / 2)
            l2 = np.arange(-floor(2 * M2), floor(2 * M2)) + ceil((self.N2 + 1) / 2)
            lpf, hpf = self._compute_filters(M1 / 2, M2 / 2)
            
            Xlow = X[l1, l2] * lpf
            Xhi = X.copy()
            Xhi[l1, l2] *= hpf
            
            C = self.C.copy()
            
            C[self.num_scales - 1][0] = _fft_inverse(Xhi)
            if self.is_real:
                C[self.num_scales - 1][0] = C[self.num_scales - 1][0].real
        
        for j in self.scales:
            M1 /= 2
            M2 /= 2
            Xhi = Xlow.copy()
            
            lpf, hpf = self._compute_filters(M1, M2)
            l1 = np.arange(-floor(2 * M1), floor(2 * M1)) + floor(4 * M1) + 1
            l2 = np.arange(-floor(2 * M2), floor(2 * M2)) + floor(4 * M2) + 1
            
            Xlow = Xlow[l1, l2]
            Xhi[l1, l2] = Xlow * hpf
            Xlow *= lpf
            
            # loop: angular decomposition
            l = 0
            for quadrant in range(self.num_quad):
                M_horiz = M2 * (quadrant % 2 == 1) + M1 * (quadrant % 2 == 0)
                M_vert = M1 * (quadrant % 2 == 1) + M2 * (quadrant % 2 == 0)
                
                wedge_ticks_left = np.round(
                    np.linspace(0, 0.5, num=2 * self.num_angles_per_quad[j]) * 2 * floor(4 * M_horiz) + 1)
                wedge_ticks_right = 2 * floor(4 * M_horiz) + 2 - wedge_ticks_left
                wedge_ticks = np.concatenate((wedge_ticks_left, np.flip(wedge_ticks_right)))
                if not self.num_angles_per_quad[j] % 2:
                    wedge_ticks = wedge_ticks[:-1]
                wedge_endpoints = wedge_ticks[1:2:-1]
                wedge_midpoints = (wedge_endpoints[:-1] + wedge_endpoints[1:]) / 2
                
                # left corner wedge
                l += 1
                first_wedge_endpoint_vert = round(2 * floor(4 * M_vert) / (2 * self.num_angles_per_quad) + 1)
                length_corner_wedge = floor(4 * M_vert) - floor(M_vert) + ceil(first_wedge_endpoint_vert / 4)
                Y_corner = np.arange(length_corner_wedge)
                XX, YY = np.meshgrid(np.arange(2 * floor(4 * M_horiz) + 1), Y_corner)
                
                width_wedge = wedge_endpoints[1] + wedge_endpoints[0] - 1
                slope_wedge = (floor(4 * M_horiz) + 1 - wedge_endpoints[0]) / floor(4 * M_vert)
                left_line = round(2 - wedge_endpoints[0] + slope_wedge * Y_corner)
                
                [wrapped_data, wrapped_XX, wrapped_YY] = deal(zeros(length_corner_wedge, width_wedge));
        
        return
    
    def adjoint(self, add, model, data):
        self.checkDomainRange(model, data)
        if not add:
            model.zero()
        modelNd = model.getNdArray()
        dataNd = data.getNdArray()
        # here we need to separate the computation and use np.take for handling nfft > model.shape
        temp = np.fft.ifftn(dataNd, s=self.nfft, axes=self.axes, norm='ortho')
        for a in self.axes:
            temp = np.take(temp, range(self.domain.shape[a]), axis=a)
        modelNd += temp
        return
