"""TBW."""
import numpy as np
import pylandau                            # todo ?!?  works only with numpy>=1.16.2 & Cython>=0.29.7
import matplotlib.pyplot as plt


def simple_fit_to_data(data, label, scale_factor):
    """Fit without fit error estimation.

    For correct fit errors check the advanced example.
    Bound should be defined. Eta has to be > 1.
    """
    from scipy.optimize import curve_fit

    # Fit with constrains
    func = pylandau.langau      # !!! pylandau.lanDau  VERSUS  pylandau.lanGau
    # func = pylandau.langau_pdf      # !!! pylandau.lanDau  VERSUS  pylandau.lanGau
    # func = pylandau.landau_pdf

    start, end = None, 5000
    step = 1
    y = data[:, 1][start:end:step]
    mpv, eta = 1., 1.
    sigma = 1.
    a = np.clip([max(y) - 50.], 1., max(y) - 50.)[0]

    # scale_factor = 1.  # 16.
    while True:
        x = data[:, 0][start:end:step] * 1000 * scale_factor
        coeff, pcov = curve_fit(func, x, y, p0=(mpv, eta, sigma, a),
                                bounds=([1., 1., 1.e-3, 1.], [100., 10., 10., 500.]))

        # coeff, pcov = curve_fit(func, x, y, p0=(mpv, eta, sigma), bounds=(1, 10000))  # , # sigma=yerr, absolute_sigma=True,

        if coeff[0] > 1.01 and coeff[1] > 1.01 and coeff[2] > 1.:       # TODO calc fitness , check if below a limit
            break
        else:
            if scale_factor < 32.:
                scale_factor *= 2
            else:
                break
            # mpv *= scale_factor
            # eta *= scale_factor
            # sigma *= scale_factor

    # print('coeff: ', coeff)                               # TODO pcov ??!?!?
    # print('scale_factor: ', scale_factor)
    # print('pcov:\n', pcov)
    # Plot
    # plt.figure()
    # plt.errorbar(x, y, np.sqrt(pylandau.langau(x, *coeff)), fmt=".")
    # plt.plot(x, y, '.', label=label+' MeV data')
    # plt.plot(x, func(x, *coeff), '-', label=label+' MeV fit')
    # plt.show()

    return (*coeff), scale_factor


def fit_landau_to_data(data):
    """TBW."""
    x = data[:, 0]
    y = data[:, 1]
    # Fit the data with numerical exact error estimation
    # Taking into account correlations

    # values, errors, m = fit_langau_migrad(x,
    values, m = fit_langau_migrad(x,
                                  y,
                                  p0=[x.shape[0] / 2., 10., 10., np.max(y)],
                                  limit_mpv=(10., 100.),
                                  limit_eta=(2., 20.),
                                  limit_sigma=(2., 20.),
                                  limit_a=(500., 1500.))

    # Plot fit result
    yerr = np.sqrt(y)

    plt.figure()
    plt.errorbar(x, y, yerr, fmt='.')
    plt.plot(x, pylandau.langau(x, *values), '-', label='Fit:')
    plt.legend(loc=0)

    # Show Chi2 as a function of the mpv parameter
    # The cut of the parabola at dy = 1 defines the error
    # https://github.com/iminuit/iminuit/blob/master/tutorial/tutorial.ipynb
    plt.figure()
    m.draw_mnprofile('mpv', subtract_min=False)

    # Show contour plot, is somewhat correlation / fit confidence
    # of these two parameter. The off regions are a hint for
    # instabilities of the langau function
    plt.figure()
    m.draw_mncontour('mpv', 'sigma', nsigma=3)

    plt.show()


