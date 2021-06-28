#!/usr/bin/env python3

import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import logging

from ..utils.modelargs import parse_args

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

# Susceptible -> Infected -> Recovered model
class SIR:
    
    def __init__(self, N, beta, gamma, I0, R0, tau):
        logger.info('Intializing SIR model ...')
        self.N = N # Total population (assumed constant)
        self.beta = beta # Daily contact rate (for adequate contact)
        self.gamma = gamma # Proportionality constant of daily recovery
        self.I0 = I0 # Initial infected population (number, not fraction)
        self.R0 = R0 # Initial recovered population (number, not fraction)
        # Initial susceptible population (number, not a fraction)
        self.S0 = N - I0 - R0
        self.tau = tau # Time window in days over which to model
        self.t = np.linspace(0, self.tau, self.tau)
        self.S = None
        self.I = None
        self.R = None
    
    # Solve the differential equatons for this model
    def solve(self):
        
        def diffeqns(t, y, N, beta, gamma):

            S, I, R = y
            dSdt = -beta * S * I / N
            dIdt = beta * S * I / N - gamma * I
            dRdt = gamma * I
        
            dydt = [dSdt, dIdt, dRdt]
            return dydt
        
        y0 = [self.S0, self.I0, self.R0] # Initial values
        
        # Solve differntial equations
        tspan = [0, self.tau]
        sol = solve_ivp(diffeqns, tspan, y0, 
                     t_eval = self.t, args=(self.N, self.beta, self.gamma))
        
        self.S = sol.y[0]
        self.I = sol.y[1]
        self.R = sol.y[2]
    
    # Find the peak infection (day, number infected)
    def peak(self):
        if self.I is None:
            logger.error('solve() method has not been invoked yet')
            raise ValueError("peak() method invoked before invoking solve()")
        
        p = find_peaks(self.I, height = 0)
        day = p[0][0]
        infec = p[1]['peak_heights'][0]
        return day, infec
    
    # Plot the S, I and R curves
    def plot(self):
        if self.S is None or self.I is None or self.R is None:
            logger.error('solve() method has not been invoked yet')
            raise ValueError("plot() method invoked before invoking solve()")
        
        logger.info('Plotting SIR model ...')
        S = self.S
        I = self.I
        R = self.R
        t = self.t
        N = self.N
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        ax.plot(t, S, label='Susceptible Population')
        ax.plot(t, I, label='Infected Population')
        ax.plot(t, R, label='Recovered Population')
        ax.set_xlabel('Days')
        ax.set_ylabel('Number of People')
        
        ax.set_ylim(0, N+100)
        legend = ax.legend()
        
        plt.show()

def usage():
    usagestr0 = './sir.py N=<N> I0=<I0> R0=<R0> beta=<beta> gamma=<gamma> tau=<tau>, where: \n'
    usagestr1 = 'N = total population, assumed constant \n'
    usagestr2 = 'I0 = initial number of infected people \n'
    usagestr3 = 'R0 = initial number of recovered people \n'
    usagestr4 = 'beta = daily contact rate \n'
    usagestr5 = 'gamma = proportionality constant of daily recovery \n'
    usagestr6 = 'tau = duration in days over which the model should be constructed. \n' 
    usagestr7 = 'Note: order of arguments passsed is not important. Any other argument will be ignored. \n'
    usagestr8 = '\nExample: ./sir.py N=1000 I0=1 R0=0 beta=0.2 gamma=0.1 tau=150 \n'
    
    print(usagestr0 + usagestr1 + usagestr2 + usagestr3 + usagestr4 + 
            usagestr5 + usagestr6 + usagestr7 + usagestr8)
    
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
            
        if 'beta' in res:
            beta = res['beta']
        else:
            miss.append('beta')
        
        if 'gamma' in res:
            gamma = res['gamma']
        else:
            miss.append('gamma')
            
        if 'I0' in res:
            I0 = res['I0']
        else:
            miss.append('I0')
            
        if 'R0' in res:
            R0 = res['R0']
        else:
            miss.append('R0')
            
        if 'tau' in res:
            tau = res['tau']
        else:
            miss.append('tau')
            
        if len(miss) > 0:
            logger.error('Some required arguments are missing: ' + ','.join(miss))
            usage()
            quit()

    model = SIR(N=N, beta=beta, gamma=gamma, I0=I0, R0=R0, tau=tau)
    
    model.solve()
    
    model.plot()