"""
Synthetic data generation via Bayesian Networks

Based on following paper

Zhang J, Cormode G, Procopiuc CM, Srivastava D, Xiao X.
PrivBayes: Private Data Release via Bayesian Networks. (2017)
"""

import numpy as np
import pandas as pd
from sklearn.metrics import mutual_info_score
from itertools import combinations
from collections import namedtuple

from synthesis.synthesizers._base import BaseDPSynthesizer
import synthesis.synthesizers.utils as utils
from thomas.core.cpt import CPT
from thomas.core.factor import Factor
from thomas.core.bayesiannetwork import BayesianNetwork

NodeParentPair = namedtuple('NodeParentPair', ['node', 'parents'])


class PrivBayes(BaseDPSynthesizer):
    """PrivBayes: Private Data Release via Bayesian Networks (Zhang et al 2017)

    Version:
    - vanilla encoding
    - mutual information as score function

    Extended:
    - Ability to initialize network

    Default hyperparameters set according to paper recommendations

    """

    def __init__(self, epsilon=1.0, theta_usefulness=4,
                 epsilon_split=0.3, network_init=None,
                 max_cpt_size=10000000, verbose=True):
        super().__init__(epsilon=epsilon, verbose=verbose)
        self.theta_usefulness = theta_usefulness
        self.epsilon_split = epsilon_split  # also called Beta in paper
        self.network_init = network_init
        self.max_cpt_size = max_cpt_size  # in general large cpts are not advised unless epsilon is infinite

    def fit(self, data):
        self._check_init_args()
        data = self._check_input_data(data)

        self._greedy_bayes(data)
        self._compute_conditional_distributions(data)
        self.model_ = BayesianNetwork.from_CPTs('PrivBayes', self.cpt_.values())
        return self

    def sample(self, n_records=None):
        # n_records = self._n_records_fit if n_records is None else n_records
        self._check_is_fitted()
        n_records = n_records or self.n_records_fit_

        synth_data = self._generate_data(n_records)
        if self.verbose:
            print("\nSynthetic Data Generated\n")
        return synth_data

    def _greedy_bayes(self, data):
        nodes, nodes_selected = self._init_network(data)

        # normally len(nodes) - 1, unless user initialized part of the network
        self._n_nodes_dp_computed = len(nodes) - len(nodes_selected)

        for i in range(len(nodes_selected), len(nodes)):
            if self.verbose:
                print("{}/{} - Evaluating next node to add to network".format(i + 1, len(self.columns_)))

            nodes_remaining = nodes - nodes_selected

            # select NodeParentPair candidates
            for node in nodes_remaining:
                node_cardinality = self._attribute_cardinality(data, node)
                max_domain_size = self.n_records_fit_ * (1 - self.epsilon_split) / \
                                  (2 * len(self.columns_) * self.theta_usefulness * node_cardinality)

                max_parent_sets = self._max_parent_sets(data, nodes_selected, max_domain_size)

                # empty set - no parents found that meet domain size restrictions
                if len(max_parent_sets) == 1 and len(max_parent_sets[0]) == 0:
                    node_parent_pairs = NodeParentPair(node, parents=None)
                else:
                    node_parent_pairs = [
                        NodeParentPair(node, tuple(p)) for p in max_parent_sets
                    ]

            if self.verbose:
                print("Number of NodeParentPair candidates: {}".format(len(node_parent_pairs)))

            scores = self._compute_scores(data, node_parent_pairs)
            sampled_pair = self._exponential_mechanism(data, node_parent_pairs, scores)

            if self.verbose >= 1:
                print("Selected node: {} - with parents: {}\n".format(sampled_pair.node, sampled_pair.parents))
            nodes_selected.add(sampled_pair.node)
            self.network_.append(sampled_pair)
        if self.verbose:
            print("Learned Network Structure\n")
        return self

    def _max_parent_sets(self, data, v, max_domain_size):
        """refer to algorithm 5 in paper
        max parent set is 1) theta-useful and 2) maximal."""
        if max_domain_size < 1:
            return set()
        if len(v) == 0:
            return [set()]

        x = np.random.choice(tuple(v))
        x_domain_size = self._attribute_cardinality(data, x)
        x = {x}

        v_without_x = v - x

        parent_sets1 = self._max_parent_sets(data, v_without_x, max_domain_size)
        parent_sets2 = self._max_parent_sets(data, v_without_x, max_domain_size / x_domain_size)

        for z in parent_sets2:
            if z in parent_sets1:
                parent_sets1.remove(z)
            parent_sets1.append(z.union(x))

        return parent_sets1

    def _init_network(self, X):
        self._binary_columns = [c for c in X.columns if X[c].unique().size <= 2]
        nodes = set(X.columns)

        if self.network_init is not None:
            nodes_selected = set(n.node for n in self.network_init)
            # print("Pre-defined network init: {}".format(self.network_))
            for i, pair in enumerate(self.network_init):
                if self.verbose:
                    print("{}/{} - init node {} - with parents: {}".format(i + 1, len(self.network_init),
                                                                           pair.node, pair.parents))
            self.network_ = self.network_init.copy()
            return nodes, nodes_selected

        # if set_network is not called we start with a random first node
        self.network_ = []
        nodes_selected = set()

        root = np.random.choice(tuple(nodes))
        self.network_.append(NodeParentPair(node=root, parents=None))
        nodes_selected.add(root)
        if self.verbose:
            print("1/{} - Root of network: {}\n".format(X.shape[1], root))
        return nodes, nodes_selected

    def set_network(self, network):
        assert [isinstance(n, NodeParentPair) for n in network], "input network does not consists of " \
                                                                 "NodeParentPairs"
        self.network_init = network
        return self

    def _compute_scores(self, X, node_parent_pairs):
        cached_scores = self._get_cached_scores(node_parent_pairs)
        # todo fix cache_scores
        scores = np.empty(len(node_parent_pairs))
        for idx, pair in enumerate(node_parent_pairs):
            scores[idx] = self._compute_mutual_information(X, pair)
        return scores

    def _get_cached_scores(self, node_parent_pairs):
        return []

    def _compute_mutual_information(self, X, pair):
        try:
            pair.node
        except:
            print(pair)

        p_node = Factor(X.groupby(pair.node).size()).normalize()
        p_parents = Factor(X.groupby(list(pair.parents)).size()).normalize()
        p_nodeparents = Factor(X.groupby([*pair.parents, pair.node]).size()).normalize()

        # todo: have to get values from Factor: 'numpy.ndarray' object has no attribute '_data'
        mi = np.sum(p_nodeparents.values * np.log(p_nodeparents / (p_node * p_parents)))
        return mi

    def _compute_mutual_information_sklearn(self, X, pair):
        df_node = X[pair.node].values
        if len(pair.parents) == 1:
            df_parent = X[pair.parents[0]].values
        else:
            # todo find alternative method to combine parent cols
            df_parent = X.loc[:, pair.parents].apply(lambda x: ' '.join(x.values), axis=1).values
        return mutual_info_score(df_node, df_parent)

    def _exponential_mechanism(self, X, node_parent_pairs, scores):
        # todo check if dp correct -> e.g. 2*scaling?
        scaling_factors = self._compute_scaling_factor(X, node_parent_pairs)
        sampling_distribution = np.exp(scores / 2 * scaling_factors)
        normalized_sampling_distribution = sampling_distribution / sampling_distribution.sum()
        pair_idx = np.arange(len(node_parent_pairs))
        sampled_pair_idx = np.random.choice(pair_idx, p=normalized_sampling_distribution)
        sampled_pair = node_parent_pairs[sampled_pair_idx]
        return sampled_pair

    def _compute_scaling_factor(self, X, node_parent_pairs):
        n_records = self.n_records_fit_
        scaling_factors = np.empty(len(node_parent_pairs))

        for idx, pair in enumerate(node_parent_pairs):
            if pair.node in self._binary_columns or \
                    (len(pair.parents) == 1 and pair.parents[0] in self._binary_columns):
                sensitivity = (np.log(n_records) / n_records) + \
                              (((n_records - 1) / n_records) * np.log(n_records / (n_records - 1)))
            else:
                sensitivity = (2 / n_records) * np.log((n_records + 1) / 2) + \
                              (((n_records - 1) / n_records) * np.log((n_records + 1) / (n_records - 1)))

            scaling_factors[idx] = self._n_nodes_dp_computed * sensitivity / (self.epsilon * self.epsilon_split)
        return scaling_factors

    def _compute_conditional_distributions(self, data):
        self.cpt_ = dict()

        local_epsilon = self.epsilon * (1 - self.epsilon_split) / len(self.columns_)

        for idx, pair in enumerate(self.network_):
            if pair.parents is None:
                dp_distribution = utils.dp_marginal_distribution(data[pair.node])
                cpt = Factor(dp_distribution)
            else:
                attributes = [*pair.parents, pair.node]
                cpt_size = utils.cardinality(data[attributes])
                if self.verbose:
                    print('Learning conditional probabilities: {} - with parents {} '
                          '~ estimated size: {}'.format(pair.node, pair.parents, cpt_size))

                dp_distribution = utils.dp_joint_distribution(data[attributes], epsilon=local_epsilon)
                cpt = CPT(dp_distribution, conditioned_variables=[pair.node])
                cpt = utils._normalize_cpt(cpt, dropna=False)
            self.cpt_[pair.node] = cpt

        return self

    def _generate_data(self, n_records):
        Xt = np.empty([n_records, len(self.columns_)], dtype=object)

        for i in range(n_records):
            if self.verbose >= 1:
                print('Number of records generated: {} / {}'.format(i + 1, n_records), end='\r')
            record = self._sample_record()
            Xt[i] = list(record.values())

        # np to df with original column ordering
        Xs = pd.DataFrame(Xt, columns=[c.node for c in self.network_])[self.columns_]
        return Xs

    def _sample_record(self):
        record = {}
        for col_idx, pair in enumerate(self.network_):
            node = self.model_[pair.node]
            # todo filter cpt based on sampled parents

            # specify pre-sampled conditioning values
            node_cpt = node.cpt
            for parent in node.conditioning:
                parent_value = record[parent]
                node_cpt = node_cpt[parent_value]

            sampled_node_value = np.random.choice(node.states, p=node_cpt.values)

            record[node.name] = sampled_node_value

        return record

    @staticmethod
    def _attribute_cardinality(data, attribute):
        return data[attribute].nunique(dropna=False)