def fit_langau_migrad(x, y, p0, limit_mpv, limit_eta, limit_sigma, limit_a):
    """Advanced fitting example that calculated the MPV errors correctly.

    For this iminuit is used plus an additional step with minos to get
    asymmetric correct errors.

    Thus iminuit has to be installed (pip install iminuit).

    Further info on minuit and the original implementation:
    http://seal.web.cern.ch/seal/documents/minuit/mnusersguide.pdf
    """
    import iminuit

    def minimize_me(mpv, eta, sigma, a):
        chi2 = np.sum(np.square(y - pylandau.langau(x, mpv, eta, sigma, a).astype(float)) /
                      np.square(yerr.astype(float)))
        return chi2 / (x.shape[0] - 5)  # devide by NDF

    # Prefit to get correct errors
    yerr = np.sqrt(abs(y))  # Assume error from measured data
    yerr[y < 1] = 1
    m = iminuit.Minuit(minimize_me,
                       mpv=p0[0],
                       limit_mpv=limit_mpv,
                       error_mpv=1,
                       eta=p0[1],
                       error_eta=0.1,
                       limit_eta=limit_eta,
                       sigma=p0[2],
                       error_sigma=0.1,
                       limit_sigma=limit_sigma,
                       a=p0[3],
                       error_a=1,
                       limit_a=limit_a,
                       errordef=1,
                       print_level=2)
    m.migrad()

    if not m.get_fmin().is_valid:
        raise RuntimeError('Fit did not converge')

    # # Main fit with model errors
    # yerr = np.sqrt(pylandau.langau(x,
    #                                mpv=m.values['mpv'],
    #                                eta=m.values['eta'],
    #                                sigma=m.values['sigma'],
    #                                A=m.values['a']))  # Assume error from measured data
    # yerr[y < 1] = 1
    #
    # m = iminuit.Minuit(minimize_me,
    #                    mpv=m.values['mpv'],
    #                    limit_mpv=limit_mpv,
    #                    error_mpv=1,
    #                    eta=m.values['eta'],
    #                    error_eta=0.1,
    #                    limit_eta=limit_eta,
    #                    sigma=m.values['sigma'],
    #                    error_sigma=0.1,
    #                    limit_sigma=limit_sigma,
    #                    a=m.values['a'],
    #                    error_a=1,
    #                    limit_a=limit_a,
    #                    errordef=1,
    #                    print_level=2)
    # m.migrad()

    fit_values = m.values

    values = np.array([fit_values['mpv'],
                       fit_values['eta'],
                       fit_values['sigma'],
                       fit_values['a']])

    # m.hesse()
    #
    # m.minos()
    # minos_errors = m.get_merrors()
    #
    # if not minos_errors['mpv'].is_valid:
    #     print('Warning: MPV error determination with Minos failed! You can still use Hesse errors.')
    #
    # errors = np.array([(minos_errors['mpv'].lower, minos_errors['mpv'].upper),
    #                    (minos_errors['eta'].lower, minos_errors['eta'].upper),
    #                    (minos_errors['sigma'].lower, minos_errors['sigma'].upper),
    #                    (minos_errors['a'].lower, minos_errors['a'].upper)])
    #
    # return values, errors, m

    return values, m


def plot_landau():
    """TBW."""
    x = np.arange(0, 100, 0.01)
    plt.figure()
    for a, eta, mpv in ((1, 1, 10), (1, 2, 30), (0.5, 5, 50)):
        # Use the function that calculates y values when given array
        # plt.plot(x, pylandau.landau(x, mpv, eta, a), '-', label='mu=%1.1f, eta=%1.1f, A=%1.1f' % (mpv, eta, a))
        plt.plot(x, pylandau.landau_pdf(x, mpv, eta), '-', label='mu=%1.1f, eta=%1.1f' % (mpv, eta))

        # Use the function that calculates the y value given a x value, (e.g. needed for minimizers)
        xx = np.arange(0, 100, 1)
        # y = np.array([pylandau.get_landau(x_value, mpv, eta, a) for x_value in x])
        # plt.plot(x, y, 'r--', label='mu=%1.1f, eta=%1.1f, A=%1.1f' % (mpv, eta, a))
        y = np.array([pylandau.get_landau_pdf(x_value, mpv, eta) for x_value in xx])
        plt.plot(xx, y, '.', label='mu=%1.1f, eta=%1.1f' % (mpv, eta))

        # sigma = 10
        # plt.plot(x, pylandau.langau(x, mpv, eta, sigma), '--',
        #          label = 'mu=%1.1f, eta=%1.1f, sigma=%1.1f, A=%1.1f' % (eta, sigma, mpv, a))
        # plt.plot(x, pylandau.langau_pdf(x, mpv, eta, sigma), '--',
        #          label='mu=%1.1f, eta=%1.1f, sigma=%1.1f' % (eta, sigma, mpv))
    plt.legend(loc=0)
    # plt.show()


# def test_fit_landau():
#     """TBW."""
#     # Fake counting experiment with Landgaus distribution
#     np.random.seed(12345)
#     x = np.arange(100).astype(np.float)
#     y = pylandau.langau(x,
#                         mpv=30.,
#                         eta=5.,
#                         sigma=4.,
#                         A=1000.)
#     # Add poisson error
#     y += np.random.normal(np.zeros_like(y), np.sqrt(y))
#
#     # Fit the data with numerical exact error estimation
#     # Taking into account correlations
#     values, errors, m = fit_langau_migrad(x,
#                                           y,
#                                           p0=[x.shape[0] / 2., 10., 10., np.max(y)],
#                                           limit_mpv=(10., 100.),
#                                           limit_eta=(2., 20.),
#                                           limit_sigma=(2., 20.),
#                                           limit_a=(500., 1500.))
#
#     # Plot fit result
#     yerr = np.sqrt(pylandau.langau(x, *values))
#
#     plt.figure()
#     plt.errorbar(x, y, yerr, fmt='.')
#     plt.plot(x, pylandau.langau(x, *values), '-', label='Fit:')
#     plt.legend(loc=0)
#     # plt.show()
#
#     # Show Chi2 as a function of the mpv parameter
#     # The cut of the parabola at dy = 1 defines the error
#     # https://github.com/iminuit/iminuit/blob/master/tutorial/tutorial.ipynb
#     # plt.clf()
#     plt.figure()
#     m.draw_mnprofile('mpv', subtract_min=False)
#     # plt.show()
#
#     # Show contour plot, is somewhat correlation / fit confidence
#     # of these two parameter. The off regions are a hint for
#     # instabilities of the langau function
#     # plt.clf()
#     plt.figure()
#     m.draw_mncontour('mpv', 'sigma', nsigma=3)
#     # plt.show()


