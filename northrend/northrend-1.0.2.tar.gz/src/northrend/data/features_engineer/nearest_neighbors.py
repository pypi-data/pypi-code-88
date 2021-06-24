from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.neighbors import NearestNeighbors
from multiprocessing import Pool

import numpy as np


class NearestNeighborsFeats(BaseEstimator, ClassifierMixin):
    """
    This class should implement KNN features extraction
    Source: Competitive Data Science
        https://www.coursera.org/learn/competitive-data-science/programming/nh0rT/knn-features-implementation/submission
    """

    def __init__(
        self, n_jobs, k_list, metric, n_classes=None, n_neighbors=None, eps=1e-6
    ):
        self.n_jobs = n_jobs
        self.k_list = k_list
        self.metric = metric

        if n_neighbors is None:
            self.n_neighbors = max(k_list)
        else:
            self.n_neighbors = n_neighbors

        self.eps = eps
        self.n_classes_ = n_classes

    def fit(self, X, y):
        """
        Set's up the train set and self.NN object
        """
        # Create a NearestNeighbors (NN) object. We will use it in `predict` function
        self.NN = NearestNeighbors(
            n_neighbors=max(self.k_list),
            metric=self.metric,
            n_jobs=1,
            algorithm="brute" if self.metric == "cosine" else "auto",
        )
        self.NN.fit(X)

        # Store labels
        self.y_train = y

        # Save how many classes we have
        self.n_classes = (
            np.unique(y).shape[0] if self.n_classes_ is None else self.n_classes_
        )

    def predict(self, X):
        """
        Produces KNN features for every object of a dataset X
        """
        if self.n_jobs == 1:
            test_feats = []
            for i in range(X.shape[0]):
                test_feats.append(self.get_features_for_one(X[i : i + 1]))
        else:

            with Pool(self.n_jobs) as p:
                rows = (X[i : i + 1] for i in range(X.shape[0]))
                test_feats = p.map(self.get_features_for_one, rows)

        return np.vstack(test_feats)

    def get_features_for_one(self, x):
        """
        Computes KNN features for a single object `x`
        """

        NN_output = self.NN.kneighbors(x)

        # Vector of size `n_neighbors`
        # Stores indices of the neighbors
        neighs = NN_output[1][0]

        # Vector of size `n_neighbors`
        # Stores distances to corresponding neighbors
        neighs_dist = NN_output[0][0]

        # Vector of size `n_neighbors`
        # Stores labels of corresponding neighbors
        neighs_y = self.y_train[neighs]

        # We will accumulate the computed features here
        # Eventually it will be a list of lists or np.arrays
        # and we will use np.hstack to concatenate those
        return_list = []

        for k in self.k_list:

            feats = self.calc_feat_label_fractions(neighs_y[:k], self.n_classes)

            assert len(feats) == self.n_classes
            return_list += [feats]

        feats = self.calc_feat_same_label_streak(neighs_y)

        assert len(feats) == 1
        return_list += [feats]

        feats = []
        for c in range(self.n_classes):

            min_distance = self.calc_feat_min_distance(neighs_y, neighs_dist, c)
            feats.append(min_distance)

        assert len(feats) == self.n_classes
        return_list += [feats]

        min_distances = return_list[-1]
        norm_min_distances = self.calc_feat_norm_min_distances(min_distances, self.eps)
        feats = norm_min_distances

        assert len(feats) == self.n_classes
        return_list += [feats]

        for k in self.k_list:

            feat_51 = neighs_dist[k - 1]
            feat_52 = feat_51 / (neighs_dist[0] + self.eps)

            return_list += [[feat_51, feat_52]]

        feats = []
        for k in self.k_list:

            feats = self.calc_feat_mean_distances(
                neighs_y[:k], neighs_dist[:k], self.eps, self.n_classes
            )

            assert len(feats) == self.n_classes
            return_list += [feats]

        # merge
        knn_feats = np.hstack(return_list)

        return knn_feats

    @staticmethod
    def calc_feat_label_fractions(neighs_y, n_classes):
        """
        1. Fraction of objects of every class.
           It is basically a KNNСlassifiers predictions.

           Note that the values should sum up to one
        """
        feats_count = np.bincount(neighs_y, minlength=n_classes)
        feats = feats_count / feats_count.sum()

        np.testing.assert_almost_equal(sum(feats), 1.0)
        return feats

    @staticmethod
    def calc_feat_same_label_streak(arr):
        """
        2. Same label streak: the largest number N,
           such that N nearest neighbors have the same label.

           What can help you: `np.where`
        """
        assert len(arr) > 0
        first_label = arr[0]
        cnt = 0

        for num in arr:
            if num == first_label:
                cnt += 1
            else:
                break

        return [cnt]

    @staticmethod
    def calc_feat_min_distance(neighs_y, neighs_dist, class_idx):
        """
        3. Minimum distance to objects of each class
           Find the first instance of a class and take its distance as features.

           If there are no neighboring objects of some classes,
           Then set distance to that class to be 999.

           `np.where` might be helpful
        """
        distances_to_class = np.where(neighs_y == class_idx, neighs_dist, 999)
        min_distance = np.min(distances_to_class)
        return min_distance

    @staticmethod
    def calc_feat_norm_min_distances(min_distances, eps):
        """
        4. Minimum *normalized* distance to objects of each class
           As 3. but we normalize (divide) the distances
           by the distance to the closest neighbor.

           If there are no neighboring objects of some classes,
           Then set distance to that class to be 999.

           Do not forget to add self.eps to denominator.
        """
        min_distances = np.array(min_distances)
        min_distance = np.min(min_distances)
        norm_factor = min_distance + eps
        norm_min_distances = np.where(
            min_distances != 999, min_distances / norm_factor, 999
        )
        return norm_min_distances

    @staticmethod
    def calc_feat_mean_distances(neighs_y, neighs_dist, eps, n_classes):
        """
        6. Mean distance to neighbors of each class for each K from `k_list`
               For each class select the neighbors of that class among K nearest neighbors
               and compute the average distance to those objects

               If there are no objects of a certain class among K neighbors, set mean distance to 999

           You can use `np.bincount` with appropriate weights
           Don't forget, that if you divide by something,
           You need to add `self.eps` to denominator.
        """
        bin_counts = np.bincount(neighs_y, minlength=n_classes)
        sum_dist = np.bincount(neighs_y, minlength=n_classes, weights=neighs_dist)
        mean_distances = sum_dist / (bin_counts + eps)
        mean_distances = np.where(bin_counts == 0, 999, mean_distances)
        return mean_distances
