#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pyro solvers."""
import numpyro as pyro
from jax.random import PRNGKey


not_mcmc_solvers = set(('TODO',))

def solve(obj, model, solver: str, num_warmup=None, num_samples=None,
          num_chains=1, mode='best', seed=0, **kwargs):
    if solver not in not_mcmc_solvers:
        res = mcmc_solver(obj, model, kernel=solver, num_warmup=num_warmup,
                          num_samples=num_samples, num_chains=num_chains,
                          mode=mode, seed=seed, **kwargs)
    else:
        raise NotImplementedError(f"Unknown solver {solver}.")
    return res
    
def mcmc_solver(obj, model, kernel: str, num_warmup=None, num_samples=None, 
                num_chains=1, mode='best', seed=0, **kwargs):
    if num_samples is None:
        n = len(obj.param_vals)
        num_samples = n * 30
    if num_warmup is None:
        num_warmup = num_samples // 5
    rnd = PRNGKey(seed)    
    with pyro.handlers.seed(rng_seed=rnd):
        try:
            k = eval(f'pyro.infer.{kernel}(model, **kwargs)')
        except AttributeError:
            raise NotImplementedError(f'Unknown MCMC kernel {kernel}.')
        mcmc = pyro.infer.MCMC(k, num_warmup=num_warmup,
                               num_samples=num_samples, num_chains=num_chains)
        mcmc.run(rng_key=rnd)
    samples = mcmc.get_samples(group_by_chain=True)
    if mode == 'best':
        best_vals = None
        best_logp = -float('inf')
        for i in range(num_chains):
            vals = {n: float(v[i].mean()) for n, v in samples.items()}
            dist, z = pyro.handlers.condition(model, data=vals)()
            logp = dist.log_prob(z)
            if logp.ndim > 0:
                logp = sum(logp)
            if logp > best_logp:
                best_logp = logp
                best_vals = vals 
    elif mode == 'average':
        best_vals = {n: float(v.mean()) for n, v in samples.items()}
    else:
        raise NotImplementedError("Unknown MCMC chains treatment method:"
                                  f" {mode}.")
    c = 0
    for name, p in obj.parameters.items():
        v = best_vals.get(name, None)
        if v is None:
            continue
        for loc in p.locations:
            loc.matrix[loc.indices] = v
        obj.param_vals[c] = v
        c += 1
    return mcmc
