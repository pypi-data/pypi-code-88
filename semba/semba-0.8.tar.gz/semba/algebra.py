#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Precompiled linear algebra functions for semba models."""
import jax.numpy as jnp
from jax import jit

@jit
def calc_sigma(mx_beta: jnp.ndarray, mx_lambda: jnp.ndarray,
               mx_psi: jnp.ndarray, mx_theta: jnp.ndarray):
    c = jnp.linalg.inv(jnp.identity(mx_beta.shape[0]) - mx_beta)
    t = mx_lambda @ c
    sigma = t @ mx_psi @ t.T + mx_theta
    return t, sigma

@jit
def calc_mean(mx_gamma1: jnp.ndarray, mx_gamma2: jnp.ndarray,
              mx_g: jnp.ndarray, lambda_c: jnp.ndarray):
    return (lambda_c @ mx_gamma1 + mx_gamma2) @ mx_g

@jit
def calc_l(mx_sigma: jnp.ndarray, mx_d: jnp.ndarray, mx_k: jnp.ndarray):
    return mx_sigma + mx_d * mx_k.sum(-1)

@jit
def calc_t_diag(mx_sigma: jnp.ndarray, mx_d: jnp.ndarray, mx_k: jnp.ndarray):
    return jnp.trace(mx_sigma) + jnp.trace(mx_d) * mx_k