import perpy as py
import copy
import numpy as np
from sklearn import metrics as mt

def NMI(labels_true, labels_pred):
    return mt.normalized_mutual_info_score(labels_true, labels_pred)

def ARI(labels_true, labels_pred):
    return mt.adjusted_rand_score(labels_true, labels_pred)

def ACC(labels_true, labels_pred):
    return mt.accuracy_score(labels_true, labels_pred)

def AMI(labels_true, labels_pred):
    return mt.adjusted_mutual_info_score(labels_true, labels_pred)

def Completeness(labels_true, labels_pred):
    return mt.completeness_score(labels_true, labels_pred)

def Homogeneity(labels_true, labels_pred):
    return mt.homogeneity_score(labels_true, labels_pred)

def k_means(x, k, max_iterations=None):
    num_x = x.shape[0]
    num_feature = x.shape[1]
    index = np.random.choice(np.arange(num_x), size=k, replace=False)
    centers = x[index]
    labels = np.zeros(num_x)

    if max_iterations is None:
        while True:
            centers_old = copy.deepcopy(centers)

            for i in range(num_x):
                min_value = 999
                for j in range(k):
                    if py.dist(x[i], centers[j]) < min_value:
                        min_value = py.dist(x[i], centers[j])
                        labels[i] = j

            for i in range(k):
                for d in range(num_feature):
                    sum_value = 0.0
                    count = 0
                    for j in range(num_x):
                        if labels[j] == i:
                            sum_value += x[j, d]
                            count += 1
                    mean = sum_value / count
                    centers[i, d] = mean
            if centers.all() == centers_old.all():
                break

    else:
        for i in range(max_iterations):
            centers_old = copy.deepcopy(centers)

            for i in range(num_x):
                min_value = 999
                for j in range(k):
                    if py.dist(x[i], centers[j]) < min_value:
                        min_value = py.dist(x[i], centers[j])
                        labels[i] = j

            for i in range(k):
                for d in range(num_feature):
                    sum_value = 0.0
                    count = 0
                    for j in range(num_x):
                        if labels[j] == i:
                            sum_value += x[j, d]
                            count += 1
                    mean = sum_value / count
                    centers[i, d] = mean
            if centers.all() == centers_old.all():
                break

    return labels, centers