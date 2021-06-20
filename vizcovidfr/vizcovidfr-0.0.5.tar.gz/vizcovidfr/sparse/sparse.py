# ---------- requirements ----------
import time
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import geopandas as gpd
from scipy.sparse import isspmatrix

# local req
from vizcovidfr.loads import load_datasets


def sparse_graph(directed=False, show=True):
    """
    Plot and return the graph of the transfer of patient with Covid-19,
    inside or outside France.

    **Note:**
    Try to first plot the undirected graph to see if you can guess the
    direction of the arrows, then check by calling the function with
    *directed=True* !

    Parameters
    ----------

    :param directed: whether we want the graph to be directed or not
    :type directed: bool, optional, default=False)
    :param show: whether or not to show the graph
    :type show: bool, optional, default=True

    Returns
    -------

    :return: the transfer graph and a plot of its representation
    :rtype:
        - networkx.classes.graph.Graph (if directed=False)
        - networkx.classes.digraph.DiGraph (if directed=True)

    :Examples:

    >>> sparse_graph()

    >>> sparse_graph(directed=True)
    """
    start = time.time()
    raw_transfer = load_datasets.Load_transfer().save_as_df()
    raw_transfer['region_arrivee'] = raw_transfer['region_arrivee'].replace(
                                                np.nan, 'outside France')
    # keep only relevent information
    transfer = raw_transfer[['region_depart',
                             'region_arrivee',
                             'nombre_patients_transferes']]
    # make a graph out of the transfer dataframe,
    if (directed):
        word = 'Directed'
        good_seed = 1133311  # it's a palindromic number!
        G = nx.from_pandas_edgelist(transfer, 'region_depart',
                                              'region_arrivee',
                                              'nombre_patients_transferes',
                                              create_using=nx.DiGraph())
    else:
        word = 'Undirected'
        good_seed = 41
        G = nx.from_pandas_edgelist(transfer, 'region_depart',
                                              'region_arrivee',
                                              'nombre_patients_transferes',
                                              create_using=nx.Graph())
    # ---------- plot graph ----------
    plt.figure(figsize=(13, 9))
    # set (good) seed for orientation purpose
    # draw graph
    nx.draw_networkx(G, with_labels=True,
                     pos=nx.spring_layout(G, seed=good_seed),
                     node_color='#d51e3999',
                     edge_color='#cc901699',
                     font_size=11)

    # extract edge 'weights' (i.e. number of transfered patients)
    labels = nx.get_edge_attributes(G, "nombre_patients_transferes")
    # add weights labels
    nx.draw_networkx_edge_labels(G,
                                 pos=nx.spring_layout(G, seed=good_seed),
                                 edge_labels=labels)
    # re-scale weights to avoid enormous edges
    lab_val = list(labels.values())
    scaled_lab_val = [element * 0.1 for element in lab_val]
    # draw egdes proportionately to weights
    if (directed):
        nx.draw_networkx_edges(G, pos=nx.spring_layout(G, seed=good_seed),
                               width=scaled_lab_val,
                               edge_color='#cc901699',
                               arrowstyle='->',
                               arrowsize=17)
    else:
        nx.draw_networkx_edges(G, pos=nx.spring_layout(G, seed=good_seed),
                               width=scaled_lab_val,
                               edge_color='#cc901699')

    plt.axis('off')
    plt.figtext(.5, .9, f'{word} graph of patient transfers',
                fontsize=17, ha='center')
    end = time.time()
    if (show):
        plt.show()
    print("Time to execute: {0:.5f} s.".format(end - start))
    return G


# Ga = sparse_graph(show=False)
# print(Ga["Bretagne"]["Grand Est"]["nombre_patients_transferes"])


# Now let's see it's adjacency matrix!

def sparse_matrix(show=True):
    """
    Return and plot the adjacency matrix of the graph of the transfer of
    patient with Covid-19, inside or outside France. This, by definition, is
    a sparse matrix.

    Parameters
    ----------

    :param show: whether or not to show the matrix
    :type show: bool, optional, default=True

    :return: the adjacency matrix of transfer graph and a plot of its
        representation
    :rtype: scipy.sparse.csr.csr_matrix

    :Examples:

    >>> sparse_matrix(show=True)

    >>> from scipy.sparse import isspmatrix
    >>> A = sparse_matrix(show=False)
    >>> print(isspmatrix(A))
    True

    """
    start = time.time()
    # take only the graph object
    G = sparse_graph(show=False)
    # get adjacency matrix
    A = nx.adjacency_matrix(G)
    # is it sparse ? ...of course it is..it's an adjacency matrix!
    if (isspmatrix(A)):
        verb = 'is'
    else:
        verb = "isn't"
    # graph properties
    e = G.number_of_edges()
    v = G.number_of_nodes()
    # percentage of matrix occupation
    percent_occ = (e / v**2) * 100
    rounded_percent_occ = round(percent_occ, 4)
    # plot sparse adjacency matrix
    plt.figure(figsize=(11, 11))
    plt.spy(A, color='#971b8599')
    plt.figtext(.5, 0.96, 'Here is the adjacency matrix of the transfer graph',
                fontsize=17, ha='center')
    plt.figtext(.5, 0.94, f'This {verb} a sparse matrix',
                fontsize=14, ha='center')
    plt.figtext(.5, 0.92, f'percentage of occupation: {rounded_percent_occ}',
                fontsize=11, ha='center')
    end = time.time()
    if (show):
        plt.show()
    print("Time to execute: {0:.5f} s.".format(end - start))
    return A


# print(isspmatrix(sparse_matrix(show=False)))
