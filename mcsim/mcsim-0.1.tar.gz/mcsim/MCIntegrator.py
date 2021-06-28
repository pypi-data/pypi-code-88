####################################################################
###################### Monte Carlo Integration #####################
####################################################################

import scipy.stats
import numpy as np

class MCIntegrator():
  '''A Monte-Carlo Integration Class Based on Uniform Density'''
  def __init__(self, N=1000):
    '''Args: N - The number of samples to draw.'''
    self.N = N  

  def __repr__(self):
    '''State the Sample size.'''
    return 'MC Sample size: {}'.format(self.N)

  def fit(self, lwr, upr, func):
    '''Compute the integral based on bounds and function.
    Also compute the standard error.
    Args:
      lwr - The lower bound of the integral (int/float).
      upper - The upper bound of the integral (int/float).
      func - The integrating function.
    Output:
      None.'''
    # Generate uniform samples
    unif_samples = np.random.uniform(low=lwr, high=upr, size=self.N)

    # Transform samples using custom function
    mapped_samples = np.array([func(x) for x in unif_samples])
    w = mapped_samples*(upr - lwr)

    # Compute the integral estimate and its se
    ihat = np.mean(w)
    s_squared = (1.0/(self.N - 1)) * np.sum(w - ihat)**2
    se_hat = np.sqrt(s_squared)

    self.ihat = ihat
    self.se_hat = se_hat/np.sqrt(self.N)

  def get_confidence_intervals(self, alpha):
    '''Computes (1 - alpha)*100% Confidence Intervals.
    Args:
      alpha - The level of significance (float, between 0 and 1).
    Output:
      (a, b) - The confidence interval.'''
    z = scipy.stats.norm.ppf(1 - alpha)
    # print(z)
    lwr = self.ihat - z*self.se_hat
    upr = self.ihat + z*self.se_hat
    self.confidence_int = (lwr, upr)
    return self.confidence_int
