import timeit
import torch
import torch.nn as nn
import torch.utils.data
import torch.nn.functional as F

from contextlib import suppress

import math

import collections

import numpy as np

def normalize(h):
    return(h / (h*h).sum((1,2),keepdim=True).sqrt())

def orthonormalize(h, ortho = True, use_qr = True):
    """Use QR decomposition to make the individual PWMs in h orthonormal to each other"""
    if not ortho: return(normalize(h))
    reshape_h = h.view(h.shape[0],h.shape[1]*h.shape[2]).transpose(0,1) # reshape each PWM to a vector
    Q = torch.qr(reshape_h).Q if use_qr else torch.svd(reshape_h).U # QR decomposition
    return(Q.transpose(0,1).view(*h.shape)) # reshape back to PWM

def pool_unpool(x, kernel_size = 7, stride = 7, two_way=False):
    """Like max-pooling but doesn't reduce resolution. i.e. zeros out all but the max in each window."""
    abs_output, indices = F.max_pool1d(x.abs(), kernel_size = kernel_size, stride = stride, return_indices=True)
    output = x.gather(dim=2, index=indices)
    if two_way: # this is like max pool (unpool) but across channels
        max_vals = abs_output.max(1,keepdim=True).values
        output[torch.logical_not(abs_output == max_vals)]=0.
    return F.max_unpool1d(output, indices, kernel_size = kernel_size, stride = stride, output_size = x.size())

def apply_op_full(x,h):
    return F.conv_transpose1d(x,h.transpose(0,1))

def apply_op_sparse(x, h, **kwargs):
    b = F.conv_transpose1d(x,h.transpose(0,1))
    return(pool_unpool(b, **kwargs))

class PowerBase: 
    """Base call for power iteration method
    
    Classes inheriting from this class should implement the member functions __init__(), accumulate() and step()"""
    
    def fit_func(self, 
            accumulator, 
            steps = 1000, 
            verbose = False, 
            change_threshold = 1e-4):
        """Functional fitting function
        
        Params
        ------
        accumulator: function which increments sufficient statistics
        steps: number of iterations to run
        verbose: output at every step? 
        change_threshold: 
        """
        
        for i in range(steps):
            accumulator(self)
            mae_change = self.step()
            if verbose: print("%i %.3g %.3g" % (i,mae_change,self.loss_cache),end="\n")
            if (mae_change < change_threshold): break
        return(self.weights)
        
    def fit(self, x, batch_size = None, deflater = None, **kwargs):
        """Public fitting function. 
        
        Params
        ------
        x: data, a [samples x channels x sequenceLength] tensor
        batch_size: think you can guess this one.
        deflater: a function which subtracts away the previously estimated factors
        **kwargs are passed on to fit_func"""

        if batch_size is None: batch_size = x.shape[0] # i.e. full data
            
        def batch_accumalator(pi):
            for j in range(0, x.shape[0], batch_size): 
                batch = x[j:j+batch_size,:,:]
                if not deflater is None: 
                    batch = deflater(batch)
                pi.accumulate(batch)
        
        return self.fit_func(batch_accumalator, **kwargs)
    
    def deflate_helper(self, net):
        return(F.conv1d(net,self.h.transpose(0,1)))
    
    def deflate(self, x):
        net = self.apply_op(x,self.h)
        fitted = self.deflate_helper(net) 
        return(x - fitted)
    
    @property
    def weights(self): 
        """Return fitted PCs."""
        return(self.h)