def landau_gauss_crosscheck():
    """Plot the Landau Gauss convolution (Langau) and cross check with convolution with scipy."""
    from scipy.ndimage.filters import gaussian_filter1d

    mpv, eta, sigma, a = 10, 1, 1e-3, 1
    x = np.arange(0, 50, 0.01)
    y = pylandau.landau(x, mpv=mpv, eta=eta, A=a)
    y_gconv = gaussian_filter1d(y, sigma=sigma / 0.01)
    # Scaled means that the resulting Landau*Gauss function maximum is A at mpv
    # Otherwise the underlying Landau function before convolution has the
    # function maximum A at mpv
    y_gconv_2 = pylandau.langau(x, mpv, eta, sigma, a, scale_langau=False)
    y_gconv_3 = pylandau.langau(x, mpv, eta, sigma, a, scale_langau=True)

    plt.figure()
    plt.plot(x, y, label='Landau')
    plt.plot(x, y_gconv_2, label='Langau')
    plt.plot(x, y_gconv, '--', label='Langau Scipy')
    plt.plot(x, y_gconv_3, label='Langau scaled')
    plt.legend(loc=0)
    plt.show()


def integrate_landau():
    """Check the integral of landau PDF ~ 1 with scipy numerical integration."""
    mu, eta, sigma = 10, 1, 3
    from scipy import integrate

    y, err = integrate.quad(pylandau.get_landau_pdf, 0, 10000, args=(mu, eta))
    print('Integral of Landau PDF:', y, '  error:', err)

    y, err = integrate.quad(pylandau.get_gauss_pdf, 0, 10000, args=(mu, sigma))
    print('Integral of Gauss PDF:', y, '  error:', err)

    y, err = integrate.quad(pylandau.get_langau_pdf, -10000, 10000, args=(mu, eta, sigma))
    print('Integral of Landau + Gauss (Langau) PDF:', y, '  error:', err)


def fwhm(x, y):
    """Determine full-with-half-maximum of a peaked set of points, x and y.

    Assumes that there is only one peak present in the datasset.  The function
    uses a spline interpolation of order k.

    http://stackoverflow.com/questions/10582795/finding-the-full-width-half-maximum-of-a-peak
    """
    from scipy.interpolate import splrep, sproot

    class MultiplePeaks(Exception):
        pass

    class NoPeaksFound(Exception):
        pass

    half_max = np.amax(y) / 2.0
    s = splrep(x, y - half_max)
    roots = sproot(s)

    if len(roots) > 2:
        raise MultiplePeaks("The dataset appears to have multiple peaks, and "
                            "thus the FWHM can't be determined.")
    elif len(roots) < 2:
        raise NoPeaksFound("No proper peaks were found in the data set; likely "
                           "the dataset is flat (e.g. all zeros).")
    else:
        return roots[0], roots[1]


def plot_landau_with_fwhm():
    """Plot Landau distributions with FWHM and MPV."""
    x = np.arange(0, 100, 0.01)
    plt.figure()
    for a, eta, mpv in ((1, 1, 10), (1, 2, 30), (0.5, 5, 50)):
        y = pylandau.landau(x, mpv, eta, a)
        plt.plot(x, y, label='A=%d, mpv=%d, eta=%d' % (a, mpv, eta))
        x_fwhm_1, x_fwhm_2 = fwhm(x, y)
        plt.plot([x_fwhm_1, x_fwhm_2], [np.max(y) / 2., np.max(y) / 2.],
                 label='FWHM: %1.1f' % np.abs(x_fwhm_1 - x_fwhm_2))
        plt.plot([mpv, mpv], [0., np.max(y)], label='MPV: %1.1f' % mpv)
    plt.legend(loc=0)
    # plt.show()


def simple_fit():
    """Fit without fit error estimation.

    For correct fit errors check the advanced example.
    Bound should be defined. Eta has to be > 1.
    """
    np.random.seed(12345)
    from scipy.optimize import curve_fit

    # Create fake data with possion error
    mpv, eta, sigma, a = 30, 5, 4, 1000
    x = np.arange(0, 100, 0.5)
    y = pylandau.langau(x, mpv, eta, sigma, a)
    yerr = np.random.normal(np.zeros_like(x), np.sqrt(y))
    yerr[y < 1] = 1
    y += yerr

    # Fit with constrains
    coeff, pcov = curve_fit(pylandau.langau, x, y, sigma=yerr, absolute_sigma=True, p0=(mpv, eta, sigma, a),
                            bounds=(1, 10000))

    # Plot
    plt.figure()
    plt.errorbar(x, y, np.sqrt(pylandau.langau(x, *coeff)), fmt=".")
    plt.plot(x, pylandau.langau(x, *coeff), "-")
    # plt.show()
