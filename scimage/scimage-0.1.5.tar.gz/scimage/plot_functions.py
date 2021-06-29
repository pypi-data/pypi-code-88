#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The following functions can be used to test the results
by plotting the dectected local peak points and highlighting the points 
of each current-sheet, all painted over the image of the simulation results
"""

import numpy as np
import matplotlib.pyplot as plt
from scimage.file_functions import (create_folder)

# Plotting detected local peak point
def plot_locations_of_local_maximas(x, y, jz, J_th, indexes_of_local_jzmax):
    """
    Plotting detected local peak point

    Returns
    -------
    None.

    """
    x_indices=[index[0] for index in indexes_of_local_jzmax]
    y_indices=[index[1] for index in indexes_of_local_jzmax]

    #partial_deriv_of_jzmagnitude_in_x, partial_deriv_of_jzmagnitude_in_y=\
    #    np.gradient(np.abs(jz),x[2]-x[1],y[2]-y[1])
    #magnitude_of_gradient_of_jzmagnitude=\
    #    np.sqrt(partial_deriv_of_jzmagnitude_in_x**2+partial_deriv_of_jzmagnitude_in_y**2)
    plt.rcParams["figure.figsize"] = (10, 8)
    plt.figure()
    plt.ion()
    #plt.pcolor(x,y,np.abs(jz)-J_th,cmap='bwr',vmin=-3*J_th,vmax=3*J_th)    
    #plt.pcolor(x,y, jz, cmap='bwr', vmin=np.min(jz), vmax=np.max(jz))
    plt.pcolor(x, y, jz, cmap='bwr', vmin=np.min(jz), vmax=np.max(jz), shading='auto')
    #plt.pcolor(jz, cmap='bwr', vmin=-0.9999, vmax=0.999, shading='auto')
    #plt.pcolor(x,y, np.abs(jz), cmap='bwr',vmin=-10,vmax=10)
    
    #contour_values=20#np.linspace(0,1.1,25)
    #plt.contourf(x,y,np.abs(jz)-J_th,contour_values,color='k',cmap='bwr',\
    #             vmin=-3*J_th,vmax=3*J_th)
    plt.colorbar()
    plt.plot(y[y_indices],x[x_indices],'xk', markersize=6)#,\
    #plt.plot(y_indices, x_indices, 'xk', markersize=6)
    
    plt.xlabel('$x$',fontsize=17)
    plt.ylabel('$y$',fontsize=17)
    #plt.xlim([0,50])
    #plt.ylim([-128,-50])
    #plt.title(r'(color) $|J_z|-J_{th}$, (x) identified points of local maxima')    
    plt.title('Identified points of maxima',fontsize=17)    
    plt.show()

# Plotting all the detected regions (e.g. current sheets in a plasma)
def plot_locations_of_region_points(x,y,jz,J_th,indexes_of_points_of_all_cs):
    """
    Plotting all the detected regions (e.g. current sheets in a plasma)

    Returns
    -------
    None.
    """
    
    plt.rcParams["figure.figsize"] = (10, 8)
    plt.figure()
    plt.ion()
    #plt.subplot(2,1,1)
    #plt.pcolor(x,y,np.abs(jz)-J_th,cmap='bwr',vmin=-0.5,vmax=0.5)
    #plt.pcolor(x,y, jz, cmap='bwr', vmin=np.min(jz),vmax=np.max(jz))
    #plt.colorbar()
    #plt.title(r'(color) $J_z$, (.) Identified points of current sheets')
    #plt.subplot(2,1,2)
    #plt.pcolor(x,y,np.abs(jz)-J_th,cmap='bwr',vmin=-0.5,vmax=0.5)
    plt.pcolor(x,y, jz, cmap='bwr', vmin=np.min(jz), vmax=np.max(jz), shading='auto')
    #plt.contourf(x,y,jz,20,cmap='bwr',vmin=-0.5,vmax=0.5)
    plt.colorbar()
    #plt.contour(x,y,jz,[0.42*np.max(jz)])
    for indexes_of_points_of_a_cs in indexes_of_points_of_all_cs:
        x_indices=[index[0] for index in indexes_of_points_of_a_cs]
        y_indices=[index[1] for index in indexes_of_points_of_a_cs]

        plt.plot(y[y_indices], x[x_indices], 'ok', markersize=6, alpha=0.1)

    plt.xlabel('$x$',fontsize=17)
    plt.ylabel('$y$',fontsize=17)
    plt.title('Detected regions (e.g. current sheets)',
              fontsize=17)
    plt.show()

# Plot one region of the whole image
def plot_region(coordinates_x_in_frame, coordinates_y_in_frame, values_of_frame,
               line_p1, line_p2):
    fig, ax = plt.subplots()
    ax.pcolormesh(coordinates_y_in_frame, coordinates_x_in_frame, values_of_frame, 
                  alpha=0.8, zorder=1, shading='auto')
    ax.plot([line_p1[1], line_p2[1]], [line_p1[0], line_p2[0]], 
            linewidth=3, zorder=2 , color='black')
    plt.show()

def save_region_image(coordinates_x_in_frame, coordinates_y_in_frame, values_of_frame, 
                     line_p1, line_p2,
                     sheet_index, target_folder):
    plt.ioff() # Call this, so that it does not display on screen in console

    fig, ax = plt.subplots()
    ax.pcolormesh(coordinates_y_in_frame, coordinates_x_in_frame, values_of_frame, 
                  alpha=0.8, zorder=1, shading='auto')
    ax.plot([line_p1[1], line_p2[1]], [line_p1[0], line_p2[0]], 
            linewidth=3, zorder=2 , color='black')

    create_folder(target_folder)
    plt.savefig(target_folder + '/'+ str(sheet_index)+'.png', bbox_inches="tight", dpi=90)
    plt.close()
