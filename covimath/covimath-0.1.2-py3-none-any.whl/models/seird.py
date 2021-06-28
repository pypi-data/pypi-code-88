#!/usr/bin/env python3
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import logging

from ..utils.modelargs import parse_args

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

# Susceptible -> Exposed -> Infected -> Recovered -> Dead model
class SEIRD:
    
    def __init__(self, N, beta, sigma, gamma, mu, E0, I0, R0, D0, tau):
        logger.info('Initializing SEIR model ...')
        self.N = N # Total population (assumed constant)
        self.beta = beta # Daily contact rate (for adequate contact)
        self.sigma = sigma # Incubation rate
        self.gamma = gamma # Proportionality constant of daily recovery
        self.mu = mu # mortality rate
        self.E0 = E0 # Initial exposed population (number, not a fraction)
        self.I0 = I0 # Initial infected population (number, not fraction)
        self.R0 = R0 # Initial recovered population (number, not fraction)
        self.D0 = D0 # Initial dead  (number, not a fraction)
        # Initial susceptible population (number, not a fraction)
        self.S0 = N - E0 - I0 - R0 - D0
        self.tau = tau # Time window in days over which to model
        self.t = np.linspace(0, self.tau, self.tau)
        self.S = None
        self.E = None
        self.I = None
        self.R = None
        self.D = None
    
    # Solve the differential equation for this model
    def solve(self):
        
        def diffeqns(t, y, N, beta, sigma, gamma, mu):
            S, E, I, R, D = y
            dSdt = -beta * S * I / N
            dEdt = beta * S * I / N - sigma * E
            dIdt = sigma * E - gamma * I - mu * I
            dRdt = gamma * I
            dDdt = mu * I
            return [dSdt, dEdt, dIdt, dRdt, dDdt]
        
        y0 = [self.S0, self.E0, self.I0, self.R0, self.D0] # Initial values
        
        # Solve differential equations
        tspan = [0, self.tau]
        sol = solve_ivp(diffeqns, tspan, y0, 
                        t_eval = self.t, 
                        args=(self.N, self.beta, self.sigma, self.gamma, self.mu))
        
        self.S = sol.y[0]
        self.E = sol.y[1]
        self.I = sol.y[2]
        self.R = sol.y[3]
        self.D = sol.y[4]
    
    # Find the peak infection (day, number infected)
    def peak(self):
        if self.I is None:
            logger.error('solve() method has not been invoked yet')
            raise ValueError("peak() method invoked before invoking solve()")
            
        p = find_peaks(self.I, height = 0)
        day = p[0][0]
        infec = p[1]['peak_heights'][0]
        return day, infec     

    # Plot the S, E, R and D curves        
    def plot(self):
        if self.S is None or self.I is None or self.R is None or self.D is None:
            logger.error('solve() method has not been invoked yet')
            raise ValueError("plot() method invoked before invoking solve()")
            
        logger.info('Plotting SEIR model ...')
        N = self.N
        S = self.S
        E = self.E
        I = self.I
        R = self.R
        D = self.D
        t = self.t
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        ax.plot(t, S, label='Susceptible Population')
        ax.plot(t, E, label='Exposed Population')
        ax.plot(t, I, label='Infected Population')
        ax.plot(t, R, label='Recovered Population')
        ax.plot(t, D, label='Dead')
        ax.set_xlabel('Days')
        ax.set_ylabel('Number of People')
        
        ax.set_ylim(0, N+100)
        
        legend = ax.legend()
        
        plt.show()

def usage():
    usagestr0 = './seird.py N=<N> E0=<E0> I0=<I0> R0=<R0> D0=<D0> beta=<beta> sigma=<sigma> gamma=<gamma> mu=<mu> tau=<tau>, where: \n'
    usagestr1 = 'N = total population, assumed constant \n'
    usagestr2 = 'E0 = initial number of people exposed \n'
    usagestr3 = 'I0 = initial number of infected people \n'
    usagestr4 = 'R0 = initial number of people recovered \n'
    usagestr5 = 'D0 = initial number of people dead \n'
    usagestr6 = 'beta = daily contact rate \n'
    usagestr7 = 'sigma = incubation rate \n'
    usagestr8 = 'gamma = proportionality constant of daily recovery \n'
    usagestr9 = 'mu = mortality rate \n'
    usagestr10 = 'tau = duration in days over which the model should be constructed. \n'
    usagestr11 = 'Note: order of arguments passsed is not important. Any other argument will be ignored. \n'
    usagestr12 = '\nExample: ./seird.py N=1000 E0=1 I0=1 R0=0 D0=0 beta=1.38 sigma=0.19 gamma=0.34 mu=0.03 tau=150 \n'
    
    print(usagestr0 + usagestr1 + usagestr2 + usagestr3 + usagestr4 + 
          usagestr5 + usagestr6 + usagestr7 + usagestr8 + 
          usagestr9 + usagestr10 + usagestr11 + usagestr12)
    
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
            
        if 'sigma' in res:
            sigma = res['sigma']
        else:
            miss.append('gamma')
            
        if 'gamma' in res:
            gamma = res['gamma']
        else:
            miss.append('gamma')
            
        if 'mu' in res:
            mu = res['mu']
        else:
            miss.append('mu')
        
        if 'E0' in res:
            E0 = res['E0']
        else:
            miss.append('E0')
            
        if 'I0' in res:
            I0 = res['I0']
        else:
            miss.append('I0')
            
        if 'R0' in res:
            R0 = res['R0']
        else:
            miss.append('R0')
            
        if 'D0' in res:
            D0 = res['D0']
        else:
            miss.append('D0')
            
        if 'tau' in res:
            tau = res['tau']
        else:
            miss.append('tau')
        
        if len(miss) > 0:
            logger.error('Some required arguments are missing: ' + ','.join(miss))
            usage()
            quit()

    model = SEIRD(N=N, E0=E0, I0=I0, R0=R0, D0=D0, beta=beta, sigma=sigma, 
                 gamma=gamma, mu=mu, tau=tau)
    
    model.solve()
    
    model.plot()