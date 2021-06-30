from ctypes import *
import ctypes
from pathlib import Path
import numpy as np

# helper function to help convert numpy array to 
# the double** in c functions
def ndarr2ptrs(arr):
    if(arr.ndim == 2):
        row = arr.shape[0]
        col = arr.shape[1]
        dest = ((ctypes.c_double * col) * row) ()
        temp = (POINTER(c_double) * row) ()
        for i in range(row):
            for j in range(col):
                dest[i][j] = arr[i][j]

        for i in range(row):
            temp[i] = dest[i]
    else:
        row = 1
        col = arr.shape[0]

        dest = ((ctypes.c_double * col) * row) ()
        temp = (POINTER(c_double) * row) ()

        for i in range(row):
            for j in range(col):
                dest[i][j] = arr[j]

        for i in range(row):
            temp[i] = dest[i]

    return temp

# check matrix if diagonal
def isdiag(a):
    m = a.shape[0]
    p,q = a.strides
    diag = ((np.lib.stride_tricks.as_strided(a[:,1:], (m-1,m), (p+q,q)))==0).all()
    return diag
"""
input: 
    theta: np.zeros
    B: ndarray
    V: ndarray
    Delta: ndarray
output: 
"""
# theta need to be created as np.zeros(shape=(K,1))
def ffp(theta, B, V, Delta):
    # V must be diagonal
    if not isdiag(V):
        raise ValueError("Current mattrix V is not diagonal. Please use a diagonal V.")

    theta_ctype = theta.ctypes.data_as(POINTER(ctypes.c_double))
    B_ctype = ndarr2ptrs(B)
    V_ctype = ndarr2ptrs(V)
    Delta_ctype = Delta.ctypes.data_as(POINTER(ctypes.c_double))
    
    int_p = B.shape[0]
    int_q = B.shape[1]

    p = ctypes.c_int(int_p)
    q = ctypes.c_int(int_q)

    # Load the shared library into ctypes
    libname = Path(__file__).parent.absolute() / "alg_lomv.so"
    alg_lib = ctypes.CDLL(libname)
    ffp_C_interface = alg_lib.ffp_C_interface
    ffp_C_interface.restype = POINTER(c_double)

    ffp_res = ffp_C_interface(p, q, theta_ctype, B_ctype, V_ctype, Delta_ctype)
    ffp_nparray = np.empty(int_q, dtype=float)

    for i in range(int_q):
        ffp_nparray[i] = ffp_res[i]
    
    return ffp_nparray


def lo_minvar(B, V, Delta):
    # V must be diagonal
    if not isdiag(V):
        raise ValueError("Current mattrix V is not diagonal. Please use a diagonal V.")

    B_ctype = ndarr2ptrs(B)
    V_ctype = ndarr2ptrs(V)
    Delta_ctype = Delta.ctypes.data_as(POINTER(ctypes.c_double))
    
    int_p = B.shape[0]
    int_q = B.shape[1]

    p = ctypes.c_int(int_p)
    q = ctypes.c_int(int_q)

    # Load the shared library into ctypes
    libname = Path(__file__).parent.absolute() / "alg_lomv.so"
    alg_lib = ctypes.CDLL(libname)
    lo_minvar_C_interface = alg_lib.lo_minvar_C_interface
    lo_minvar_C_interface.restype = POINTER(c_double)
    
    lo_minvar_res = lo_minvar_C_interface(p, q, B_ctype, V_ctype, Delta_ctype)
    lo_minvar_nparray = np.empty(int_p, dtype=float)

    for i in range(int_p):
        lo_minvar_nparray[i] = lo_minvar_res[i]
    
    return lo_minvar_nparray


def psi(B, V, Delta):
    # V must be diagonal
    if not isdiag(V):
        raise ValueError("Current mattrix V is not diagonal. Please use a diagonal V.")

    B_ctype = ndarr2ptrs(B)
    V_ctype = ndarr2ptrs(V)
    Delta_ctype = Delta.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    
    int_p = B.shape[0]
    int_q = B.shape[1]

    p = ctypes.c_int(int_p)
    q = ctypes.c_int(int_q)
    
    # Load the shared library into ctypes
    libname = Path(__file__).parent.absolute() / "alg_lomv.so"
    alg_lib = ctypes.CDLL(libname)
    psi_C_interface = alg_lib.psi_C_interface    
    psi_C_interface.restype = POINTER(c_double)

    psi_res = psi_C_interface(p, q, B_ctype, V_ctype, Delta_ctype) #__main__.LP_LP_c_double object
    psi_nparray = np.empty(int_q, dtype=float)
    
    for i in range(int_q):
        psi_nparray[i] = psi_res[i]
    
    return psi_nparray

