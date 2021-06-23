#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conventional SEM model without mean components. Bayesian version."""
from numpyro import distributions as dists
from semopy import ModelMeans as fModelMeans
from .model_mixin import ModelMixin
from .solver import solve
import jax.numpy as jnp
import numpyro as pyro
from . import algebra

class ModelMeans(ModelMixin, fModelMeans):

    def model(self):
        """
        Evaluate Model.

        Returns
        -------
        None.

        """
        mxs = self.sample_matrices()
        mx_lambda = mxs['Lambda']
        mx_beta = mxs['Beta']
        mx_psi = mxs['Psi']
        mx_theta = mxs['Theta']
        mx_gamma1 = mxs['Gamma1']
        mx_gamma2 = mxs['Gamma2']
        mx_g = self.mx_g
        t, sigma = algebra.calc_sigma(mx_beta, mx_lambda, mx_psi, mx_theta)
        mean = algebra.calc_mean(mx_gamma1, mx_gamma2, mx_g, t)
        pyro.sample('Z', dists.MultivariateNormal(loc=mean.T, 
                                                  covariance_matrix=sigma))

    def fit(self, data=None, cov=None, solver='NUTS',
            groups=None, num_warmup=None, num_samples=None, num_chains=1,
            **kwargs):
        """
        Fit model to data.

        Parameters
        ----------
        data : pd.DataFrame, optional
            Data with columns as variables. The default is None.
        cov : pd.DataFrame, optional
            Pre-computed covariance/correlation matrix. The default is None.
        solver : str, optional
            Optimizaiton method. Currently MCMC approaches are available.
            The default is 'NUTS'.
        groups : list, optional
            Groups of size > 1 to center across. The default is None.
        num_warmup : int, optional
            Number of warmup samples in MCMC. If None, then it is determined
            heuristically as num_samples // 5. The default is None.
        num_samples : int, optional
            Number of samples in MCMC. If None, then it is determined
            as number of parameters times 30. The default is None.
        num_chains : int, optional
            Number of chains in MCMC. The default is 1.

        Raises
        ------
        Exception
            Rises when attempting to use FIML in absence of full data.

        Returns
        -------
        SolverResult
            Information on optimization process.

        """
        self.load(data=data, cov=cov, groups=groups)
        if data is not None or cov is not None:
            self.convert_model()
        mod = pyro.handlers.condition(self.model, 
                                      data={'Z': self.mx_data,
                                            'G': self.mx_g})
        res = solve(self, mod, solver=solver, num_samples=num_samples,
                    num_warmup=num_warmup, num_chains=num_chains)
        self.last_result = res
        return res