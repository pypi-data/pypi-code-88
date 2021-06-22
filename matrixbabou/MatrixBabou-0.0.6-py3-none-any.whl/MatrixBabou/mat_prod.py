
import numpy as np
from numba import prange , jit
import os
import sys
def sh_b(A):
    t=list(np.asarray(A).shape)
    if len(t)==1:
        return t[0],1
    else:
        return t[0],t[1]
@jit(parallel=True,fastmath=True)
def kroneck(A,B):
    n,m = sh_b(A)
    p,k = sh_b(B)
    return np.array([[A[i,j]*B[s,r] for j in prange(m) for r in prange(k)] for i in prange(n) for s in prange(p)])

@jit(parallel=True,fastmath=True)

def hadamrd(A,B):
    n,m=sh_b(A)
    return np.asarray( [[A[i,j]*B[i,j]  for j in prange(m) ] for i in prange(n) ] )
@jit(parallel=True,fastmath=True)
def khatrirao(a,b):
    return  np.vstack([np.kron(a[:, k], b[:, k]) for k in prange(sh_b(b)[1])]).T
    
@jit(parallel=True, fastmath=True)
def LU(A):
    n=len(A)
    U,L= A.copy(),np.eye(n)
    for i in prange(n):
        for j in prange(i+1,n):
            L[j,i]=U[j,i]/U[i,i]
            U[j]=U[j]-L[j,i]*U[i]
    return L,U 
@jit(parallel=True,fastmath=True,nopython=True)
def Cholesky(A):
    n=len(A)
    H=A.copy()
    for i in prange(n-1):
        H[i,i]=np.sqrt(H[i,i])
        H[i+1:n,i]= H[i+1:n,i]/H[i,i]
        for j in prange(i+1,n):
            H[j:n,j]= H[j:n,j]- H[j:n,i]* H[j,i]
    H[-1,-1]=np.sqrt(H[-1,-1])
    H=np.tril(H).T
    return H
@jit(fastmath=True , parallel=True)
def zeros_b(n,m): return np.array([[0 for i in prange(m)] for j in prange(n)])

    
@jit(fastmath=True,parallel=True)
def prod(A,B):
    C=zeros_b(sh_b(A)[0],sh_b(B)[1])
    for i in prange(sh_b(A)[0]):
            for j in prange(sh_b(B)[1]):
                  for k in prange(sh_b(A)[1]):
                    C[i,j]+=[ A[i,k]*B[k,j]
                  
    return C

