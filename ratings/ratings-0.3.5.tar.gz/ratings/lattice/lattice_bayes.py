# Speculative
from winning.lattice_conventions import STD_L, STD_UNIT, NAN_DIVIDEND
from winning.std_calibration import std_ability_implied_dividends, std_dividend_implied_ability
import math
import numpy as np


def std_posterior_dividend(dividends:[float], ability_std:float, idio_std:float, observations:[float],
                           nan_value=NAN_DIVIDEND, unit:float=STD_UNIT, L=STD_L, check_inversion=False):
     centered_observations = [ o-np.nanmean(observations) for o in observations]
     sigma_squared = ability_std*ability_std
     eps_squared   = idio_std * idio_std
     prior_std     = math.sqrt( sigma_squared + eps_squared )
     prior_ability = std_dividend_implied_ability( dividends=dividends, scale=prior_std, L=L,unit=unit, nan_value=nan_value )
     if check_inversion:
         prior_dividends = std_ability_implied_dividends( ability=prior_ability, scale=prior_std, L=L, unit=unit, nan_value=nan_value)
         assert all([abs(d1-d2)/d1<0.01 if np.notna(d1) else True for d1,d2 in zip(dividends,prior_dividends)])
     psi_squared = 1/( 1/sigma_squared +1/eps_squared)
     c1 = psi_squared/sigma_squared
     c2 = psi_squared/eps_squared
     posterior_ability = [ c1*z1+c2*theta_bar for z1,theta_bar in zip(centered_observations,prior_ability) ]
     posterior_var = psi_squared + 2*sigma_squared
     posterior_std = math.sqrt(posterior_var)
     posterior_div = std_ability_implied_dividends(posterior_ability, unit=unit, L=L, scale=posterior_std, nan_value=NAN_DIVIDEND)
     return posterior_div


if __name__=='__main__':
    dividends = [2,3,6]
    observations = [0,-1,-0.5]
    pseudo = std_posterior_dividend(dividends=dividends, ability_std=10, idio_std=2 * math.sqrt(2), observations=observations)
    print(pseudo)