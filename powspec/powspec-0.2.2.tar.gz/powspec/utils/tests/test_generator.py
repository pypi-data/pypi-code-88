import numpy as np
import numpy.testing as npt


def test_Pk():
    from ..generator import Pk

    assert Pk(1, alpha=2, fknee=1) == 1
    assert np.all(Pk(np.arange(10), alpha=0, fknee=1) == np.ones(10))


def test_gen_pkfield():
    from ..generator import gen_pkfield

    np.random.seed(42)
    pkfield = gen_pkfield(npix=256, alpha=0, fknee=1, res=1)

    assert pkfield.shape == (256, 256)
    npt.assert_almost_equal(np.mean(pkfield), 0)
    npt.assert_almost_equal(np.std(pkfield), 1, decimal=3)


def test_gen_psffield():
    from ..generator import gen_psffield
    from astropy.convolution import Gaussian2DKernel

    np.random.seed(42)
    n_pix = 64
    n_sources = 3
    sigma = 2
    positions = np.random.uniform(n_pix // 5, n_pix * 4 // 5, size=(2, n_sources))

    m = gen_psffield(positions, shape=n_pix, kernel=None, factor=None)
    assert np.sum(m) == n_sources

    shape = (n_pix, n_pix)
    m = gen_psffield(positions, shape=shape, kernel=None, factor=None)
    assert np.sum(m) == n_sources

    m_f = gen_psffield(positions, shape=shape, kernel=None, factor=10)
    npt.assert_equal(m, m_f)

    m = gen_psffield(positions, shape=shape, kernel=Gaussian2DKernel(sigma), factor=None)
    npt.assert_almost_equal(np.log10(n_sources * 2 * np.pi * sigma ** 2), np.log10(m.sum()), decimal=4)

    m = gen_psffield(positions, shape=shape, kernel=Gaussian2DKernel(sigma), factor=10)
    npt.assert_almost_equal(np.log10(n_sources * 2 * np.pi * sigma ** 2), np.log10(m.sum()), decimal=4)

    def pixelated_gaussian(shape, center, sigma):
        """x, y bin edges"""
        from scipy.special import erf

        x = np.linspace(-0.5, shape[1] - 0.5, shape[1] + 1)
        y = np.linspace(-0.5, shape[0] - 0.5, shape[0] + 1)
        x, y = np.meshgrid(x, y)
        x1 = x[:-1, :-1]
        x2 = x[1:, 1:]
        y1 = y[:-1, :-1]
        y2 = y[1:, 1:]

        m = (
            1
            / (4 * (x2 - x1) * (y2 - y1))
            * (erf((x2 - center[0]) / (np.sqrt(2) * sigma[0])) - erf((x1 - center[0]) / (np.sqrt(2) * sigma[0])))
            * (erf((y2 - center[1]) / (np.sqrt(2) * sigma[1])) - erf((y1 - center[1]) / (np.sqrt(2) * sigma[1])))
            * (2 * np.pi * sigma[0] * sigma[1])
        )
        return m

    m_pix = np.sum([pixelated_gaussian(m.shape, center, (sigma, sigma)) for center in positions.T], axis=0)

    # Should be better
    npt.assert_almost_equal(m_pix, m, decimal=2)
    assert np.all(np.abs(m_pix - m) < 1e-1)

    fluxes = [1, 2, 3]
    m_f = gen_psffield(positions, fluxes, shape=shape, kernel=Gaussian2DKernel(sigma), factor=10)
    npt.assert_almost_equal(np.log10(2 * np.pi * sigma ** 2 * np.sum(fluxes)), np.log10(m_f.sum()), decimal=4)


def main():
    import matplotlib.pyplot as plt
    from astropy.convolution import Gaussian2DKernel
    from powspec.generator import gen_psffield

    plt.ion()

    def pixelated_gaussian(shape, center, sigma):
        """x, y bin edges"""
        from scipy.special import erf

        x = np.linspace(-0.5, shape[1] - 0.5, shape[1] + 1)
        y = np.linspace(-0.5, shape[0] - 0.5, shape[0] + 1)
        x, y = np.meshgrid(x, y)
        x1 = x[:-1, :-1]
        x2 = x[1:, 1:]
        y1 = y[:-1, :-1]
        y2 = y[1:, 1:]

        m = (
            1
            / (4 * (x2 - x1) * (y2 - y1))
            * (erf((x2 - center[0]) / (np.sqrt(2) * sigma[0])) - erf((x1 - center[0]) / (np.sqrt(2) * sigma[0])))
            * (erf((y2 - center[1]) / (np.sqrt(2) * sigma[1])) - erf((y1 - center[1]) / (np.sqrt(2) * sigma[1])))
            * (2 * np.pi * sigma[0] * sigma[1])
        )
        return m

    def centered_gaussian(shape, center, sigma):
        """x, y bin edges"""
        x = np.linspace(0, shape[1] - 1, shape[1])
        y = np.linspace(0, shape[0] - 1, shape[0])
        x, y = np.meshgrid(x, y)
        m = np.exp(-((x - center[0]) ** 2) / (2 * sigma[0] ** 2) - (y - center[1]) ** 2 / (2 * sigma[1] ** 2))
        return m

    n_pix = 11
    n_sources = 3
    np.random.seed(0)
    positions = np.random.uniform(1, n_pix - 1, size=(2, n_sources))

    shape = (n_pix, n_pix)

    # test = np.sum([centered_gaussian(shape, center, (1, 1)) for center in positions.T], axis=0)
    # pix_test = np.sum([pixelated_gaussian(shape, center, (1, 1)) for center in positions.T], axis=0)
    m = gen_psffield(positions, shape, kernel=Gaussian2DKernel(1), factor=4)

    plt.clf()
    plt.imshow(m, extent=(-0.5, shape[0] - 0.5, -0.5, shape[1] - 0.5), origin="lower")
    plt.scatter(*positions)