class FastICA(PowerBase):
    """Based on the FastICA algorithm. Work out quite similiar to power iteration."""
    @staticmethod
    def tanh_prime(g):
        t = torch.tanh(g)
        return(1. - t * t)
    
    @staticmethod
    def rbf(g):
        return(g * torch.exp(-.5*g*g))
    
    @staticmethod
    def rbf_prime(g):
        return((1. - g*g) * torch.exp(-.5*g*g))
    
    def soft_threshold_prime_(self, g):
        return( torch.sign(g) * ( g.abs() - self.lam ).float() )
        
    def soft_threshold(self, g):
        return( torch.sign(g) * F.relu( g.abs() - self.lam ) )
    
    def soft_threshold_prime(self, g):
        return( ( g.abs() > self.lam ).float() )
    
    def soft_threshold_nn(self, g):
        return( F.relu( g - self.lam ) )
    
    def soft_threshold_prime_nn(self, g):
        return( ( g > self.lam ).float() )
    
    def __init__(self, latent_dim, obs_dim, K, device, g = "tanh", lam = 0.1, ortho = True, init = None): 
        """g is the interesting setting here. tanh and rbf are suggested by the FastICA paper. 
        l1 is designed to behave like the soft thresholding in l1-regularized regression aka the lasso"""
        self.h = init if (not init is None) else orthonormalize(torch.randn(latent_dim,obs_dim,K).to(device))
        self.orthonormalize = lambda g: orthonormalize(g, ortho)
        self.lam = lam
        if g=="tanh":
            self.g = torch.tanh
            self.g_prime = self.tanh_prime
        elif g=="rbf":
            self.g = self.rbf
            self.g_prime = self.rbf_prime
        elif g == "l1":
            self.g = self.soft_threshold
            self.g_prime = self.soft_threshold_prime
        else:
            self.g = self.soft_threshold_nn
            self.g_prime = self.soft_threshold_prime_nn
        self.term1 = torch.zeros_like(self.h)
        self.term2 = torch.zeros_like(self.h)
        
    def apply_op(self, x, h):
        x_h = F.conv_transpose1d(x, h.transpose(0,1))
        return self.g(x_h)
    
    def accumulate(self,x):
        x_h = F.conv_transpose1d(x, self.h.transpose(0,1))
        net = self.g(x_h)
        self.term1 += F.conv1d(net.transpose(0,1),x.transpose(0,1)) / x.shape[0]
        g_prime_net = self.g_prime(x_h)
        self.term2 += F.conv1d(g_prime_net.transpose(0,1),torch.ones_like(x).transpose(0,1)) / x.shape[0]
    
    def step(self):
        hnew = self.term1 - self.term2 * self.h
        hnew = self.orthonormalize(hnew)
        mae_change = (self.h - hnew).abs().mean()
        self.h = hnew
        self.term1[:] = 0.
        self.term2[:] = 0.
        return(mae_change.item())

class PowerIteration(PowerBase):
    """PowerIteration but for translationally invariant data."""
    
    def __init__(self, latent_dim, obs_dim, K, device, ortho = True, init = None, sparse = False, use_qr = True, **kwargs): 
        """
        latent_dim: number of factors/PCs to extract
        obs_dim: observed dimension (i.e. number of channels)
        K: PWM length aka filter width
        device: cpu or gpu
        ortho: whether to orthonormalize factors at each step
        init: initialize of factors
        sparse: whether to only propagate maximum response
        use_qr: use QR (as opposed to SVD) for orthonormalization
        """
        self.h = init if (not init is None) else orthonormalize(torch.randn(latent_dim, obs_dim, K).to(device))
        self.orthonormalize = lambda g: orthonormalize(g, ortho, use_qr=use_qr)
        self.apply_op = (lambda a,b: apply_op_sparse(a,b,**kwargs)) if sparse else apply_op_full
        self.accumulator = torch.zeros_like(self.h)
        self.loss = 0.
    
    def accumulate(self, x): 
        x_h = self.apply_op(x,self.h) # F.conv_transpose1d(x,h.transpose(0,1)) or sparsified version thereof
        self.accumulator += F.conv1d(x_h.transpose(0,1),x.transpose(0,1))
        fitted = self.deflate_helper(x_h)
        self.loss += F.mse_loss(fitted, x, reduction = "sum")
    
    def step(self):
        hnew = self.orthonormalize(self.accumulator)
        
        hh = self.apply_op(self.accumulator, hnew) # don't remember why this is helpful? presumably only for for H>1
        fitted = torch.conv1d(hh, hnew.transpose(0,1))
        b = torch.dot( self.accumulator.flatten(), fitted.flatten() ) / torch.dot( fitted.flatten(), fitted.flatten() )
        hnew *= torch.sqrt(b)
        
        mae_change = (self.h - hnew).abs().mean()
        self.h = hnew
        self.accum_cache = self.accumulator.clone()
        self.accumulator[:] = 0.
        self.loss_cache = self.loss.detach().item()
        self.loss = 0.
        return(mae_change.item())

