#!/usr/bin/python
"""! @brief Radial Distribution Analysis"""
##
# @mainpage RDF analysis
#
# @section rdf RDF
# RDF analysis for MD coordinates
#
# @file rdf.py
#
# @section todo_rdf TODO
# - None.

import os, glob
import ctypes 


def rdf_two_types_many_steps(coord1, coord2, cell, rcut, nbins=100): 
    '''! Radial Distribution Function between two types of particles for several steps
    density for RDF calculate by number of 2nd particles (len(coord2[0])).
    @param coord1,coord2 XYZ coordinates of 1,2-nd type particles, format 
        coord[Nstep][Nparticles][Dimension]
    @param cell Size of cubic cell
    @param rcut Max radius of RDF
    @param nbins Number of bins for RDF (dbins=rcut/nbins)

    @return [bins, rdf]
    '''
    # Load Library
    basedir = os.path.abspath(os.path.dirname(__file__))
    libpath = os.path.join(basedir, 'librdf*.so')
    libpath = glob.glob(libpath)[0]
    rdf_ctypes = ctypes.CDLL(libpath)
    Nsteps = len(coord1)
    Npart1 = len(coord1[0])
    Npart2 = len(coord2[0])
    Rpart1=[]
    Rpart2=[]
    for step in range(Nsteps):
        for idp in range(Npart1):
            for dim in range(3):
                Rpart1.append(coord1[step][idp][dim])

    for step in range(Nsteps):
        for idp in range(Npart2):
            for dim in range(3):
                Rpart2.append(coord2[step][idp][dim])

    Rpart1_c_double=(ctypes.c_double * (Nsteps*Npart1*3)) (*Rpart1)
    Rpart2_c_double=(ctypes.c_double * (Nsteps*Npart2*3)) (*Rpart2)
    rdf_c_double = (ctypes.c_double * nbins) ()
    

    rdf_ctypes.rdf.restype = ctypes.c_int
    rdf_ctypes.rdf.argtypes = [ctypes.c_int, ctypes.c_double,
                               ctypes.POINTER(ctypes.c_double),
                               ctypes.c_int, ctypes.c_int, ctypes.c_int,
                               ctypes.POINTER(ctypes.c_double), 
                               ctypes.POINTER(ctypes.c_double), 
                               ctypes.c_double]
    rdf_ctypes.rdf(nbins, rcut, rdf_c_double, Npart1, Npart2, Nsteps,
                                Rpart1_c_double,Rpart2_c_double,cell)
    
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]
    return bins, list(rdf_c_double)

def rdf_one_type_one_step(coord, cell, rcut,nbins):
    # Load Library
    basedir = os.path.abspath(os.path.dirname(__file__))
    libpath = os.path.join(basedir, 'librdf*.so')
    libpath = glob.glob(libpath)[0]
    rdf_ctypes = ctypes.CDLL(libpath)
    '''! Radial Distribution Function between particles for one step only
    @param coord XYZ coordinates of particles, format:
        coord[Nparticles][Dimension]
    @param cell Size of cubic cell
    @param rcut Max radius of RDF
    @param nbins Number of bins for RDF (dbins=rcut/nbins)

    @return [bins, rdf]
    '''
    Npart=len(coord)
    Rpart1_c_double=(ctypes.c_double * (Npart*3)) ()
    Rpart2_c_double=(ctypes.c_double * (Npart*3)) ()
    rdf_c_double = (ctypes.c_double * nbins) ()
    for idp in range(Npart):
        for dim in range(3):
            Rpart1_c_double[idp*3+dim]=coord[idp][dim]
            Rpart2_c_double[idp*3+dim]=coord[idp][dim]
    rdf_ctypes.rdf.restype = ctypes.c_int
    rdf_ctypes.rdf.argtypes = [ctypes.c_int, ctypes.c_double,
                               ctypes.POINTER(ctypes.c_double),
                               ctypes.c_int, ctypes.c_int, ctypes.c_int,
                               ctypes.POINTER(ctypes.c_double), 
                               ctypes.POINTER(ctypes.c_double), 
                               ctypes.c_double]
    rdf_ctypes.rdf(nbins, rcut, rdf_c_double, Npart, Npart, 1,
                                Rpart1_c_double,Rpart2_c_double,cell)
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]
    return bins, list(rdf_c_double)

def get_nearest_axes(r1,r2,cell):
    dx = abs(r2-r1)
    c = int(dx/cell)
    dx = dx - c * cell
    if abs(dx-cell) < abs(dx):
        dx=dx-cell
        
    return dx

def rdf_one_type_one_step_python(coord, cell, rcut,nbins):
    '''! Radial Distribution Function between particles for one step only
    Python Version (SLOW) of rdf_one_type_one_step
    @param coord XYZ coordinates of particles, format:
        coord[Nparticles][Dimension]
    @param cell Size of cubic cell
    @param rcut Max radius of RDF
    @param nbins Number of bins for RDF (dbins=rcut/nbins)

    @return [bins, rdf]
    '''
    N=len(coord)
    rho = N/cell**3
    l_list=[]
    naveraged=0
    for i in range(N):
        for j in range(N):
            r1=coord[i]
            r2=coord[j]
            l_r=0
            for l in range(3):
                l_r +=get_nearest_axes(r1[l],r2[l], cell)**2
            l_r = l_r**0.5
            if (l_r > 0) and (l_r < rcut):
                l_list += [l_r]#get_distances(r1, r2, cell, rcut)
            
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]
    counts = [0 for i in range(nbins)]
    for l in l_list:
        counts[ int(l/dbins) ] += 1
    g_r=[]
    for index in range(len(counts)):
        g_r.append(1.0*(counts[index]/( 4*3.14*(bins[index]**2)*dbins) / rho / N))
    return bins, g_r
