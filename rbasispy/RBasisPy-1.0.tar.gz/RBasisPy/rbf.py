import numpy as np
from sklearn.cluster import KMeans

class rbn:

  def __init__(self, K, f='gaussian'):

    self.K = K
    self.f = f

    self.centroids = None
    self.W = None

  def fs(self, r):

    if self.f == 'gaussian':

      return np.exp((-1*(r)**2)/2)
    
    elif self.f == 'inv_sqr':

      return 1/(1+r**2)
    
    elif self.f == 'inv_mul':

      return 1/(np.sqrt(1+r**2))

  def cal_dist(self, X):

    G = np.zeros((X.shape[0], self.K))

    for i in range(self.K):

      for j in range(X.shape[0]):

        G[j, i] = self.fs(np.linalg.norm(X[j, :] - self.centroids[i]))

    return G

  def fit(self, X, Y):

    KM = KMeans(n_clusters=self.K)
    KM.fit(X)

    self.centroids = KM.cluster_centers_

    G = self.cal_dist(X)

    self.W = np.linalg.pinv(G) @ Y

    #return G
  
  def predict(self, X):

    G = self.cal_dist(X)

    return G @ self.W