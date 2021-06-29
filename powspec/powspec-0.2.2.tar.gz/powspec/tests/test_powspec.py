import pytest
import numpy as np
import numpy.testing as npt


def test_powspec():
    from ..powspec import power_spectral_density as powspec
    from ..utils.generator import gen_pkfield, Pk

    npix = 128
    res = 50
    img = gen_pkfield(npix=npix, res=res)
    _powspec, bin_edges = powspec(img, res=res, bins=npix)
    bin_centers = (bin_edges[1:] + bin_edges[:-1]) / 2

    def gen_pk(npix, res):
        img = gen_pkfield(npix=npix, res=res)
        _powspec, _ = powspec(img, res=res, bins=npix)
        return _powspec

    realization = list(map(lambda i: gen_pk(npix, res), range(100)))
    mean_Pk = np.mean(realization, axis=0)
    std_Pk = np.std(realization, axis=0)

    # plt.close('all')
    # plt.loglog(bin_centers[1:], mean_Pk[1:])
    # plt.loglog(bin_centers[1:], mean_Pk[1:]+std_Pk[1:])
    # plt.loglog(bin_centers[1:], mean_Pk[1:]-std_Pk[1:])
    # plt.loglog(bin_centers, P(bin_centers) / res**2)

    assert np.all((mean_Pk[1:] - Pk(bin_centers[1:])) < std_Pk[1:])


def test_powspec_unit():
    import astropy.units as u

    from ..powspec import power_spectral_density as powspec
    from ..utils.generator import gen_pkfield

    npix = 1024
    nsub = 128
    alpha = -1  # For alpha=-3, the P(k) is dominated by the step edges...
    res = 2 * u.arcsec

    np.random.seed(1)

    img = gen_pkfield(npix=npix, res=res, alpha=alpha, fknee=1 / u.arcsec) * u.Jy

    with pytest.raises(AssertionError):
        # range must be a quantity
        powspec(img, res=res, range=(0, 1))

    bins = np.linspace(2, nsub // 2, nsub // 2 - 2) / (res * nsub)
    powspec_full, bin_full = powspec(img, res=res, bins=bins)

    # Test on sub image
    powspecs = u.Quantity(
        [
            powspec(img[i : i + nsub, j : j + nsub], res=res, bins=bins)[0]  # noqa: E203
            for i, j in np.random.randint(size=(128, 2), low=0, high=npix - nsub)
        ]
    ).to(u.Jy ** 2 / u.sr)

    # plt.close('all')
    # bin_centers = (bin_full[1:] + bin_full[:-1]) / 2
    # plt.loglog(bins[1:], powspec_full.to(u.Jy**2/u.sr), c='k')
    # plt.loglog(bins[1:], np.mean(powspecs, axis=0))
    # plt.loglog(bins[1:], np.mean(powspecs, axis=0) + np.std(powspecs, axis=0), linestyle='dashed')
    # plt.loglog(bins[1:], np.mean(powspecs, axis=0) - np.std(powspecs, axis=0), linestyle='dashed')
    # plt.loglog(bins, (P(bins, alpha=alpha, fknee=1/u.arcsec) / res **2 * u.Jy**2).to(u.Jy**2 / u.sr))

    assert np.all((np.mean(powspecs, axis=0) - powspec_full.to(u.Jy ** 2 / u.sr)) < np.std(powspecs, axis=0))


def test_crosspec():
    from ..powspec import power_spectral_density as powspec, cross_spectral_density as crosspec
    from ..utils.generator import gen_pkfield

    npix = 128
    res = 50
    img = gen_pkfield(npix=npix, res=res)
    _powspec, bin_pow = powspec(img, res=res, bins=npix)

    _crosspec, bin_cross = crosspec(img, img, res=res, bins=npix)

    npt.assert_equal(bin_pow, bin_cross)
    npt.assert_allclose(_powspec, _crosspec)

    # plt.close('all')
    # bin_centers = (bin_pow[1:] + bin_pow[:-1]) / 2
    # plt.loglog(bin_centers[1:], _powspec[1:])
    # plt.loglog(bin_centers[1:], _crosspec[1:])


@pytest.mark.parametrize(
    "bins,range,expected",
    [
        (4, None, (4, None)),
        (4, 100, (4, 100)),
        (4, "tight-linear", (np.linspace(0.1, 0.5, 5), None)),
        (4, "tight-log", (np.logspace(np.log10(0.1), np.log10(0.5), 5), None)),
    ],
)
def test_k_bin_edges(bins, range, expected):
    from ..powspec import k_bin_edges

    shape = (10, 5)
    result = k_bin_edges(shape, bins=bins, range=range)
    npt.assert_equal(result[0], expected[0])
    assert result[1] == expected[1]
