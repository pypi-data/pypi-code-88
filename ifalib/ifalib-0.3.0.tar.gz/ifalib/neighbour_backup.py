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


def neighbour(coord, types, cell, rcut, maxunique): 
    '''! Radial Distribution Function between two types of particles for several steps
    density for RDF calculate by number of 2nd particles (len(coord2[0])).
    @param coord XYZ coordinates of particles, format coord[Nstep][Nparticles][Dimension]
    @param types Type of every particle
    @param cell Size of cubic cell
    @param rcut Max radius of RDF
    @param maxunique maximum number molecules type to find

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
                    ('molInfo', ctypes.c_void_p),]

    class SystemState(ctypes.Structure):
        _fields_ = [('N', ctypes.c_int),
                    ('types', ctypes.POINTER(ctypes.c_int)),
                    ('r', ctypes.POINTER(ctypes.c_double))]

    # Указываем, что функция возвращает MolsInfo *
    neighbour_ctypes.neighbour.restype = ctypes.POINTER(MolsInfo)
    # Указываем, что функция принимает аргумент void *
    neighbour_ctypes.neighbour.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]

    
    Nsteps = len(coord)
    Npart = len(coord[0])
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
    maxtypes = unique_flag - 1

    Types_c_int=(ctypes.c_int * (Nsteps*Npart*3)) (*types_for_c)
    # Создаем структуру
    sysState = SystemState(Npart, Types_c_int, Rpart_c_double)

    # maxunique+1 because we want to add other")
    molsInfo = neighbour_ctypes.neighbour(Nsteps, ctypes.byref(sysState), cell, rcut, maxunique+1, maxtypes)
    return 0 #TODO
    list_of_molecules = []
    for i in range(molsInfo.Maxunique):
        if (molsInfo.molInfo[i].exist == 0): break
        label = ""
        composition = {}
        for key in Types_label:
            n = molsInfo.molInfo[i].types[Types_label[key]]
            if ( n > 0):
                composition[key] = n
                label += key + str(n) + " "
        count = list(molsInfo.molInfo[i].quantityByStep)
        list_of_molecules.append({
            'label': label,
            'composition': composition,
            'count': count
        })

    return list_of_molecules