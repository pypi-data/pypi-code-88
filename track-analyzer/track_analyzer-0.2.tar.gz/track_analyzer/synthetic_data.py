##########################################################################
# Track Analyzer - Quantification and visualization of tracking data     #
# Authors: Arthur Michaut                                                #
# Copyright 2016-2019 Harvard Medical School and Brigham and             #
#                          Women's Hospital                              #
# Copyright 2019-2021 Institut Pasteur and CNRS–UMR3738                  #
# See the COPYRIGHT file for details                                     #
#                                                                        #
# This file is part of Track Analyzer package.                           #
#                                                                        #
# Track Analyzer is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# Track Analyzer is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the           #
# GNU General Public License for more details .                          #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with Track Analyzer (COPYING).                                   #
# If not, see <https://www.gnu.org/licenses/>.                           #
##########################################################################

import sys
import os.path as osp
import datetime
import csv
import shutil
import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from skimage import io
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte
import scipy.interpolate as sci
import pickle
import seaborn as sns
from lmfit import Parameters, Model
from scipy.optimize import curve_fit
from scipy import stats
import matplotlib.tri as tri
import napari
import tifffile as tifff


# Plotting parameters
color_list=[c['color'] for c in list(plt.rcParams['axes.prop_cycle'])]+sns.color_palette("Set1", n_colors=9, desat=.5)
plot_param={'figsize':(5,5),'dpi':300,'color_list':color_list,'format':'.png','despine':True,'logx':False,'logy':False,'invert_yaxis':True,'export_data_pts':False}



def make_diff_traj(part_index=0,grid_size=[500,500,500],dim=3,tmax=10,periodic=True,noise_amp=10,x0=[250,250,250],bias=[0,0,0]):
    """Generate a trajectory with a diffusive trajectory, with a bias. bias gives the amplitude at each step along each dimension."""
    #time and index
    t = arange(tmax)
    index = ones(tmax)*part_index
    #displacement
    displacement=pd.DataFrame(np.random.randn(tmax,dim),columns=list('xyz')[0:dim])
    displacement['r2']=0
    for i in range(dim):
        displacement['r2']+=displacement[list('xyz')[i]]**2
    displacement['r']=np.sqrt(displacement['r2'])
    for i in range(dim):
        displacement[list('xyz')[i]]/=displacement['r'] #normalize raw displacement
        displacement[list('xyz')[i]]*=noise_amp #amply amplitude
        displacement[list('xyz')[i]]+=bias[i] #add bias
    displacement=displacement[list('xyz')[0:dim]].values

    #traj
    traj=np.zeros((tmax,dim))
    for i in range(dim):
        traj[:,i]=np.cumsum(displacement[:,i])+x0[i]
        if periodic:
            traj[:,i]=np.remainder(traj[:,i],grid_size[i])
    return pd.DataFrame(np.concatenate([index[:,None],t[:,None],traj],axis=1),columns=['traj','frame']+list('xyz')[0:dim])

def make_spatial_gradient(part_num=100,grid_size=[500,500,500],dim=3,tmax=10,periodic=True,noise_amp=10,bias_basis=[0,0,0],
                         diff_grad={'min':0,'max':10},bias_grad={'min':0,'max':10,'dim':0},grad={'step_num':4,'dim':0}, 
                         x0_range={'x':[0.1,0.9],'y':[0.1,0.9],'z':[0.1,0.9]},dt=1):
    """Make a spatial gradient (number of steps on the gradient given by grad['step_num'})in diffusion or bias, along a specific dimension, given by grad['dim'].
    The gradient can be in diffusion with diff_grad or bias_grad. min and max give the extrema of the gradient, and bias_grad['dim'] give the dimension along the gradient in bias is applied.
    An overall constant bias can be passed by bias_basis. 
    """
    
    df=pd.DataFrame([],columns=['traj','frame']+list('xyz')[0:dim])
    df_param=pd.DataFrame([],columns=['traj','v','D'])
    
    diff_grad_=np.linspace(diff_grad['min'],diff_grad['max'],grad['step_num'])
    bias_grad_=np.linspace(bias_grad['min'],bias_grad['max'],grad['step_num'])
    #spatial boundaries of the regions of particles
    lims=[[x0_range['x'][0]*grid_size[0],x0_range['x'][1]*grid_size[0]],
          [x0_range['y'][0]*grid_size[1],x0_range['y'][1]*grid_size[1]], 
          [x0_range['z'][0]*grid_size[2],x0_range['z'][1]*grid_size[2]]]
    
    part_count=0
    for i in range(grad['step_num']):
        grad_increment=(lims[grad['dim']][1]-lims[grad['dim']][0])/grad['step_num']
        lims_=lims[:]
        lims_[grad['dim']]=[lims_[grad['dim']][0]+i*grad_increment,lims_[grad['dim']][0]+(i+1)*grad_increment]
        noise_amp=diff_grad_[i]
        bias=bias_basis[:]
        bias[bias_grad['dim']]=bias_grad_[i]
        bias_ampl=0
        for k in range(dim):
            bias_ampl+=bias[k]**2
        bias_ampl=np.sqrt(bias_ampl)
        
        for j in range(int(part_num/grad['step_num'])):
            x0=[np.random.uniform(lims_[0][0],lims_[0][1]),
                np.random.uniform(lims_[1][0],lims_[1][1]),
                np.random.uniform(lims_[2][0],lims_[2][1])]
                       
            traj=make_diff_traj(part_index=part_count,noise_amp=noise_amp,x0=x0,bias=bias,tmax=tmax,periodic=periodic,dim=dim)
            df=pd.concat([df,traj])
            v=bias_ampl/dt
            D=noise_amp**2/(2.*dim*dt)
            df_param.loc[part_count,:]=[part_count,v,D]
            
            part_count+=1
    return df,df_param

