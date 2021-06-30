#!/usr/bin/python
"""! @brief Radial Distribution Analysis"""
##
# @mainpage Neighbour analysis
#
# @section Neighbour Neighbour
# Neighbour (Composition) analysis for MD coordinates
#
# @file neighbour.py
#
# @section todo_neighbour TODO
# - None.

import os, glob
import ctypes 

def neighbour(coord, types, cell, rcut, maxunique=4): 
    '''! Radial Distribution Function between two types of particles for several steps
    density for RDF calculate by number of 2nd particles (len(coord2[0])).
    @param coord XYZ coordinates of particles, format coord[Nstep][Nparticles][Dimension]
    @param types Type of every particle
    @param cell Size of cubic cell
    @param rcut Max radius of RDF
    @param maxunique maximum number molecules type to find (default: 4)

    @return [{
            'composition': {'H': 2, 'e':1},
            'label': 'H2 e1',
            'count': [Nmol[step] for step in range(Nstep)]
            }, ...]
    }
    '''
    # Load Library
    basedir = os.path.abspath(os.path.dirname(__file__))
    libpath = os.path.join(basedir, 'libneighbour*.so')
    libpath = glob.glob(libpath)[0]
    neighbour_ctypes = ctypes.CDLL(libpath)

    # Объявляем структуру в Python аналогичную в C структуре MolInfo
    class MolInfo(ctypes.Structure):
        _fields_ = [('exist', ctypes.c_int),
                    ('typesCount', ctypes.POINTER(ctypes.c_int)),
                    ('quantityByStep', ctypes.POINTER(ctypes.c_int))]

    # Объявляем структуру в Python аналогичную в C структуре MolsInfo
    class MolsInfo(ctypes.Structure):
        _fields_ = [('Maxtypes', ctypes.c_int),
                    ('Maxsteps', ctypes.c_int),
                    ('Maxunique', ctypes.c_int),
                    ('step', ctypes.c_int),
                    ('molInfo', ctypes.POINTER(MolInfo))]

    class SystemState(ctypes.Structure):
        _fields_ = [('Npart', ctypes.c_int),
                    ('Nsteps', ctypes.c_int),
                    ('maxtypes', ctypes.c_int),
                    ('types', ctypes.POINTER(ctypes.c_int)),
                    ('cell', ctypes.c_double),
                    ('r', ctypes.POINTER(ctypes.c_double))]

    # Указываем, что функция возвращает MolsInfo *
    neighbour_ctypes.neighbour.restype = MolsInfo
    # Указываем, что функция принимает аргумент void *
    neighbour_ctypes.neighbour.argtypes = [SystemState, ctypes.c_double, ctypes.c_int]

    
    Nsteps = len(coord)
    Npart = len(coord[0])
    # print (Npart)
    Rpart=[]
    for step in range(Nsteps):
        for idp in range(Npart):
            for dim in range(3):
                Rpart.append(coord[step][idp][dim])
    Rpart_c_double=(ctypes.c_double * (Nsteps*Npart*3)) (*Rpart)
    unique_flag = 0
    Types_label = {}
    types_for_c = []
    for idp in range(Npart):
        if not types[idp] in Types_label:
            Types_label[types[idp]] = unique_flag
            unique_flag+= 1
        types_for_c.append(Types_label[types[idp]])
    maxtypes = unique_flag

    Types_c_int=(ctypes.c_int * (Npart)) (*types_for_c)

    # Создаем структуру
    sysState = SystemState(Npart, Nsteps, maxtypes, Types_c_int, cell, Rpart_c_double)

    # maxunique+1 because we want to add other")
    molsInfo = neighbour_ctypes.neighbour(sysState,rcut, maxunique+1)

    list_of_molecules = {}
    for i in range(molsInfo.Maxunique):
        # print ("molInfo[{:d}]: ".format(i), molsInfo.molInfo[i].exist)
        if (molsInfo.molInfo[i].exist == 0): break
        label = ""
        composition = {}
        count = 0
        for key in Types_label:
            n = molsInfo.molInfo[i].typesCount[Types_label[key]]
            if ( n > 0):
                composition[key] = n
                label += str(key) + str(n) + " "
        # remove last space
        if len(label)>0:
            label = label[:-1]
        count = []
        for step in range(molsInfo.Maxsteps):
            count.append(molsInfo.molInfo[i].quantityByStep[step])
        
        if (i == molsInfo.Maxunique-1):
            label = "unknown"
            composition = []

        list_of_molecules[label] = {
            'composition': composition,
            'count': count
        }

    return list_of_molecules