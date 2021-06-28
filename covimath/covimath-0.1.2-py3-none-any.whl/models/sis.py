#!/usr/bin/env python3

from math import exp
import numpy as np
import matplotlib.pyplot as plt
import logging

from ..utils.modelargs import parse_args

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

# Susceptible -> Infected -> Susceptible model
class SIS:
    
    def __init__(self, N, lam, mu, gamma, I0, tau):
        logger.info('Intializing SIS model ...')
        self.N = N # Total population (assumed constant)
        self.lam = lam # Daily contact rate (for adequate contact)
        self.mu = mu # Proportionality constant of daily deaths (in each class)
        self.gamma = gamma # Proportionality constant of daily recovery
        self.I0 = I0 # Initial infected population (number, not fraction)
        self.S0 = N - I0 # Initial susceptible population (number, not fraction)
        self.tau = tau # Time window in days over which to model
        self.sigma = lam * 1.0 / (gamma + mu) # contact number
    
    # Closed form function : Infected population (fraction)
    def i(self, t):
        lam = self.lam
        gamma = self.gamma
        mu = self.mu
        sigma = self.sigma
        I0 = self.I0
        
        if sigma == 1:
            return 1.0 / (lam*t + 1.0/I0)
        else:
            num = exp((gamma + mu)*(sigma -1 )*t)
            den = (exp((gamma + mu)*(sigma -1 )*t)) * (sigma * 1.0 / 
                                                (sigma - 1)) + 1.0 / I0
            
            return num * 1.0 / den
    
    # Infected population (absolute number)
    def iabs(self, t):
        return self.i(t) * self.N
    
    # Closed form function : Susceptibile poputation (fraction)
    def s(self, t):
        return 1.0 - self.i(t)
    
    # Susceptible population (absolute number)
    def sabs(self, t):
        return self.s(t) * self.N
    
    # Plot the S and I curves
    def plot(self, absolute=False):
        logger.info('Plotting SIS model ...')
        T = np.linspace(0, self.tau, self.tau)
        N = self.N
        
        if absolute:
            I = [self.iabs(tim) for tim in T]
            S = [self.sabs(tim) for tim in T]
        else:
            I = [self.i(tim) for tim in T]
            S = [self.s(tim) for tim in T]
        
        Iarr = np.array(I)
        Sarr = np.array(S)
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        if absolute:
            slab = 'Susceptible Population'
            ilab = 'Infected Population'
        else:
            slab = 'Susceptible Fraction'
            ilab = 'Infected Fraction'
            
        ax.plot(T, Sarr, label=slab)
        ax.plot(T, Iarr, label=ilab)
        
        ax.set_xlabel('Days')
        if absolute:
            ax.set_ylabel('Number of People')
            ax.set_ylim(0, N+100)
        else:
            ax.set_ylabel('Fraction of Population')
            ax.set_ylim(0, 1.1)
            
        legend = ax.legend()
        
        plt.show()

def usage():
    usagestr0 = './sis.py N=<N> I0=<I0> lambda=<lambda> mu=<mu> gamma=<gamma> tau=<tau> --abs, where: \n'
    usagestr1 = 'N = total population, assumed constant \n'
    usagestr2 = 'I0 = initial number of infected people \n'
    usagestr3 = 'lambda = daily contact rate \n'
    usagestr4 = 'mu = proportionality constant of daily deaths \n'
    usagestr5 = 'gamma = proportionality constant of daily recovery \n'
    usagestr6 = 'tau = duration in days over which the model should be constructed. \n'
    usagestr7 = '--abs (optional) means a plot with absolute numbers (instead of fraction of population) is needed. \n'
    usagestr8 = 'Note: order of arguments passsed is not important. Any other argument will be ignored. \n'
    usagestr9 = '\nExample: ./sis.py N=1000 lambda=0.05 mu=0.15 gamma=0.1 I0=1 tau=30 \n'
    
    print(usagestr0 + usagestr1 + usagestr2 + usagestr3 + usagestr4 + 
            usagestr5 + usagestr6 + usagestr7 + usagestr8 + usagestr9)
        
if __name__ == "__main__":
    
    res = parse_args()
    if res is None:
        logger.error('No argument passed.')
        usage()
        quit()
        
    if res == 'usage':
        usage()
        quit()
        
    if isinstance(res, dict):
        miss = []
        if 'N' in res:
            N = res['N']
        else:
            miss.append('N')
            
        if 'lambda' in res:
            lam = res['lambda']
        else:
            miss.append('lambda')
            
        if 'mu' in res:
            mu = res['mu']
        else:
            miss.append('mu')
        
        if 'gamma' in res:
            gamma = res['gamma']
        else:
            miss.append('gamma')
            
        if 'I0' in res:
            I0 = res['I0']
        else:
            miss.append('I0')
            
        if 'tau' in res:
            tau = res['tau']
        else:
            miss.append('tau')
        
        plotabs = False
        if '--abs' in res:
            plotabs = True
            
        if len(miss) > 0:
            logger.error('Some required arguments are missing: ' + ','.join(miss))
            usage()
            quit()

    model = SIS(N=N, lam=lam, mu=mu, gamma=gamma, I0=I0, tau=tau)
    
    if plotabs:
        model.plot(absolute=True)
    else:
        model.plot()