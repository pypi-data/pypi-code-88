"""Class to compute various Multi-Stat like 
MoN (Median of Means) and other derivative 
statistics
"""

import numpy as np

class NotEnoughValue(Exception):
    pass




#for gmon

def gini(array):
    """Calculate the Gini coefficient of a numpy array."""
    # based on bottom eq: http://www.statsdirect.com/help/content/image/stat0206_wmf.gif
    # from: http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    array = array.flatten() #all values are treated equally, arrays must be 1d
    if np.amin(array) < 0:
        array -= np.amin(array) #values cannot be negative
    array += 0.0000001 #values cannot be 0
    array = np.sort(array) #values must be sorted
    index = np.arange(1,array.shape[0]+1) #index per array element
    n = array.shape[0]#number of array elements
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array))) #Gini coefficient


def create_k_means(samples, k=11):
    
    if len(samples) < k:
        raise NotEnoughValue("Need at least", k, "samples...")

    means = []
    counters = []
    
    for i in range(k):
        means.append(0)
        counters.append(0)
        
    index = 0
    # On ajoute chaque échantillon dans un paquet uniformément
    for s in samples:
        
        means[index] += s
        counters[index] += 1
        
        index += 1
        
        # on cible bien le paquet en question et on éviter de sortir de k
        if index >= k:
            index = 0
            
    # on calcule les k moyennes finales relativement aux échantillons dispatchés
    current_means = []  
    for i in range(k):        
        if counters[i] != 0:
           current_means.append(means[i] / counters[i])
           
    return current_means


def gmon(means, nexpected=11, giniv=0.5):
    
    n = len(means)
    mIndex = int(len(means) / 2)
    
    meansSorted = sorted(means)
    
    meanSum = meansSorted[mIndex]
    weightSum = 1
    
    if n < nexpected:
        return np.median(meansSorted)
    
    for i in range(1, int(mIndex * giniv) + 1):
        
        meanSum += meansSorted[mIndex - i]
        meanSum += meansSorted[mIndex + i]
        weightSum += 2

    return meanSum / weightSum

def gmon_value(data, k=13):
    k_means = create_k_means(data, k)
    giniv = gini(np.array(k_means))
    return gmon(k_means, len(k_means), giniv)   




def abmm(sample: np.array, alpha: float = 1) -> float:
    """Calculates deterministic approximation to BMM to estimate the mean of a sample.
    (from Paulo Orenstein)

    Args:
        sample (np.array): Array with observed samples.
        alpha (float): Interpolation parameter between mean (alpha -> infty) and median (alpha -> 0).

    Returns:
        float: Mean estimate.
    """
    sample_mean = sample.mean()
    correction = (1 / (3*alpha*len(sample))) * np.sum((sample - sample_mean)**3) / np.sum((sample - sample_mean)**2)
    abmm = sample_mean - correction
    return abmm

def MoN(data, chunks=3):
        """
        Compute Median of meaNs

        Arguments:
        chunks: {int} -- number of chunks

        Returns:
        {float} -- Returns the Medians of meaNs

        Example :
            >>> from MONarchy.MONarchy import *
            >>> MoN([1,2,3,4,5,6000])
            3.5
        """
        
        g = np.array_split(data, chunks)
        means = []
        for array in g:
            means.append(np.mean(array))
        return np.median(means)  





def bin_gmon(data, k=13, threshold=0.25):
    """
    Compute binary Gini MoN (see : The paper whose name cannot be pronounced )

    Arguments:
    chunks: {int} -- number of chunks

    Returns:
    {float} -- Returns the Medians of meaNs

    Example :
        >>> from MONarchy.MONarchy import *
        >>> MoN([1,2,3,4,5,6000])
        3.5
    """
    k_means = create_k_means(data, k)
    giniv = gini(np.array(k_means))
    if (giniv < threshold):
        return np.mean(data)
    else :
        return MoN(data,k)


class MONarchy():
    """A Class to rule them all"""

    def __init__(self, data):
        """
        MONarchy constructor

        Attributes:
            data: {float} list of numericals values
        """
        self.data = data
        

    def MoN(self, chunks=3):
        """
        Compute Median of meaNs

        Arguments:
        chunks: {int} -- number of chunks

        Returns:
        {float} -- Returns the Medians of meaNs

        Example :
            >>> from MONarchy.MONarchy import *
            >>> stat = MONarchy([1,2,3,4,5,6])
            >>> stat.MoN()
            3.5
        """
        return MoN(self.data, chunks)
        
    def size(self):
        """
        Return the number of values 

        Returns:
        {int} -- Returns the number of values

        Example :
            >>> from MONarchy.MONarchy import MONarchy
            >>> stat = MONarchy([1,2,3,4,5,6]*5)
            >>> stat.size()
            30
        """

        return len(self.data)  

    def GMoN(self, k=13):
        """
        Compute Gini Median of meaNs

        Arguments:
        chunks: {int} -- number of chunks

        Returns:
        {float} -- Returns the Binary Medians of meaNs

        Example :
            >>> from MONarchy.MONarchy import MONarchy
            >>> stat = MONarchy([1,2,3,4,5,6]*10)
            >>> stat.GMoN()
            3.5
        """
        return gmon_value(self.data,k)

    def abmm(self, alpha: float = 1):
        """Calculates deterministic approximation to BMM to estimate the mean of a sample.

        Args:
            alpha (float): Interpolation parameter between mean (alpha -> infty) and median (alpha -> 0).

        Returns:
            float: Mean estimate.

        Example :
            >>> from MONarchy.MONarchy import MONarchy
            >>> stat = MONarchy([1,2,3,4,5,6]*10)
            >>> stat.abmm()
            3.5
         """
        return abmm(np.array(self.data))

    def Bin_GMoN(self, k=13):
        """
        Compute Binary Gini Median of meaNs

        Arguments:
        chunks: {int} -- number of chunks

        Returns:
        {float} -- Returns the Binary Gini Medians of meaNs

        Example :
            >>> from MONarchy.MONarchy import MONarchy
            >>> stat = MONarchy([1,2,3,4,5,6]*10)
            >>> stat.GMoN()
            3.5
        """
        return gmon_value(self.data,k)
              
        
