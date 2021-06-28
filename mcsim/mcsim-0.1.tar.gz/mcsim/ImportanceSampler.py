#################################################################
#################### Importance Sampling ########################
#################################################################

import scipy.stats
import numpy as np
# from pdfs import pdf_pareto, pdf_chisquare

class ImportanceSampler():
  '''Importance Sampling for Expectation approximations when sampling is difficult.'''
  def __init__(self, tails = 2, N=1000):
    '''Args: 
      N - The number of samples to draw (float()).
      tails - Whether f(x) has one or two tails (float).
    Returns: None.'''
    if float(tails) not in (1,2):
      raise TypeError('Distributions can have one or two tails only.') 
    self.N = N  
    self.tails = tails
  
  def __repr__(self):
    '''State the Sample size and tail number.'''
    return 'MC Sample size: {}, Number of tails: {}'.format(self.N, self.tails)

  def fit(self, f, h):
    '''Compute the integral based on bounds and f function.
    Also compute the standard error.
    Args:
      f - The original integrating function.
      h - The expectation function (e.g. h(x) = x^2)
    Output:
      None.'''
    # Generate our alternate samples based on number of tails
    if float(self.tails) == 2.0:
      g = scipy.stats.cauchy.rvs(loc=0, scale=2, size = self.N)
    elif float(self.tails) == 1.0:
      g = scipy.stats.levy.rvs(scale=2, size = self.N) 
    
    # Transform these samples
    g_samples = np.array([scipy.stats.levy.pdf(x, scale=2) for x in g])
    h_samples = np.array([h(x) for x in g])
    f_samples = np.array([f(x) for x in g])

    new_expectation = (h_samples*f_samples)/g_samples

    # Compute Ihat and se
    ihat = np.mean(new_expectation)
    self.ihat = ihat

    s_squared = (1.0/(self.N - 1)) * np.sum(new_expectation - ihat)**2
    se_hat = np.sqrt(s_squared)

    self.se_hat = se_hat/np.sqrt(self.N)

  def get_confidence_intervals(self, alpha):
    '''Computes (1 - alpha)*100% Confidence Intervals.
    Args:
      alpha - The level of significance (float, between 0 and 1).
    Output:
      (a, b) - The confidence interval.'''
    z = scipy.stats.norm.ppf(1 - alpha)
    lwr = self.ihat - z*self.se_hat
    upr = self.ihat + z*self.se_hat
    self.confidence_int = (lwr, upr)
    return self.confidence_int