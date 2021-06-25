#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Default priors for parameters in different model matrices."""

from numpyro import distributions as dists
import numpy as np

cov_mult = np.sqrt(np.pi / 2)

def prior_beta(model, start, i, j):
    if model.prior_loading is not None:
        return model.prior_loading
    if abs(start) < 1e-4:
        return dists.Normal(scale=1.5)
    else:
        return dists.Normal(start, 0.75)

def prior_lambda(model, start, i, j):
    return prior_beta(model, start, i, j)

def prior_gamma1(model, start, i, j):
    return prior_beta(model, start, i, j)

def prior_gamma2(model, start, i, j):
    return prior_gamma1(model, start, i, j)

def prior_psi(model, start, i, j):
    lats = model.vars['latent']
    names = model.names_psi[0]
    a = names[i]
    b = names[j]
    if a in lats or b in lats:
        if i == j:
            if model.prior_variance_latent is not None:
                return model.prior_variance_latent
            return dists.HalfNormal(cov_mult)
        else:
            if model.prior_covariance_latent is not None:
                return model.prior_covariance_latent
            return dists.Normal(start, scale=1)
    if i == j:
        if model.prior_variance is not None:
            return model.prior_variance
        return dists.HalfNormal(start ** 0.5 * cov_mult)
    if model.prior_covariance is not None:
        return model.prior_covariance
    return dists.Normal(start, scale=1)
    
def prior_theta(model, start, i, j):
    if i == j:
        if model.prior_variance:
            return model.prior_variance
        return dists.HalfNormal(start ** 0.5 * cov_mult)
    if model.prior_covariance is not None:
        return model.prior_covariance
    return dists.Normal(start, scale=1)

def prior_d(model, start, i, j):
    if i == j:
        return dists.HalfNormal(cov_mult * 0.5)
    else:
        return dists.Normal(scale=0.5)