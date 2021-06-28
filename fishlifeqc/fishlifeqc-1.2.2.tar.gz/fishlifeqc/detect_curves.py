
import numpy as np
import matplotlib.pyplot as plt
# from sklearn.mixture import GMM

from sklearn.mixture import GaussianMixture as GMM
from sklearn.mixture import BayesianGaussianMixture as BGMM


N=400
mu, sigma = 0, 0.01
mu2, sigma2 = 0.4, 0.1
X1 = np.random.normal(mu, sigma, N )
X2 = np.random.normal(mu2, sigma2, N)
X = np.concatenate([X1, X2])
plt.hist(X, bins = 50)

test_data = X.reshape(-1,1)
test_data2 = X1.reshape(-1,1)

# nmodes = 2
# GMModel = GMM(n_components = nmodes, covariance_type = 'diag', verbose = 0, tol = 1e-3)


# a = GMModel.fit(X.reshape(-1,1))
# a.score(X.reshape(-1,1))

BGMModel = BGMM(verbose=0, n_components=1, covariance_type='spherical')

b = BGMModel.fit(test_data)

plt.hist(X, bins = 50)

b.score(test_data2)