def make_attraction_node(part_num=100,grid_size=[500,500,500],dim=3,tmax=10,periodic=True,noise_amp=10,bias_basis=[0,0,0], 
                         attraction_ampl=10,node=None,x0_range={'x':[0.1,0.9],'y':[0.1,0.9],'z':[0.1,0.9]},dt=1):
    """Make array of diffusive particles biased toward a node (or away if attraction_ampl is negative)"""
    
    df=pd.DataFrame([],columns=['traj','frame']+list('xyz')[0:dim])
    df_param=pd.DataFrame([],columns=['traj','v','D'])

    if node is None:
        node=[grid_size[d]/2 for d in range(dim)] #by default center

    #spatial boundaries of the regions of particles
    lims=[[x0_range['x'][0]*grid_size[0],x0_range['x'][1]*grid_size[0]],
          [x0_range['y'][0]*grid_size[1],x0_range['y'][1]*grid_size[1]], 
          [x0_range['z'][0]*grid_size[2],x0_range['z'][1]*grid_size[2]]]
    
    for i in range(part_num):
        x0=[np.random.uniform(lims[0][0],lims[0][1]),
            np.random.uniform(lims[1][0],lims[1][1]),
            np.random.uniform(lims[2][0],lims[2][1])]
        
        #unit vector towards node
        node_vec=np.array([node[d]-x0[d] for d in range(dim)])
        sum_=0
        for d in range(dim):
            sum_+=node_vec[d]**2
        node_vec/=np.sqrt(sum_)
        
        bias=node_vec*attraction_ampl
        bias=bias+np.array(bias_basis)
        
        bias_ampl=0
        for k in range(dim):
            bias_ampl+=bias[k]**2
        bias_ampl=np.sqrt(bias_ampl)
        
        traj=make_diff_traj(part_index=i,noise_amp=noise_amp,x0=x0,bias=bias,tmax=tmax,periodic=periodic,dim=dim)
        df=pd.concat([df,traj])
        v=bias_ampl/dt
        D=noise_amp**2/(2.*dim*dt)
        df_param.loc[i,:]=[i,v,D]
        
    return df,df_param

def plot_synthetic_stack(df,outdir,dpi=300,grid_size=[500,500,500],tmax=10):    
    """Plot synthetic data and save it as a grayscaled tiff stack"""
    outdir_temp=osp.join(outdir,'temp')
    safe_mkdir(outdir_temp)

    stack=np.zeros((tmax,grid_size[0],grid_size[1]),'uint8')

    groups=df.groupby('frame')
    #print
    for i in range(tmax):
        group=groups.get_group(i).reset_index(drop=True)
        fig=figure(frameon=False)
        fig.set_size_inches(grid_size[0]/dpi,grid_size[1]/dpi)
        ax = fig.add_axes([0, 0, 1, 1])
        for k in range(group.shape[0]):
            ax.scatter(group.loc[k,'x'],group.loc[k,'y'],s=10)
        ax.set_xlim(0,grid_size[0])
        ax.set_ylim(0,grid_size[1])
        ax.invert_yaxis()
        ax.axis('off')
        fn=osp.join(outdir_temp,'{}.jpg'.format(i))
        fig.savefig(fn,dpi=300)

    #add to stack
    for i in range(tmax):
        fn=osp.join(outdir_temp,'{}.jpg'.format(i))
        im=io.imread(fn,as_gray=True)
        stack[i]=img_as_ubyte(im)

    out_fn=osp.join(outdir,'stack.tiff')
    tifff.imsave(out_fn, stack)
    shutil.rmtree(outdir_temp)


