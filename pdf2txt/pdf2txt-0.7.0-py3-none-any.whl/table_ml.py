
from sklearn.cluster import AgglomerativeClustering
from tabulate import tabulate
import pandas as pd
import numpy as np
import collections





dist_thresh=24
min_size=2


def extract_table(text_lines, debug=False):
    text_coordinates = []
    raw_text = []


    for line in text_lines:
        for token in line:
            text_coordinates.append((token.left, token.top, token.right, token.bottom))
            raw_text.append(token)

    nb_cols = collections.Counter([len(r) for r in text_lines if len(r)>1]).most_common(1)[0][0]
    cols=cluster_cols(text_coordinates, raw_text, dist_thresh, "left", n_clusers=nb_cols)

    nb_values=sum([1 for col in cols for c in col])
    if nb_values != len(raw_text):
        cols = cluster_cols(text_coordinates, raw_text, dist_thresh, "center")

    nb_values=sum([1 for col in cols for c in col])
    if nb_values != len(raw_text):
        rows = cluster_rows(text_coordinates, raw_text, dist_thresh / 2, "bottom")
        nb_cols=collections.Counter([len(r) for r in rows]).most_common(1)[0][0]
        cols = cluster_cols(text_coordinates, raw_text, dist_thresh, "center", n_clusers=nb_cols)
    rows=cluster_rows(text_coordinates, raw_text, dist_thresh/2, "bottom")
    # extract all x-coordinates from the text bounding boxes, setting the # y-coordinate value to zero

    if len(cols)==0:
        return rows

    m=get_matrix(rows, cols)
    if debug:
        df = pd.DataFrame()
        df=pd.DataFrame(m)

        df.fillna("", inplace=True)
        print(tabulate(df, headers="keys", tablefmt="psql"))

    return m




def cluster_cols(text_coordinates, raw_text, dist_thresh, alogrithm='left', n_clusers=None):


    if alogrithm=="left":
        coordinates = [(c[0], 0) for c in text_coordinates]
    elif alogrithm=="center":
        coordinates = [((c[0]+c[2])/2, 0) for c in text_coordinates]
    elif alogrithm=="left_right":
        coordinates = [(c[0], c[2]) for c in text_coordinates]
    elif alogrithm=="right":
        coordinates = [(c[2], 0) for c in text_coordinates]
    elif alogrithm=="full":
        coordinates = [[c[0], c[2], (c[0]+c[2])/2] for c in text_coordinates]

    else:
        raise ValueError("wrong algorithm in cluster_cols")
    if n_clusers is  not None:
        dist_thresh=None
    clustering = AgglomerativeClustering(
        n_clusters=n_clusers,
        affinity="manhattan",
        linkage="complete",
        distance_threshold=dist_thresh)
    clustering.fit(coordinates)
    # initialize our list of sorted clusters
    sortedClusters = []

    # loop over all clusters
    for l in np.unique(clustering.labels_):
        # extract the indexes for the coordinates belonging to the # current cluster
        idxs = np.where(clustering.labels_ == l)[0]

        # sort the clusters by their average x-coordinate and initialize our
        # data frame
        # verify that the cluster is sufficiently large
        if len(idxs) >= min_size:
            # compute the average x-coordinate value of the cluster and # update our clusters list with the current label and the
            # average x-coordinate
            avg = np.average([coordinates[i][0] for i in idxs])
            sortedClusters.append((l, avg))
    sortedClusters.sort(key=lambda x: x[1])
    df = pd.DataFrame()

    cols = []

    # loop over the clusters again, this time in sorted order
    for (l, _) in sortedClusters:
        # extract the indexes for the coordinates belonging to the # current cluster
        idxs = np.where(clustering.labels_ == l)[0]
        # extract the y-coordinates from the elements in the current
        # cluster, then sort them from top-to-bottom

        yCoords = [text_coordinates[i][1] for i in idxs]

        sortedIdxs = idxs[np.argsort(yCoords)]

        # extract the text for the current column, then construct
        # a data frame for the data where the first entry in our column
        # serves as the header

        cols.append([raw_text[i] for i in sortedIdxs])


    return cols


def cluster_rows(text_coordinates, raw_text, dist_thresh, alogrithm='left', n_clusers=None):


    if alogrithm=="top":
        coordinates = [(c[1], 0) for c in text_coordinates]
    elif alogrithm=="center":
        coordinates = [((c[1]+c[3])/2, 0) for c in text_coordinates]
    elif alogrithm=="top_bottom":
        coordinates = [(c[1], c[3]) for c in text_coordinates]
    elif alogrithm=="bottom":
        coordinates = [(c[3], 0) for c in text_coordinates]
    elif alogrithm=="full":
        coordinates = [[c[1], c[3], (c[1]+c[3])/2] for c in text_coordinates]

    else:
        raise ValueError("wrong algorithm in cluster_cols")
    clustering = AgglomerativeClustering(
        n_clusters=n_clusers,
        affinity="manhattan",
        linkage="complete",
        distance_threshold=dist_thresh)
    clustering.fit(coordinates)
    # initialize our list of sorted clusters
    sortedClusters = []

    # loop over all clusters
    for l in np.unique(clustering.labels_):
        # extract the indexes for the coordinates belonging to the # current cluster
        idxs = np.where(clustering.labels_ == l)[0]

        # sort the clusters by their average x-coordinate and initialize our
        # data frame
        # verify that the cluster is sufficiently large
        if len(idxs) >= min_size:
            # compute the average x-coordinate value of the cluster and # update our clusters list with the current label and the
            # average x-coordinate
            avg = np.average([text_coordinates[i][1] for i in idxs])
            sortedClusters.append((l, avg))

    sortedClusters.sort(key=lambda x: x[1])
    df = pd.DataFrame()

    cols = []

    # loop over the clusters again, this time in sorted order
    for (l, _) in sortedClusters:
        # extract the indexes for the coordinates belonging to the # current cluster
        idxs = np.where(clustering.labels_ == l)[0]
        # extract the y-coordinates from the elements in the current
        # cluster, then sort them from top-to-bottom

        xCoords = [text_coordinates[i][0] for i in idxs]

        sortedIdxs = idxs[np.argsort(xCoords)]

        # extract the text for the current column, then construct
        # a data frame for the data where the first entry in our column
        # serves as the header

        cols.append([raw_text[i] for i in sortedIdxs])


    return cols



def row_index(mat, val, index=0):
    for m in mat:
        try:
            i=m.index(val, index)
            if i is not None:
                return i
        except:
            pass
    return None

def col_index(mat, val, index=0):
    for j, m in enumerate(mat):
        try:
            i=m.index(val, index)
            if i is not None:
                return j
        except:
            pass
    return None


def get_matrix(rows, columns):

    m=defaultlist()
    items=[r for row in  rows for r in row]
    last_i=0
    last_j=0
    for item in items:
        i=col_index(rows, item, last_i)
        j=col_index(columns, item, last_j)
        if i is None or j is None:
            continue
        if i>= len(m):
            m[i]=defaultlist()
        if len(m[i]) > j:
            m[i][j]+=' '+item.Text
        else:
            m[i][j] = item.Text
#        print(i, j, item.Text)

    return m

def get_column_for_item(columns, item):
    for i, column in enumerate(columns):
        if item in column:
            return i
    return None


class defaultlist(list):

   def __setitem__(self, index, value):
      size = len(self)
      if index >= size:
         self.extend(0 for _ in range(size, index + 1))

      list.__setitem__(self, index, value)