# class PrivBayesBinary(PrivBayes):
#     """PrivBayes on binary encoded data - use F score function and a fixed degree k
#
#     STILL IN DEVELOPMENT!
#     """
#
#     def fit(self, data):
#         self._check_init_args()
#         X = self._check_input_data(data)
#
#         self._check_degree_network(data)
#         self._greedy_bayes(X)
#         self._compute_conditional_distributions(X)
#         self.model_ = BayesianNetwork.from_CPTs('PrivBayes', self.cpt_.values())
#         return self
#
#     def _greedy_bayes(self, X):
#
#         nodes, nodes_selected = self._init_network(X)
#         # normally equal to n_columns - 1 as only the root is selected, unless user
#         # initializes part of the network.
#         self._n_nodes_dp_computed = len(nodes) - len(nodes_selected)
#
#         for i in range(len(nodes_selected), len(nodes)):
#             if self.verbose:
#                 print("{}/{} - Evaluating next node to add to network".format(i + 1, len(self.columns_)))
#
#             nodes_remaining = nodes - nodes_selected
#             n_parents = min(self.degree_network, len(nodes_selected))
#
#             node_parent_pairs = [
#                 NodeParentPair(n, tuple(p)) for n in nodes_remaining
#                 for p in combinations(nodes_selected, n_parents)
#             ]
#             if self.verbose:
#                 print("Number of NodeParentPair candidates: {}".format(len(node_parent_pairs)))
#
#             scores = self._compute_scores(X, node_parent_pairs)
#
#             if self.epsilon:
#                 sampled_pair = self._exponential_mechanism(X, node_parent_pairs, scores)
#             else:
#                 sampled_pair = node_parent_pairs.index(max(scores))
#             if self.verbose >= 1:
#                 print("Selected node: {} - with parents: {}\n".format(sampled_pair.node, sampled_pair.parents))
#             nodes_selected.add(sampled_pair.node)
#             self.network_.append(sampled_pair)
#         if self.verbose >= 1:
#             print("Learned Network Structure\n")
#         return self
#
#     def _check_degree_network(self, X):
#         if not self.degree_network:
#             self.degree_network = self._compute_degree_network(self.n_records_fit_, len(self.columns_))
#
#         # check if degree network will not result in conditional tables that do not fit into memory
#         if self.max_cpt_size:
#             max_degree_network = self._max_degree_network(X)
#             if self.degree_network > max_degree_network:
#                 if self.verbose >= 1:
#                     print("Degree network capped from {} to {} to be able to fit CPT into memory"
#                           .format(self.degree_network, max_degree_network))
#                     self.degree_network = max_degree_network
#
#         if self.verbose >= 1:
#             print("Degree of network (k): {}\n".format(self.degree_network))
#
#     def _compute_degree_network(self, n_records, n_columns):
#         """
#         Determine the degree of the network (k) by finding the lowest integer k possible that ensures that the defined
#         level of theta-usefulness is met. This criterion measures the ratio of information over noise.
#         Lemma 4.8 in the paper.
#
#         Note there are some inconsistencies between the original paper from 2014 and the updated version in 2017
#         - avg_scale_info: full epsilon in paper 2014 | epsilon_2 in paper2017
#         - avg_scale_noise: k + 3 in paper 2014 lemma 3 | k + 2 in paper 2017 lemma  4.8
#         """
#         k = n_columns - 1
#
#         while k > 1:
#             # avg_scale_info = self.epsilon * (1 - self.epsilon_split[0]) * n_records
#             avg_scale_info = self.epsilon * self.epsilon_split[1] * n_records
#             avg_scale_noise = (n_columns - k) * (2 ** (k + 2))
#             if (avg_scale_info / avg_scale_noise) >= self.theta_usefulness:
#                 break
#             k -= 1
#         return k
#
#     def _max_degree_network(self, X):
#         """calculate max degree network to ensure the CPTs will fit into memory"""
#         ranked_column_cardinalities = utils.rank_columns_on_cardinality(X)
#         cum_cardinality = 1
#         degree_network = 0
#         for k, cardinality in enumerate(ranked_column_cardinalities):
#             cum_cardinality *= cardinality
#             if cum_cardinality >= self.max_cpt_size:
#                 break
#             degree_network += 1
#         return degree_network
#
#     def _compute_conditional_distributions(self, X):
#         P = dict()
#         # note we only compute n_columns - (degree_network+1), as the CPTs from the other nodes
#         # in range [0, degree_network] can be inferred -> ensures (eps_2 / (d-k))-differential privacy
#         local_epsilon = self.epsilon * self.epsilon_split[1] / (len(self.columns_)- self.degree_network)
#
#         # first materialize noisy joint distributions for nodes who have a equal number of parents to the degree k.
#         # earlier nodes can be inferred from these distributions without adding extra noise
#         for idx, pair in enumerate(self.network_[self.degree_network:]):
#             cpt_size = utils.get_size_contingency_table(X[[*pair.parents, pair.node]])
#             if self.verbose >= 2:
#                 print('Learning conditional probabilities: {} - with parents {} ~ estimated size: {}'.format(pair.node,
#                                                                                                          pair.parents,
#                                                                                                          cpt_size))
#             attributes = [*pair.parents, pair.node]
#             dp_joint_distribution = utils.dp_joint_distribution(X[attributes], epsilon=local_epsilon)
#             # dp_joint_distribution = utils.joint_distribution(X[attributes])
#             cpt = CPT(dp_joint_distribution, conditioned_variables=[pair.node])
#             # todo: use custom normalization to fill missing values with uniform
#             cpt = utils._normalize_cpt(cpt, dropna=False)
#             P[pair.node] = cpt
#             # retain noisy joint distribution from k+1 node to infer distribution parent nodes
#             if idx == 0:
#                 infer_from_distribution = Factor(dp_joint_distribution)
#                 infer_from_distribution = infer_from_distribution.sum_out(pair.node)
#
#         # for pair in self.network_[:self.k]:
#
#         # go iteratively from node at k to root of network, sum out child nodes and get cpt.
#         for pair in reversed(self.network_[:self.degree_network]):
#             if pair.parents is not None:
#                 attributes = [*pair.parents, pair.node]
#             else:
#                 attributes = [pair.node]
#             cpt_size = utils.get_size_contingency_table(X[attributes])
#             if self.verbose >= 2:
#                 print('Learning conditional probabilities: {} - with parents {} ~ estimated size: {}'.format(pair.node,
#                                                                                                          pair.parents,
#                                                                                                          cpt_size))
#             # infer_from_distribution = infer_from_distribution.sum_out(pair.node)
#             # conditioned_var = pair.parents[-1]
#             cpt = CPT(infer_from_distribution, conditioned_variables=[pair.node])
#             cpt = utils._normalize_cpt(cpt, dropna=False)
#
#             P[pair.node] = cpt
#             infer_from_distribution = infer_from_distribution.sum_out(pair.node)
#
#         self.cpt_ = P
#         return self

