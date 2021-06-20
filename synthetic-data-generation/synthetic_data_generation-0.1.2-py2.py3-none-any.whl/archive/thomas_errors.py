"""
Errors after update thomas to 0.1.1a18
Prior version: thomas-core==0.1.0a16

Perhaps due to my misinterpretation of some of the functionalities that thomas offers.
"""
import numpy as np
import pandas as pd

from sklearn.metrics import mutual_info_score
from thomas.core.cpt import CPT
from thomas.core.factor import Factor
from collections import namedtuple
from thomas.core.bayesiannetwork import BayesianNetwork

data_path = 'C:/projects/synthetic_data_generation/examples/data/original/adult.csv'
df = pd.read_csv(data_path, delimiter=', ', engine='python')
columns = ['age', 'sex', 'education', 'workclass', 'income']
df = df.loc[:, columns]

"""
Factor class
"""

# default states used to be None.
# Factor(df[column.value_counts()) no longer works
column = 'age'
Factor(df[column].value_counts()) # TypeError: __init__() missing 1 required positional argument: 'states'
# now use the following workaround:
column = 'age'
states = {column: df[column].unique()}
Factor(df[column].value_counts(), states)

# from_series() does not work with strings:
Factor.from_series(df['sex']) # ValueError: could not convert string to float: 'Male'

# from_series() does not work with integers:
Factor.from_series(df['age']) # TypeError: sequence item 0: expected str instance, NoneType found

# from_series() does not work with value_counts:
Factor.from_series(df['age'].value_counts()) # TypeError: sequence item 0: expected str instance, NoneType found

# from_data() does not work with one column - different errors depending on string or integer
Factor.from_data(df, cols=['sex']) # ValueError: 'data' must be of size/length: 2
Factor.from_data(df, cols=['age']) # TypeError: 'int' object is not iterable

# my pull request from december might fix some of these issues in from_data() with one column, but is also probably not
# the best solution. Not sure if you even intended to support Factors of one column.

"""
CPT 
subclasses Factor so will inherit the same problems as above
"""

# CPT default states is None, as it calls super.init() this does no longer work
CPT(df['age']) # AssertionError: 'states should be a dict, but got <class 'NoneType'> instead? type(data): <class 'pandas.core.series.Series'>

# CPT from_data() not implemented, inherits from Factor, thus does not return a CPT
CPT.from_data(df, cols=['age', 'sex']) # works but returns a Factor not CPT

# method I used in previous version of thomas - no longer works due to missing states
CPT(df.groupby(['age', 'sex']).size(), conditioned=['sex'])

# workaround to obtain a CPT -> not ideal as you cannot specify hyperparameters like conditioned or input an
# already computed joint distribution.
CPT.from_factor(Factor.from_data(df, cols=['age', 'sex']))

# from_data() and from_series() same as Factor does not work with one column - different errors depending on column type
CPT.from_data(df, cols=['sex']) # ValueError: 'data' must be of size/length: 2

# note: I need a CPT of only 1 column when initiating the BayesianNetwork.from_CPTS()
# workaround solution
column = 'sex'
states = {column: df[column].unique()}
CPT.from_factor(Factor(df[column].value_counts(), states))


# CPT no longer has normalize method -> thus inherits from Factor
# I use this now as a workaround (based on your old solution)
def _normalize_cpt(cpt):
    """normalization of cpt with option to fill missing values with uniform distribution"""
    # convert to series as normalize does not work with thomas cpts
    series = cpt.as_series()
    series_norm_full = series / series.unstack().sum(axis=1)
    # fill missing combinations with uniform distribution
    uniform_prob = 1 / len(cpt.states[cpt.conditioned[-1]])
    series_norm_full = series_norm_full.fillna(uniform_prob)
    return CPT(series_norm_full, cpt.states)

"""DEPRECATED:
mutual information method that worked with older version of thomas -> now resort to clunky sklearn variant see below.
"""
NodeParentPair = namedtuple('NodeParentPair', ['node', 'parents'])

def compute_mutual_information(X, pair):
    """DEPRECATED"""
    p_node = Factor(X.groupby(pair.node).size()).normalize()
    p_parents = Factor(X.groupby(list(pair.parents)).size()).normalize()
    p_nodeparents = Factor(X.groupby([*pair.parents, pair.node]).size()).normalize()

    # have to get values from Factor: 'numpy.ndarray' object has no attribute '_data'
    mi = np.sum(p_nodeparents.values * np.log(p_nodeparents / (p_node * p_parents)))
    return mi


def compute_mutual_information_sklearn(X, pair):
    df_node = X[pair.node].values
    if len(pair.parents) == 1:
        df_parent = X[pair.parents[0]].values
    else:
        df_parent = X.loc[:, pair.parents].apply(lambda x: ' '.join(x.values), axis=1).values
    return mutual_info_score(df_node, df_parent)

pair = NodeParentPair(node='age', parents=['sex'])
compute_mutual_information(df, pair) # TypeError: __init__() missing 1 required positional argument: 'state
compute_mutual_information_sklearn(df, pair)

NodeParentPair(node='income', parents=('education',)) # work work as np.log has 0 values

# JPT - Factor not possible