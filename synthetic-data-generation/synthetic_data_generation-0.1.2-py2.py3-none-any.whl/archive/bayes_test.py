from thomas.core.cpt import CPT
from thomas.core.factor import Factor
from thomas.core.bayesiannetwork import BayesianNetwork
from sklearn.metrics import mutual_info_score


def _compute_mutual_information_sklearn(self, X, pair):
    df_node = X[pair.node].values
    if len(pair.parents) == 1:
        df_parent = X[pair.parents[0]].values
    else:
        # todo find alternative method to combine parent cols
        df_parent = X.loc[:, pair.parents].apply(lambda x: ' '.join(x.values), axis=1).values
    return mutual_info_score(df_node, df_parent)

def _compute_mutual_information_thomas(self, X, pair):
    p_node = Factor(X.groupby(pair.node).size()).normalize()
    p_parents = Factor(X.groupby(list(pair.parents)).size()).normalize()
    p_nodeparents = Factor(X.groupby([*pair.parents, pair.node]).size()).normalize()

    # todo: have to get values from Factor: 'numpy.ndarray' object has no attribute '_data'
    mi = np.sum(p_nodeparents.values * np.log(p_nodeparents/(p_node*p_parents)))
    mi_old = self._compute_mutual_information_old(X, pair)
    if mi != mi_old:
        print('New mi: {} - old mi: {}'.format(mi, mi_old))
    return mi