# class PrivBayesFix(PrivBayes):
#
#     def __init__(self, epsilon: float = 1.0, degree_network=None,
#                  theta_usefulness=4, score_function='mi', random_state=None,
#                  epsilon_split=0.4, n_records_synth=None, network_init=None,
#                  fix_columns=None):
#         super().__init__(epsilon=epsilon, degree_network=degree_network,
#                          theta_usefulness=theta_usefulness, score_function=score_function,
#                          random_state=random_state,
#                          epsilon_split=epsilon_split, n_records_synth=n_records_synth,
#                          network_init=network_init)
#         self._fix_columns = fix_columns
#
#     # def _init_network(self, X):
#     #     # todo implement user-specified init network
#     #
#     #     nodes = set(X.columns)
#     #     network = []
#     #     nodes_selected = set()
#     #
#     #     root = np.random.choice(tuple(nodes))
#     #     network.append(NodeParentPair(node=root, parents=None))
#     #     nodes_selected.add(root)
#     #     print("Root of network: {}".format(root))
#
#     def fit(self, X, y=None):
#         # assert hasattr(self, 'fix_columns'), "first call set_network and fix_columns to fix columns " \
#         #                                       "prior to generating data"
#         assert self.network_init is not None, "first define network_init prior to fitting data"
#         return super().fit(X, y)
#
#     def transform(self, X):
#         n_records = len(self._fix_columns)
#
#         Xt = self._generate_data(X, n_records)
#         return Xt
#
#     def _generate_data(self, X, n_records):
#         Xt = np.empty([n_records, len(self.network_)], dtype=object)
#
#         for i in range(n_records):
#             if self.verbose >= 1:
#                 print('Number of records generated: {} / {}'.format(i+1, n_records), end='\r')
#             record_init = self._fix_columns.loc[i].to_dict()
#             record = self._sample_record(record_init)
#             Xt[i] = list(record.values())
#
#         # np to df with original column ordering
#         df_synth = pd.DataFrame(Xt, columns=[c.node for c in self.network_])[self.columns_]
#         return df_synth
#
#     def set_fixed_columns(self, fix_columns):
#         # assert hasattr(self, 'network_'), "use set_network with X_fix columns before defining" \
#         #                                   "fixing columns"
#         # assert self.network_init is not None, "use set_network with X_fix columns before " \
#         #                                       "defining fixed columns"
#         network_init_nodes = [n.node for n in self.network_init]
#         if not isinstance(fix_columns, pd.DataFrame):
#             fix_columns = pd.DataFrame(fix_columns)
#
#         assert set(fix_columns.columns) == set(network_init_nodes), "features in X_fix not set in network_init"
#         self._fix_columns = fix_columns.reset_index(drop=True)
#         return self
#
#     def _sample_record(self, record_init):
#         # assume X has columns with values that correspond to the first nodes in the network
#         # that we would like to fix and condition for.
#         record = record_init
#
#         # sample remaining nodes after fixing for input X
#         for col_idx, pair in enumerate(self.network_[len(record_init):]):
#             node = self.bayesian_network_[pair.node]
#             # todo filter cpt based on sampled parents
#
#             # specify pre-sampled conditioning values
#             node_cpt = node.cpt
#             for parent in node.conditioning:
#                 parent_value = record[parent]
#                 node_cpt = node_cpt[parent_value]
#                 # try:
#                 #     node_cpt = node_cpt[parent_value]
#                 # except:
#                 #     print(record)
#                 #     print(node)
#                 #     print(node_cpt)
#                 #     print("parent: {} - {}".format(parent, parent_value))
#                 #     print('----')
#                 #     raise ValueError
#             # print(node.states)
#             # print(node_cpt.values)
#             sampled_node_value = np.random.choice(node.states, p=node_cpt.values)
#
#             record[node.name] = sampled_node_value
#
#         return record


