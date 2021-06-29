"""
======================
Basic Usage of powspec
======================

"""
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_path = '_static/demo.png'
import astropy.units as u
from astropy.convolution import Gaussian2DKernel
from astropy.visualization import quantity_support

import numpy as np
from powspec.powspec import power_spectral_density
from powspec.utils.generator import gen_pkfield, gen_psffield


quantity_support()

# %%
# Create fake Gaussian field images
# ---------------------------------
#
# Create a list of fake images with different P(k)
#


res = 1 * u.arcmin
alphas = [-1, -2, -3]
images = []
for alpha in alphas:
    images.append(
        gen_pkfield(npix=1024, alpha=alpha, fknee=0.1 / u.arcmin, res=res) * u.MJy
    )

# %%
# Compute P(k)
# ------------
#
# Compute power spectra of each images
#

powspecs = []
for image in images:
    powspec, k = power_spectral_density(image, res=res)
    powspecs.append(powspec)


k_mid = np.mean(u.Quantity([k[1:], k[:-1]]), axis=0)

# %%
# Plots
# -----

fig = plt.figure()
gs = fig.add_gridspec(ncols=2, nrows=len(alphas))
ax_pk = fig.add_subplot(gs[:, 0])

for i, (image, powspec, alpha) in enumerate(zip(images, powspecs, alphas)):

    ax_pk.loglog(k_mid.to(u.arcmin ** -1), powspec.to(u.MJy ** 2 / u.arcmin ** 2), label=alpha)
    ax = fig.add_subplot(gs[i, 1])
    ax.imshow(image.value, origin="lower")

plt.show()

# %%
# Create PSF field image
# ----------------------
#
# Create a fake catalog of sources

n_pix = 1024
n_sources = 1024*5
positions = np.random.uniform(0, n_pix, size=(2, n_sources))
fluxes = np.random.uniform(1, 10, n_sources)
sigma = 10 # pixels

image = gen_psffield(positions, fluxes, n_pix, kernel=Gaussian2DKernel(sigma), factor=4) * u.Jy / u.beam

# %%
# Compute P(k)
# ------------
#
# Compute power spectra of each images
#
powspec, k = power_spectral_density(image, res=res, range='tight', bins='auto')

k_mid = np.mean(u.Quantity([k[1:], k[:-1]]), axis=0)

# %%
# Plots
# -----

fig, axes = plt.subplots(ncols=2)
axes[0].imshow(image.value, origin='lower')
axes[1].loglog(k_mid, powspec)

def gaussian_pk(k, sigma):
    return np.exp(- (np.pi * k)**2 * (2 * sigma**2) * 2 )

axes[1].plot(k_mid, gaussian_pk(k_mid, sigma * res) * powspec.max())
axes[1].set_ylim(np.min(powspec), np.max(powspec))

fig.show()
