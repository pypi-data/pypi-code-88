from bmtk.simulator.filternet.lgnmodel import movie
from bmtk.simulator.filternet.lgnmodel.spatialfilter import GaussianSpatialFilter
from bmtk.simulator.filternet.lgnmodel.temporalfilter import TemporalFilterCosineBump
import numpy as np

mv = movie.Movie(np.zeros((1001, 120, 240)), t_range=np.linspace(0.0, 1.0, 1001, endpoint=True))

# tf = TemporalFilterCosineBump(weights=[25.328, -10.10059], kpeaks=[59.0, 120.0], delays=[0.0, 0.0])
# kernel = tf.get_kernel(t_range=mv.t_range, threshold=0.0, reverse=True)
# print(tf.imshow())


gsf = GaussianSpatialFilter(translate=(-20, -10), sigma=(20, 10), rotation=0.0)
gsf.imshow(mv.row_range, mv.col_range)