if __name__ == "__main__":
    data_path = 'C:/projects/synthetic_data_generation/examples/data/original/adult.csv'
    df = pd.read_csv(data_path, delimiter=', ', engine='python')
    columns = ['age', 'sex', 'education', 'workclass', 'income']
    df = df.loc[:, columns]
    print(df.head())

    pb = PrivBayes()
    pb.fit(df)
    df_synth = pb.sample()

    init_network = [NodeParentPair(node='age', parents=None),
                    NodeParentPair(node='education', parents='age'),
                    NodeParentPair(node='sex', parents=('age', 'education'))]

    pbinit = PrivBayes
    pbinit.set_network(init_network)
    pbinit.fit(df)
    df_synth_init = pbinit.sample(1000)

    # pb._check_init_args()
    # nodes, nodes_selected = pb._init_network(df)
    #
    # max_parents = pb._max_parent_sets(df, nodes_selected, 100)
    # print('Max parents: {}'.format(max_parents))
    # epsilon = float(np.inf)
    # epsilon = 1
    # pb = PrivBayes(epsilon=epsilon, degree_network=2)
    # pb.fit(df)
    # print(pb.network_)
    # print("Succesfull")
    #
    #
    # df_synth = pb.sample()
    # df_synth.head()

    # # fixing a network - specify init network to fix those variables when generating
    # pbfix = PrivBayesFix(epsilon, degree_network=2)
    # # init_network = [NodeParentPair('age', None), NodeParentPair('education', 'age')]
    # init_network = [NodeParentPair(node='age', parents=None),
    #                 NodeParentPair(node='education', parents='age'),
    #                  NodeParentPair(node='sex', parents=('age', 'education')),
    #                  NodeParentPair(node='workclass', parents=('age', 'education')),
    #                  NodeParentPair(node='income', parents=('sex', 'age'))]
    # pbfix.set_network(init_network)
    # pbfix.fit(df)
    # pbfix_copy = deepcopy(pbfix)
    #
    #
    # # x2 = df.copy() # todo should really be synth
    # df_synth_tuned = pbfix.transform(df_synth[['age', 'education']])
