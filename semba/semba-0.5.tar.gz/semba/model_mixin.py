#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pyro Mixin for semopy models."""
from semopy.inspector import inspect as semopy_inspect
from numpyro import distributions as dists
from .inspector import inspect
import jax
import jax.numpy as jnp
import numpyro as pyro
import numpy as npo
import logging

class ModelMixin(object):
    
    symb_prior_loading = "PRIOR_LOADING"
    symb_prior_covariance = "PRIOR_COVARIANCE"
    symb_prior_variance = "PRIOR_VARIANCE"
    symb_prior_covariance_latent = "PRIOR_COVARIANCE_LATENT"
    symb_prior_variance_latent = "PRIOR_VARIANCE_LATENT"
    symb_prior_param = "PRIOR"
    prior_loading = None
    prior_variance = None
    prior_covariance = None
    prior_covariance_latent = None
    prior_variance_latent = None
    priors = None


    def convert_model(self):
        """
        Create necessary structure for Pyro from a semopy model.

        Returns
        -------
        None.

        """
        names = self.inspect('mx', what='names')
        start = self.inspect('mx', what='start')
        params = self.parameters
        priors = self.priors
        lats = self.vars['latent']
        cov_mxs = dict()
        t = ((getattr(self, f'mx_{n}'), getattr(self, f'names_{n}')[0])
             for n in self.matrices_names
             if n.startswith(('psi', 'theta', 'd')))
        for mx, rows in t:
            cov_mxs[id(mx)] = set(rows.index(v) for v in rows if v in lats)
        cov_mult = npo.sqrt(npo.pi / 2)
        for name, p in params.items():
            if not p.active:
                continue
            dist = priors.get(name, None)
            if dist is None:
                cov = False
                for loc in p.locations:
                    inds = cov_mxs.get(id(loc.matrix), None)
                    if inds is not None:
                        cov = True
                        break
                if cov:
                    ind = loc.indices
                    lat = (ind[0] in inds) or (ind[1] in inds)
                    if not loc.symmetric:
                        ind = loc.indices
                        if lat:
                            if self.prior_variance_latent is not None:
                                dist = self.prior_variance_latent
                            else:
                                dist = dists.HalfNormal(cov_mult)
                        else:
                            if self.prior_variance is not None:
                                dist = self.prior_variance
                            else:
                                t = p.start ** 0.5 * cov_mult
                                dist = dists.HalfNormal(t)
                    else:
                        if not lat:
                            if self.prior_covariance is not None:
                                dist = self.prior_covariance
                            else:
                                dist = dists.Normal(p.start, scale=0.5)
                        else:
                            if self.prior_covariance_latent is not None:
                                dist = self.prior_covariance_latent
                            else:
                                dist = dists.Normal(p.start, scale=1)
                else:
                    if self.prior_loading:
                        dist = self.prior_loading
                    else:
                        if abs(p.start) < 1e-4:
                            dist = dists.Normal(p.start, scale=1.5)
                        else:
                            dist = dists.Normal(p.start, scale=0.5)
                priors[name] = dist
        mxs = dict()
        keys = list(priors.keys())
        for name, mx in start.items():
            inds_a = list()
            inds_b = list()
            inds_c = list()
            mx = jnp.array(mx.astype(float))
            for (a, b), val in npo.ndenumerate(names[name]):
                try:
                    c = keys.index(val)
                    inds_a.append(a)
                    inds_b.append(b)
                    inds_c.append(c)
                except ValueError:
                    continue
            mxs[name] = (mx, jax.ops.index[inds_a, inds_b], inds_c)
        self.jax_matrices = mxs
        self.built_priors = priors
    
    def sample_matrices(self):
        """
        Update matrices with stochastic samples.

        Analogous to update_matrices of semopy.
        Returns
        -------
        mxs : dict
            A mapping matrix_name->jnp.ndarray.

        """
        priors = self.built_priors
        matrices = self.jax_matrices
        samples = [pyro.sample(name, dist) for name, dist in priors.items()]
        mxs = dict()
        for name, (mx, inds, inds_c) in matrices.items():
            st = [samples[i] for i in inds_c]
            mxs[name] = jax.ops.index_update(mx, inds, st,
                                             indices_are_sorted=True,
                                             unique_indices=True)
        return mxs

    def operation_bound(self, operation):
        """
        Works through BOUND command.

        Sets bound constraints to parameters.
        Parameters
        ----------
        operation : Operation
            Operation namedtuple.

        Raise
        ----------
        SyntaxError
            When no starting value is supplied as an argument to START.
        ValueError
            When BOUND arguments are not translatable through FLOAT.
        KeyError
            When invalid parameter name is supplied.

        Returns
        -------
        None.

        """
        logging.warning('Bounds are unavailable for semopy-mc.')

    def operation_constraint(self, operation):
        """
        Works through CONSTRAINT command.

        Adds inequality and equality constraints.
        Parameters
        ----------
        operation : Operation
            Operation namedtuple.

        Raise
        ----------
        SyntaxError
            When no starting value is supplied as an argument to START.

        Returns
        -------
        None.

        """
        logging.warning('Constraints are unavailable for semopy-mc.')

    def operation_prior(self, operation):
        """
        Sets default prior for a given set of parameters.

        Possible sets are variance and covariance parameters for observed
        variables, loadings, and variance/covariance for latent variables.
        Parameters
        ----------
        operation : Operation
            Operation namedtuple.

        Raise
        ----------
        SyntaxError
            When no starting value is supplied as an argument to START.

        Returns
        -------
        None.

        """
        name = operation.params[0]
        params = dict()
        for p in operation.params[1:]:
            p, v = p.split('=')
            params[p] = v
        dist = self.get_distribution(name, params)
        if operation.name == self.symb_prior_param:
            for name in operation.onto:
                self.priors[name] = dist            
        elif operation.name == self.symb_prior_loading:
            self.prior_loading = dist
        elif operation.name == self.symb_prior_variance:
            self.prior_variance = dist
        elif operation.name == self.symb_prior_covariance:
            self.prior_covariance = dist
        elif operation.name == self.symb_prior_variance_latent:
            self.prior_variance_latent = dist
        else:
            self.prior_covariance_latent = dist

    def apply_operations(self, operations: dict):
        """
        Apply operations to model.

        Parameters
        ----------
        operations : dict
            Mapping of operations as returned by parse_desc.

        Raises
        ------
        NotImplementedError
            Raises in case of unknown command name.

        Returns
        -------
        None.

        """
        self.priors = dict()
        ops = self.dict_operations
        ops[self.symb_prior_loading] =  self.operation_prior,
        ops[self.symb_prior_variance] = self.operation_prior,
        ops[self.symb_prior_covariance] = self.operation_prior,
        ops[self.symb_prior_variance_latent] = self.operation_prior,
        ops[self.symb_prior_covariance_latent] = self.operation_prior,
        ops[self.symb_prior_param] = self.operation_prior    
        for command, items in operations.items():
            try:
                list(map(self.dict_operations[command], items))
            except KeyError:
                raise NotImplementedError(f'{command} is an unknown command.')

    def inspect(self, mode='list', what='est', alpha=0.9, std_est=False,
                **kwargs):
        """
        Get fancy view of model parameters estimates.
    
        Parameters
        ----------
        model : str
            Model.
        mode : str, optional
            If 'list', pd.DataFrame with estimates and p-values is returned.
            If 'mx', a dictionary of matrices is returned. The default is
            'list'.
        what : TYPE, optional
            Used only if mode == 'mx'. If 'est', matrices have estimated
            values. If 'start', matrices have starting values. If 'name',
            matrices have names inplace of their parameters. The default is
            'est'.
        alpha : float, optional
            HDPI interval length. The default is 0.9.
        std_est : bool, optional
            If True, estimates are standardized. The default is False.

        Returns
        -------
        pd.DataFrame | dict
            Dataframe or mapping matrix_name->matrix.
    
        """
        if mode == 'mx':
            return semopy_inspect(self, mode=mode, what=what)
        else:
            return inspect(self, alpha=alpha, std_est=std_est)
        

    def get_distribution(self, dist: str, params: list):
        """
        Get pyro.distribution by name.

        Parameters
        ----------
        dist : str
            Textual description of distributin in a Pyro-compaitible format,
            e.g. "Normal".
        params : dict
            Parameters that are passed to the distribution, e.g.
            {'loc': 3.0, 'scale': 1.0}

        Returns
        -------
        Pryo distribution.

        """
        params = ', '.join(f'{p}={v}' for p, v in params.items())
        return eval(f'dists.{dist}({params})')
