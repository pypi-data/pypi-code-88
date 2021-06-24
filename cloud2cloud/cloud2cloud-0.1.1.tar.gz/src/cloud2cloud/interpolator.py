import numpy as np
from scipy import spatial


SMALL = 1e-16
class CloudInterpolator:
	def __init__(self, source, target, limitsource=None, stencil=4, function=None):
		n_dim = len(source)
		if n_dim != len(target):
			print("Warning: source and target dim mismatch")
			pass #error "mismatch dims"

		n_points = source[0].size
		self.skipper = 1
		if limitsource is not None and n_points > limitsource:
			self.skipper = 1+(n_points-1)//limitsource

		if isinstance(source, np.ndarray):
			source = np.stack(source[:,::self.skipper], axis=1)
		else:
			source = np.stack([axe[::self.skipper] for axe in source], axis=1)
		target = np.stack(target, axis=1)
		kdtree = spatial.cKDTree(source)
		dists, self.index = kdtree.query(target, k=stencil)

		if stencil == 1:
			self.index = self.index[:,None]
			self.weight = np.ones((self.index.size, 1))
			return

		if function is not None:
			dists[...] = function(dists)
		dists[...] = np.reciprocal(np.maximum(dists, SMALL))
		dists /= np.sum(dists, axis=1)[:,None]
		self.weight = dists

	def interp(self, data):
		estimate = data[::self.skipper,...][self.index]
		estimate *= self.weight.reshape(*self.weight.shape, *[1]*(data.ndim-1))
		return np.sum(estimate, axis=1)


def cloud2cloud(source_xyz, source_val, target_xyz, verbose=False, **kwargs):
	*shp_sce, dim_sce = source_xyz.shape
	*shp_tgt, dim_tgt = target_xyz.shape
	shp_sce, shp_tgt = tuple(shp_sce), tuple(shp_tgt)
	shp_val = source_val.shape[len(shp_sce):]
	n_p_sce = np.prod(shp_sce)
	n_p_tgt = np.prod(shp_tgt)

	if verbose:
		if dim_sce != dim_tgt:
			print("Warning: source and target dim mismatch")
		if source_val.shape[:len(shp_sce)] != shp_sce:
			print("Warning: Source and data mismatch")
		print("dim_sce:", dim_sce)
		print("dim_tgt:", dim_sce)
		print("shp_sce:", shp_sce)
		print("shp_tgt:", shp_tgt)
		print("shp_val:", shp_val)
		print("n_points_sce:", n_p_sce)
		print("n_points_tgt:", n_p_tgt)

	source_val = source_val.reshape(n_p_sce, *shp_val)
	source_xyz = source_xyz.reshape(n_p_sce, dim_sce)
	target_xyz = target_xyz.reshape(n_p_tgt, dim_tgt)

	if verbose:
		print("new shp_sce:", source_xyz.shape)
		print("new shp_tgt:", target_xyz.shape)
		print("new shp_val:", source_val.shape)

	base = CloudInterpolator(source_xyz.T, target_xyz.T, **kwargs)
	if verbose and base.skipper > 1:
		print("skipper:", base.skipper)
	return base.interp(source_val).reshape(*shp_tgt, *shp_val)
