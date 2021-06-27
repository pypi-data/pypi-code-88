import torch
import torch.nn as nn
import torch.utils.data
import torch.nn.functional as F
from contextlib import suppress
import math

import collections

import numpy as np

from conv_pca import pool_unpool


class AE_base(nn.Module):
    """Auto-encoder base class"""
    
    def __init__(self):
        super().__init__()

    def fit(self, x, steps = 100, batch_size = None):
        """Train on the data in x using Adam/SGD"""

        if not batch_size: batch_size = x.shape[0]
        
        optim = torch.optim.Adam(self.parameters(), amsgrad=True)

        for i in range(steps): # TODO: add a sensible stopping criterion
            for j in range(0, x.shape[0], batch_size): 
                batch = x[j:j+batch_size,:,:]
                h,o = self(batch)
                loss = F.mse_loss(o,batch) + self.l1 * h.abs().mean()
                loss.backward()
                optim.step()
                optim.zero_grad()
    
    def lbfgs(self, x, verbose = False, **kwargs):
        """Train on the data in x using LBFGS (full data) optimization"""
        
        if not "history_size" in kwargs: kwargs["history_size"] = 20
        if not "line_search_fn" in kwargs: kwargs["line_search_fn"] = 'strong_wolfe'
        if not "max_iter" in kwargs: kwargs["max_iter"] = 10000

        optim = torch.optim.LBFGS(self.parameters(), **kwargs)

        evals = 0
        def closure():
            nonlocal evals
            optim.zero_grad()
            h,o = self(x)
            loss = F.mse_loss(o,x) + self.l1 * h.abs().mean()
            loss.backward()
            evals += 1
            if verbose: print("%i %.3g        " % (evals, loss.item()), end = "\n")
            return loss

        optim.step(closure)

class AE(AE_base):
    """Convolutional single-layer autoencoder."""
    
    def __init__(self, latent_dim, obs_dim, k, sparse = False, flipped = True, activation = lambda g: g, l1 = 0.,  **kwargs):
        """
        latent_dim: number of hidden channels
        obs_dim: observed num channels
        k: filter width
        sparse: whether to 0 out non-maximal entries in windows (details specified by **kwargs)
        flipped: `normal` AEs do Conv -> TransposedConv. Flipped means doing TransposedConv -> Conv (makes more sense imo).
        activation: linear by default. 
        l1: l1 penalty on parameters
        """
        super().__init__()
        self.encoder = (nn.ConvTranspose1d if flipped else nn.Conv1d)(obs_dim, latent_dim, k, padding=0)
        self.decoder = (nn.Conv1d if flipped else nn.ConvTranspose1d)(latent_dim, obs_dim, k, bias = False, padding=0)
        self.sparse = (lambda x: pool_unpool(x, **kwargs)) if sparse else False
        self.activation = activation
        self.l1 = l1

    def forward(self, x):
        """Forward pass through whole model. Returns hidden and output"""
        h = self.encoder(x)
        if self.sparse: h = self.sparse(h)
        h = self.activation(h)
        return(h,self.decoder(h))
    
    @property
    def decoder_weights(self):
        return self.decoder.weight.detach().transpose(0,1)
    
    @property
    def encoder_weights(self):
        return self.encoder.weight.detach().transpose(0,1)

class flipped_AE_tied_weights(AE_base):
    """Convolutional single-layer autoencoder with weights tied between encoder and decoder."""
    
    def __init__(self, latent_dim, obs_dim, k, sparse = False, activation = lambda g: g, l1 = 0., **kwargs):
        super().__init__()
        self.decoder = nn.Conv1d(latent_dim, obs_dim, k, bias=False, padding=0)
        self.sparse = (lambda x: pool_unpool(x, **kwargs)) if sparse else False
        self.activation = activation
        self.l1 = l1
        
    def forward(self, x):
        h = nn.functional.conv_transpose1d(x, 
                                           weight=self.decoder.weight,
                                           stride=1, 
                                           padding=0)
        if self.sparse: h = self.sparse(h)
        h = self.activation(h)
        return(h,self.decoder(h))
    
    @property
    def encoder_weights(self):
        return self.decoder.weight.detach().transpose(0,1) # [ w.detach() for w in self.parameters() ][0]
    
    @property
    def decoder_weights(self):
        return self.encoder_weights
    
class AE_tied_weights(AE_base):
    """Convolutional single-layer autoencoder with weights tied between encoder and decoder."""
    
    def __init__(self, latent_dim, obs_dim, k, sparse = False, activation = lambda g: g, l1 = 0., **kwargs):
        super().__init__()
        self.encoder = nn.Conv1d(obs_dim, latent_dim, k, bias=False, padding=0)
        self.sparse = (lambda x: pool_unpool(x, **kwargs)) if sparse else False
        self.activation = activation
        self.l1 = l1
        
    def forward(self, x):
        h = self.encoder(x)
        if self.sparse: h = self.sparse(h)
        h = self.activation(h)
        y = nn.functional.conv_transpose1d(h, 
                                           weight=self.encoder.weight, # reverse? 
                                           stride=1, 
                                           padding=0)
        return(h,y)
    
    @property
    def encoder_weights(self):
        return self.encoder.weight.detach() # [ w.detach() for w in self.parameters() ][0]
    
    @property
    def decoder_weights(self):
        return self.encoder_weights

def ae_factory(latent_dim, obs_dim, k, tied = True, flipped = True, **kwargs):
    """Function to create """
    if tied: 
        ae = (flipped_AE_tied_weights if flipped else AE_tied_weights)(latent_dim, obs_dim, k, **kwargs)
    else: 
        ae = AE(latent_dim, obs_dim, k, flipped = flipped, **kwargs)
    return(ae)
