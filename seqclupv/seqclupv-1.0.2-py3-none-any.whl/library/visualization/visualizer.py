"""
    This module contains a class that bundles several approaches to visualize the results of the variations of
    the 'SeqClu' algorithm that are contained in the package.

    NOTE: This class has actually never been used during the research project and therefore needs major modifications
    to make it compatible with the rest of the framework.
"""

import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from IPython import display
import pandas as pd
import seaborn as sns
from sklearn.manifold import TSNE

matplotlib.use("TkAgg")


class Visualizer:

    def __init__(self, classes, distribution, labels, indices, result, data, classDictionary,
                 numPrototypes, numClusters) -> None:
        self.classes = classes
        self.distribution = distribution
        self.labels = labels
        self.numPrototypes = numPrototypes
        self.numClasses = numClusters
        self.indices = indices
        self.result = result
        self.data = data
        self.classDictionary = classDictionary

    def visualizeInputData(self) -> None:
        """
            This method visualizes the input data in two dimensions.

            :return: void
        """
        fig = plt.figure(figsize=(10, 10))
        plt.title('Raw data')
        X_embedded = TSNE(random_state=42, n_components=2).fit_transform(self.distribution)
        # plt.scatter(*X_embedded)
        pal = sns.color_palette("hls", self.numClasses)  # 3 classes, hence 3 colors
        for i, txt in enumerate(self.labels):
            plt.scatter(X_embedded.T[0][i], X_embedded.T[1][i], color=pal[self.classDictionary[txt]])
            plt.annotate(i, (X_embedded.T[0][i], X_embedded.T[1][i]), color=pal[self.classDictionary[txt]], alpha=0.2)
        # Color = class, annotation = Sequence ID
        plt.show()

    def visualizeClustersAsTSNE(self) -> None:
        """
            This method visualizes the clusters as TSNE-graphs.

            :return: void
        """
        fig = plt.figure(figsize=(10, 10))
        plt.title('Clustered data')
        X_embedded = TSNE(random_state=42, n_components=2).fit_transform(self.distribution)
        # plt.scatter(*X_embedded)
        pal = sns.color_palette("hls", len(set(self.result)))
        # ann = [x for x,y in enumerate(X)]
        for i, txt in enumerate(self.indices):
            plt.scatter(X_embedded.T[0][i], X_embedded.T[1][i], color=pal[self.result[i]])
            plt.annotate(txt, (X_embedded.T[0][i], X_embedded.T[1][i]), color=pal[self.result[i]], alpha=0.2)
        plt.show()

    # plt.savefig('clus.png')

    def visualizeClustersAsHeatMaps(self) -> None:
        """
            This method visualizes the clusters as heatmaps.

            :return: void
        """
        # Show clusters as heatmaps (does not work too great for hand-written data)
        clusterdata = [[] for x in range(self.numClasses)]
        for idx, clus in enumerate(self.result):
            clusterdata[clus].append(idx)

        for cnum in range(len(clusterdata)):
            values = [self.distribution[idx] for idx in clusterdata[cnum]]
            fig = plt.figure(figsize=(10, 5))
            df = pd.DataFrame(values, index=clusterdata[cnum])
            plt.title('ClusterStore: ' + str(cnum))
            ax = sns.heatmap(df, center=0.0, xticklabels=False)
            ax.set_yticks(np.arange(len(clusterdata[cnum])))
            ax.set_yticklabels(clusterdata[cnum])
            plt.setp(ax.get_yticklabels(), rotation=0)
            plt.xlabel('Time ->')
            plt.ylabel('Trajectory id')

            plt.show()

    def simulateClusteringProcess(self) -> None:
        """
            This method makes multiple plots that replay the clustering process step-by-step.

            :return: void
        """
        # Simulates how the clustering happened
        # TODO: Fix the extra plots showing up at the end
        X_embedded_ = TSNE(random_state=42, n_components=2).fit_transform(self.distribution)

        for end in range(1, len(self.result)):

            fig = plt.figure(figsize=(18, 10))

            X_embedded = X_embedded_[0:end]
            ann = [x for x, y in enumerate(self.data)][0:end]

            pal = sns.color_palette("hls", len(set(self.result)))

            plt.subplot(1, 2, 1)
            sns.heatmap(self.distribution[0:end], center=0.0)

            plt.subplot(1, 2, 2)
            plt.scatter(X_embedded.T[0], X_embedded.T[1], color=[pal[c] for c in self.result[0:end]])
            for i, txt in enumerate(ann):
                plt.scatter(X_embedded.T[0][i], X_embedded.T[1][i], color=pal[self.result[i]])
                plt.annotate(txt, (X_embedded.T[0][i], X_embedded.T[1][i]), color=pal[self.result[i]])

            display.clear_output(wait=True)
            display.display(plt.gcf())
            time.sleep(0.01)  # change the rate of rendering
