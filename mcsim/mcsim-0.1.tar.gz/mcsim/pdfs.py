########################################################################
########################### PDF Functions ##############################
######################################################################## 

import math

# Gaussian Distribution
def pdf_normal(x, mu=0, sigma = 1):
    '''The pdf of the normal distribution.
    Args:
    x - the query point (int/float).
    mu - the normal density mean (float).
    sigma - the normal density SD (float).
    Returns: The normal density at point x.'''
    # Confirm sigma is positive
    if sigma <= 0:
        print('ParamError: Variance must be positive.')
        return None
    else:
        coef = (1./ (math.sqrt(2*math.pi) * sigma) )
        exponent = math.exp( -0.5*((x - mu)/sigma)**2 )
        pdf = coef*exponent
        return pdf

# Exponential Distribution
def pdf_exponential(x, lam = 0.5):
    '''The pdf of the exponential distribution.
    Args:
        x - the query point (int/float).
        lam - the rate parameter (float).
    Returns: The exponential density at point x.'''
    # Confirm query point is in (0, inf)
    if x < 0:
        print('Exponential has non-negative support.')
        return 0
    # Confirm positive rate
    elif lam <= 0:
        print('Rate parameter must be positive.')
        return None
    else:
        pdf =  lam * math.exp(-1 * lam * x)
        return pdf
  

# Uniform Distribution
def pdf_uniform(x, a=0, b=1):
    '''The pdf of the uniform distribution.
    Args:
        x - the query point (int/float).
        a - the lower bound (float).
        b - the upper bound (float).
    Returns: The uniform density at point x.'''
    # Confirm bounds don't cross
    if b <= a:
        return None
    # Confirm query point is in (a, b)
    elif x < a or x > b:
        print('Uniform support is in (a,b).')
        return 0.0
    else:
        return 1 / (b - a)

# Student-T distribution
def pdf_studentt(x, v=1):
    '''The pdf of the T distribution.
    Args:
        x - the query point (int/float).
        v - the degrees of freedom (float).
    Returns: The student-t density at point x.'''
    # Confirm v > 0
    if v <= 0:
        print('Error: Degrees of Freedom must be positive.')
        return None
    else:
        coef = math.gamma( 0.5*(v + 1) )/ (math.sqrt(v*math.pi) * math.gamma(v/2))
        exponent = ( (1 + x**2)/v )**(-0.5*(v + 1))
        pdf = coef*exponent
        return pdf

# Beta Distribution
def pdf_beta(x, a=1, b=1):
    '''The pdf of the Beta distribution.
    Args:
        x - the query point (int/float).
        a - the first shape parameter (float).
        b - the second shape parameter (float).
    Returns: The beta density at point x.'''
    # Confirm x in (0,1)
    if x <= 0 or x > 1:
        print('Beta support is in (0,1).')
        return 0
    # Confirm positive shape params
    elif a <=0 or b <= 0:
        print('ParamError: Beta shape params must be positive.')
        return None
    else:
        coef = math.gamma(a + b)/ (math.gamma(a)*math.gamma(b))
        prod = x**(a-1) * (1-x)**(b-1)
        pdf = coef*prod
        return pdf

# Gamma Distribution
def pdf_gamma(x, a, b):
    '''The pdf of the Gamma distribution.
    Args:
        x - the query point (int/float).
        a - the shape param (float).
        b - the scale param (float).
    Returns: The gamma density at point x.'''
    # Confirm positive x
    if x < 0:
        print('Gamma support is strictly nonnegative.')
        return 0
    # Confirm positive params
    elif a <= 0 or b <= 0:
        print('ParamError: Shape and Scale params must be strictly positive')
        return None
    else:
        coef = ( b**a ) / math.gamma(a)
        exponent = x**(a - 1) * math.exp(-1*b*x)
        pdf = coef*exponent
        return pdf

# Chi-square Distribution

def pdf_chisquare(a, v):
    '''The pdf of the Chi-square distribution.
    Args:
        x - the query point (int/float).
        v - the degrees of freedom (float).
    Returns: The chisquare density at point x.'''
    # Confirm positive x
    if x <= 0:
        print('Chisquare support is positive.')
        return 0.0
    # Confirm df is natural number
    elif not v.is_integer():
        print('ParamError: v must be a natural number.')
        return None
    else:
        coef = 1 / ((2**(v/2))*(math.gamma(v/2)))
        prod = (x**( (k-1)/2 ))*(math.exp(-0.5*x))
        pdf = coef*prod
        return pdf

# Fisher Distribution

def pdf_fisher(x, v1, v2):
    '''The pdf of the Fisher distribution.
    Args:
        x - the query point (int/float).
        v1 - the first degrees of freedom (float).
        v2 - the second degrees of freedom (float).
    Returns: The fisher density at point x.'''
    if x <= 0:
        print('Fisher support is positive.')
        return 0.0
    # Confirm dfs are natural numbers
    elif not v1.is_integer() or not v2.is_integer():
        print('ParamError: dfs must be natural numbers.')
        return None
    else:
        u1 = pdf_chisquare(x, v1)
        u2 = pdf_chisquare(x, v2)
        pdf = (u1/v1)/(u2/v2)
        return pdf

# Laplace Distribution
def pdf_laplace(x, mu, b):
    '''The pdf of the Laplace distribution.
    Args:
        x - the query point (int/float).
        mu - the location parameter (float).
        b - the scale parameter (float).
    Returns: The laplace density at point x.'''
    # Confirm b is positive
    if b <= 0:
        print('ParamError: Scale parameter must be positive')
        return None
    else:
        coef = 1/(2*b)
        exponent = math.exp((-1/b)*abs(x - mu))
        pdf = coef*exponent
        return pdf

# Pareto Distribution
def pdf_pareto(x, m, a):
    '''The pdf of the pareto distribution.
    Args:
        x - the query point (int/float).
        m - the scale parameter (float).
        a - the shape parameter (float).
    Returns: The pareto density at point x.'''
    # Confirm parameters are positive
    if m <= 0 or a <= 0:
        print('ParamError: Parameters must be positive.')
        return None
    # Confirm x exceeds m
    elif x < m:
        print('Pareto support is lower-bounded by m.')
        return 0
    else:
        pdf = (a*(m**a))/ (x**(a + 1))
        return pdf

# Rayleigh Distribution
def pdf_rayleigh(x, sigma):
    '''The pdf of the Rayleigh distribution.
    Args:
        x - the query point (int/float).
        sigma - the scale parameter (float).
    Returns: The rayleigh density at point x.'''
    # Confirm scale param is positive
    if sigma <= 0:
        print('ParamError: Sigma must be positive.')
        return None
    # Confirm x is non-negative
    elif x < 0:
        print('Rayleigh has positive support.')
        return 0
    else:
        coef = x / (sigma*2)
        exponent = math.exp( (-x**2)/ (2 * (sigma**2)) )
        pdf = coef*exponent
        return pdf

# Weibull Distribution
def pdf_weibull(x, lam, k):
    '''The pdf of the Weibull distribution.
    Args:
        x - the query point (int/float).
        lam - the scale parameter (float).
        k - the shape parameter (float).
    Returns: The Weibull density at point x.'''
    # Confirm non-negative support
    if x < 0:
        print('Weibull has non-negative support.')
        return 0
    # confirm positive parameters
    elif lam <= 0 or k <= 0:
        print('ParamError: Shape and scale params must be positive.')
        return None
    else:
        coef = (k/lam)*(k/lam)**(k-1)
        exponent = math.exp( -1*(x/lam)**k )
        pdf = coef*exponent
        return pdf