class PowerIterationShift(PowerIteration):
    """Extends PowerIterration class above to additionally try to center PWMs"""
    
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        hnew = torch.zeros(self.h.shape[0], self.h.shape[1], self.h.shape[2] + 2, device = self.h.device)
        hnew[:,:,1:-1] = self.h
        self.h = hnew
        self.accumulator = torch.zeros_like(self.h)
    
    def step(self):
        hnew = self.accumulator
        K = hnew.shape[2]
        ones = torch.ones(1, hnew.shape[1], K-2, device = hnew.device)
        ss = F.conv1d(hnew**2, ones)[:,0,:] # sum of squares
        _,ind = ss.max(dim=1) # get positiions with max ss
        for i in range(hnew.shape[0]): # recenter each factor
            hnew[i,:,1:-1] = hnew[i,:,ind[i]:(ind[i]+K-2)] 
        hnew[:,:,0] = 0.
        hnew[:,:,-1] = 0.
        hnew = self.orthonormalize(hnew)
        # assert(hnew[:,:,0].abs().sum().item() < 1e-6)
        mae_change = (self.h - hnew).abs().mean()
        self.h = hnew
        self.accum_cache = self.accumulator.clone()
        self.accumulator[:] = 0.
        return(mae_change.item())
    
    @property
    def weights(self): 
        """Return fitted PCs, including clipping edges"""
        return(self.h[:,:,1:-1])

class AdaOja: 
    """Principled online power iteration. Underperforms offline in my hands."""
    
    def __init__(self, latent_dim, obs_dim, K, device, learning_rate = 1., b0 = 1e-5): 
        self.h = orthonormalize(torch.randn(latent_dim,obs_dim,K).to(device))
        #self.running_gs = torch.full_like(self.h, b0)
        self.running_gs = torch.full([latent_dim], b0, device=device)
        self.learning_rate = learning_rate
        
    def step(self, x):
        x_h = apply_op_full(x,self.h)
        g = F.conv1d(x_h.transpose(0,1),x.transpose(0,1)) / x.shape[0]
        self.running_gs += (g * g).sum((1,2))
        hnew = self.h + self.learning_rate * g / torch.sqrt(self.running_gs[:,None,None])
        self.h = orthonormalize(hnew)

def fit_adaoja(x, inferred_dim, K, device, learning_rate = 0.1, batch_size = 10, epochs = 10):
    optim = AdaOja(inferred_dim, x.shape[1], K, device, learning_rate = learning_rate)
    for i in range(epochs):
        for j in range(0, x.shape[0], batch_size): 
            batch = x[j:j+batch_size,:,:]
            optim.step(x)
    return(optim.h)

def fit_with_deflate(x, pi_factory, latent_dim, **kwargs): 
    """Iteratively fit factors. 
    Coordinate descent extensiion of this didn't converge"""
    
    pi = pi_factory() # make a power iteration object
    assert(pi.h.shape[0]==1)
    pi.fit(x, **kwargs)
    deflater_pi = pi_factory()
    deflater_pi.h = pi.h # store the first factor
    for i in range(1,latent_dim):
        pi = pi_factory()
        pi.fit(x, deflater = deflater_pi.deflate, **kwargs) # fit while removing signal explained by the previous factors
        deflater_pi.h = torch.cat((deflater_pi.h,pi.h), dim=0) # store the newly fitted factor
    return deflater_pi
