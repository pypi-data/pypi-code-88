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
    images.append(gen_pkfield(npix=1024, alpha=alpha, fknee=0.1 / u.arcmin, res=res) * u.MJy)

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

n_pix = 512
n_sources = 128 * 5
positions = np.random.uniform(0, n_pix, size=(2, n_sources))
fluxes = np.random.uniform(1, 10, n_sources)
sigma = 10  # pixels

images = [
    gen_psffield(positions, fluxes, n_pix, kernel=Gaussian2DKernel(sigma)) * u.Jy / u.beam,
    gen_psffield(positions, fluxes, n_pix, kernel=Gaussian2DKernel(sigma, x_size=n_pix // 2)) * u.Jy / u.beam,
]
labels = ["", "x_size"]


# %%
# Compute P(k)
# ------------
#
# Compute power spectra of each images
#
powspecs = []
for image in images:
    powspec, k = power_spectral_density(image, res=res, range="tight", bins=n_pix // 2)
    powspecs.append(powspec)

# powspec, k = power_spectral_density(image, res=res, range='tight', bins='auto')

k_mid = np.mean(u.Quantity([k[1:], k[:-1]]), axis=0)

# %%
# Plots
# -----
def gaussian_pk(k, sigma):
    return np.exp(-((np.pi * k) ** 2) * (2 * sigma ** 2) * 2)


fig = plt.figure()
gs = fig.add_gridspec(ncols=2, nrows=len(images))
# ax_pk = fig.add_subplot(gs[:, 0])
ax_pk = fig.add_subplot(gs[: len(images) // 2, 0])
ax_pk_ratio = fig.add_subplot(gs[len(images) // 2 :, 0])

for i, (image, powspec, label) in enumerate(zip(images, powspecs, labels)):
    ax_pk.loglog(k_mid.to(u.arcmin ** -1), powspec.to(u.Jy ** 2 / u.beam ** 2 * u.arcmin ** 2), label=label)
    ax_pk_ratio.semilogx(
        k_mid.to(u.arcmin ** -1),
        powspec.to(u.Jy ** 2 / u.beam ** 2 * u.arcmin ** 2) / gaussian_pk(k_mid, sigma * res),
        label=label,
    )
    ax = fig.add_subplot(gs[i, 1])
    ax.imshow(image.value, origin="lower")

ax_pk.plot(
    k_mid.to(u.arcmin ** -1),
    gaussian_pk(k_mid, sigma * res) * (u.Jy ** 2 / u.beam ** 2 * u.arcmin ** 2),
    linestyle="--",
    label="analytical",
)
ax_pk.legend()
ax_pk.set_ylim(1e-15, np.max(fluxes * 2 * np.pi * sigma ** 2) ** 2)
ratio = np.sum((2 * np.pi * sigma ** 2 * fluxes * u.Jy / u.beam) ** 2) * res ** 2 / n_pix ** 2
ax_pk_ratio.axhline(ratio, linestyle="--", label="analytical")
ax_pk_ratio.legend()
ax_pk_ratio.set_ylim(0, 3 * ratio)
fig.show()
