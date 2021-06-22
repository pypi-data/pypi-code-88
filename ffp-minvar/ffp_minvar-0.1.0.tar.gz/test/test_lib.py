from ffp_minvar import ffp_minvar_lib

import numpy as np

if __name__ == "__main__":

    #---------------- Initialize numbers ----------------#
    
    srng = np.random.RandomState

    N = 500  # number of securities
    K = 4  # number of factors

    # seed for beta and other factor exposures

    seed = np.random.randint(0, 100000)
    seed = 31877
    fmrng = srng(seed)

    ones = np.ones(N)
    IN = np.diag(ones)


    # factor volatilities and variances
    fvol = fmrng.exponential(5, K) / 100
    fvar = fvol ** 2

    # specific variance
    svol = fmrng.uniform(0, 100, N) / 100
    svar = svol ** 2 ## svar: Z
    #print(svar.shape)
    #print(type(svar))
    D = svar
    #D_p = D.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    #print(D_p)

    # construct the factor matrix B
    B = np.zeros((N, K))
    # B = np.random.rand(N,K)
    for k in range(K):
        cents = np.array([0, 1 / 4, 1 / 2, 3 / 4, 1])
        disps = np.array([1 / 8, 1 / 4, 1 / 2, 3 / 4, 1])
        cent = fmrng.choice(cents)
        disp = fmrng.choice(disps)
        sgn = fmrng.choice([-1.0, 1.0])
        beta = fmrng.normal(sgn * cent, disp, N)
        B[:, k] = beta

    V = np.diag(fvar)

    # V = np.random.rand(K,K)
    theta = np.zeros(k)

    # theta = np.random.rand(k,1)
    """
    print("------------ python B ------------")
    print(B)
    print("------------ python V ------------")
    print(V)
    print("------------ python Delta ------------")
    print(D)
    """

    #---------------------- ffp Test ----------------------------#
    print("------------ ffp Test ------------")
    ffp_res = ffp_minvar_lib.ffp(theta, B, V, D)  
    print(ffp_res)
    
    #---------------------- Psi Test ----------------------------#
    print("------------ Psi Test ------------")
    psi_res = ffp_minvar_lib.psi(B, V, D)  
    print(psi_res)
    #---------------------- lo_minvar Test ----------------------------#
    print("------------ lo_minvar Test ------------")
    lo_minvar_res = ffp_minvar_lib.lo_minvar(B, V, D)
    print(lo_minvar_res)