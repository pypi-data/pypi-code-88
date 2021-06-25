#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inspector module helps researcher fetch information on estimates."""
from semopy.inspector import inspect_list
from numpyro.diagnostics import summary


def inspect(model, std_est=False, alpha=0.9):
    """
    Get a pandas DataFrame containin a view of parameters estimates.

    Parameters
    ----------
    model : Model
        Model.
    std_est : bool
        If True, standardized coefficients are also returned as Std. Ests col.
        The default is False.
    alpha : float, optional
        The default is 0.9. #TODO

    Returns
    -------
    pd.DataFrame
        DataFrame with parameters information.

    """
    res = inspect_list(model, information=None, std_est=std_est,
                       index_names=True).drop(['Std. Err', 'z-value',
                                               'p-value'], axis=1)
    samples = model.last_result.get_samples(group_by_chain=True)
    s = summary(samples, prob=alpha)
    it = next(iter(s))
    res['std'] = '-'
    res['n_eff'] = '-'
    res['r_hat'] = '-'    
    k = list(s[it].keys())
    hp = k[-3]
    lp = k[-4]
    res[lp] = '-'
    res[hp] = '-'
    for name, row in s.items():
        it = res.loc[name].copy()
        it['std'] = row['std']
        it['n_eff'] = row['n_eff']
        it['r_hat'] = row['r_hat']
        it[lp] = row[lp]
        it[hp] = row[hp]
        res.loc[name] = it
    cols = ['lval', 'op', 'rval', 'Estimate', lp, hp, 'std', 'n_eff', 'r_hat']
    return res[cols]