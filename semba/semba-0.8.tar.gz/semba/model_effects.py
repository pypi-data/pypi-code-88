#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEM model with mean component. Bayesian version."""
from .matrix_variate_normal import MatrixVariateNormal
from semopy import ModelEffects as fModelEffects
from numpyro import distributions as dists
from .model_mixin import ModelMixin
from .solver import solve
import jax.numpy as jnp
import numpyro as pyro
from . import algebra

class ModelEffects(ModelMixin, fModelEffects):

    def model(self):
        """
        Evaluate Model.

        Returns
        -------
        dist : pyro.distribtuions.Distribution
            Distribution of the data.
        z : jax.ndarray
            Data sample.

        """
        mxs = self.sample_matrices()
        mx_lambda = mxs['Lambda']
        mx_beta = mxs['Beta']
        mx_psi = mxs['Psi']
        mx_theta = mxs['Theta']
        mx_gamma1 = mxs['Gamma1']
        mx_gamma2 = mxs['Gamma2']
        mx_d = mxs['D']
        mx_k = pyro.sample('K', dists.HalfNormal())
        p = mx_gamma1.shape[-1]
        mx_g = pyro.sample('G', dists.Normal(jnp.zeros((p, 1))))
        t, sigma = algebra.calc_sigma(mx_beta, mx_lambda, mx_psi, mx_theta)
        rowcov = algebra.calc_l(sigma, mx_d, mx_k)
        colcov_diag = algebra.calc_t_diag(sigma, mx_d, mx_k)
        colcov_diag = colcov_diag / jnp.trace(rowcov)
        mean = algebra.calc_mean(mx_gamma1, mx_gamma2, mx_g, t)
        dist = MatrixVariateNormal(loc=mean, rowcov=rowcov,
                                   colcov_diag=colcov_diag)
        z = pyro.sample('Z', dist)
        return dist, z


    def fit(self, data=None, cov=None, k=None,  group=None, solver='NUTS',
            num_warmup=None, num_samples=None, num_chains=1,
            chains_mode='best', seed=0, **kwargs):
        """
        Fit model to data.

        Parameters
        ----------
        data : pd.DataFrame, optional
            Data with columns as variables. The default is None.
        cov : pd.DataFrame, optional
            Pre-computed covariance/correlation matrix. The default is None.
        group : str, optional
            Groups of size > 1 to center across. The default is None.
        solver : str, optional
            Optimizaiton method. Currently MCMC approaches are available.
            The default is 'NUTS'.
        num_warmup : int, optional
            Number of warmup samples in MCMC. If None, then it is determined
            heuristically as num_samples // 5. The default is None.
        num_samples : int, optional
            Number of samples in MCMC. If None, then it is determined
            as number of parameters times 30. The default is None.
        num_chains : int, optional
            Number of chains in MCMC. The default is 1.
        chains_mode : str, optional
            If "best", then only the best in terms of loglikelihood chain is
            used for parameter estimatation. If "mean" (the default Pyro 
            behavior), then estimates are computed as a mean of joined chains.
            "Best" handles local minima problem much better. The default is
            "best".
        seed : int, optional
            Seed for random number generator. The default is 0.

        Raises
        ------
        Exception
            Rises when attempting to use FIML in absence of full data.

        Returns
        -------
        SolverResult
            Information on optimization process.

        """
        self.load(data=data, cov=cov, group=group, k=k)
        self.load_ml()
        self.mx_s = jnp.clip(self.mx_s, 0.0, jnp.inf)
        if not hasattr(self, 'mx_data'):
            raise Exception('Full data must be supplied.')
        if data is not None or cov is not None:
            self.convert_model()
        mod = pyro.handlers.condition(self.model, 
                                      data={'Z': self.mx_data_transformed,
                                            'G': self.mx_g,
                                            'K': self.mx_s})
        res = solve(self, mod, solver=solver, num_samples=num_samples,
                    num_warmup=num_warmup, num_chains=num_chains, seed=seed,
                    mode=chains_mode)
        self.last_result = res
        return res