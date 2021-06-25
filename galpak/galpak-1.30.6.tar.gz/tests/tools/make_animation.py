from galpak import GalPaK3D, MUSEWFM
from os import pardir
from os.path import abspath, dirname, join

# filename = 'contsubCube_Hb_MUSE_J223256.08-603414.17_z0.56'
filename = 'contsubCube_O3_MUSE_J223256.08-603414.17_z0.56'

root_folder = abspath(join(dirname(abspath(__file__)), pardir))
fits_folder = join(root_folder, 'data/input')
fits_file = join(fits_folder, filename + '.fits')

glpk3d = GalPaK3D(fits_file, seeing=0.7, instrument=MUSEWFM(lsf_fwhm=2.519/1e4))
glpk3d.run_mcmc(max_iterations=10000, verbose=True)

# ANIMATION
glpk3d.film_images(filename, frames_skipped=5)

glpk3d.save(filename, overwrite=True)