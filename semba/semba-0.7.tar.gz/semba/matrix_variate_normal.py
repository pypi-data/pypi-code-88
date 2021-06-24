#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Matrix-variate normal distribution for Pyro.

Note that it is effectively the same as MultivariateNormal, but takes advantage
of Kronecker structure of covariance matrix, hence making sampling much more
efficient: O(m^3 + n^3) vs O(m^3 n^3). If structure of one of the matrices
is diagonal, it can be further used to reduce computational burden.
"""
import jax.numpy as jnp
from jax import random
from jax.scipy.linalg import solve_triangular
from numpyro.distributions import constraints
from numpyro.distributions import Distribution
from numpyro.distributions.util import validate_sample, is_prng_key


real_matrix = constraints.independent(constraints.real, 2)
positive_vector = constraints.independent(constraints.positive, 1)

class MatrixVariateNormal(Distribution):
    arg_constraints = {'loc': real_matrix,
                       'colcov': constraints.positive_definite,
                       'rowcov': constraints.positive_definite,
                       'colcov_diag': positive_vector,
                       'rowcov_diag': positive_vector}
    support = real_matrix
    reparametrized_params = ['loc', 'colcov', 'rowcov',
                             'colcovdiag', 'rowcovdiag']

    def __init__(self, loc, rowcov=None, colcov=None,
                 rowcov_diag=None, colcov_diag=None,
                 validate_args=None):
        if colcov is not None:
            self.scale_tril_col = jnp.linalg.cholesky(colcov)
            self.scale_diag_col = None
        elif colcov_diag is not None:
            self.scale_diag_col = colcov_diag ** 0.5
        else:
            raise ValueError('One of `rowcov`, `rowcov_diag`, '
                             'must be specified.')
        if rowcov is not None:
            self.scale_tril_row = jnp.linalg.cholesky(rowcov)
            self.scale_diag_row = None
        elif rowcov_diag is not None:
            self.scale_diag_row = rowcov_diag ** 0.5
        else:
            raise ValueError('One of `colcov`, `colcov_diag`, '
                             'must be specified.')
        batch_shape = jnp.shape(loc)[:-2]
        event_shape = jnp.shape(loc)[-2:]
        self.loc = loc
        super(MatrixVariateNormal, self).__init__(batch_shape=batch_shape,
                                                  event_shape=event_shape,
                                                  validate_args=validate_args)

    def sample(self, key, sample_shape=()):
        assert is_prng_key(key)
        t = random.normal(key, shape=sample_shape + self.batch_shape + \
                          self.event_shape)
        if self.scale_diag_row is None:
            t = self.scale_tril_row @ t
        else:
            t = t * self.scale_diag_row[..., jnp.newaxis] 
        if self.scale_diag_col is None:
            t = t @ self.scale_tril_col
        else:
            t = t * self.scale_diag_col
        return self.loc + t


    @validate_sample
    def log_prob(self, value):
        n, m = self.event_shape    
        center = value - self.loc
        if self.scale_diag_row is None:
            center = solve_triangular(self.scale_tril_row, center, lower=True)
            logdet_r = m * jnp.log(jnp.diagonal(self.scale_tril_row, axis1=-2,
                                                axis2=-1)).sum(-1) * 2
        else:
            center = (1 / self.scale_diag_row)[..., jnp.newaxis] * center
            logdet_r = m * jnp.log(self.scale_diag_row).sum(-1) * 2
        if self.scale_diag_col is None:
            center = solve_triangular(self.scale_tril_col, center.T,
                                       lower=True)
            logdet_c = n * jnp.log(jnp.diagonal(self.scale_tril_col, axis1=-2,
                                                axis2=-1)).sum(-1) * 2
        else:
            center = center * (1 / self.scale_diag_col)
            logdet_c = n * jnp.log(self.scale_diag_col).sum(-1) * 2
        distance = jnp.einsum('ij,ij->', center, center)
        t = jnp.log(2 * jnp.pi) * n * m
        return -0.5* (distance + logdet_r + logdet_c + t)


    @staticmethod
    def infer_shapes(loc=(), **kwargs):
        batch_shape, event_shape = loc[:-2], loc[-2:]
        return batch_shape, event_shape
