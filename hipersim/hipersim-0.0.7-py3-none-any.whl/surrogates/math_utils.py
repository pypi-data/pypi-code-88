# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:37:43 2019

@author: nkdi
"""
import numpy as np
def relu(x): return x*(x > 0)

def softplus(x): return np.log(1 + np.exp(x))

def logistic(x): return 1/(1 + np.exp(-x))

def hyperbolic_tangent(x): return (np.exp(2*x) - 1)/(np.exp(2*x) + 1)

def pairwise_correlation(A,B):
    N = B.shape[0]
    M = B.shape[1]
    muA = A.sum(0)/N
    muB = B.sum(0)/N
    muAB = (A*B).sum(0)/N
    muA2 = (A**2).sum(0)/N
    muB2 = (B**2).sum(0)/N
    rho = np.array([None]*M,ndmin = 2,dtype = 'float64')
    rho[0,:M] = (muAB - muA*muB)/(np.sqrt( muA2 - muA*muA)*np.sqrt( muB2 - muB*muB))
    return rho

def NormalDist(task,x,mu,sigma):
    import scipy.special
    if task == 0:
        y = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-((x - mu)**2)/(2*(sigma**2)))
    elif task == 1:
        y = 0.5*(1 + scipy.special.erf((x - mu)/(sigma*np.sqrt(2))))
    elif task == 2:
        y = mu + sigma*np.sqrt(2)*scipy.special.erfinv(2*x - 1)
    return y
