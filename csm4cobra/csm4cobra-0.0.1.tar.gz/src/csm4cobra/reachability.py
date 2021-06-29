import re
import warnings
import pandas as pd
from pyfastcore import Fastcore
from cobra.flux_analysis.deletion import find_gene_knockout_reactions

import multiprocessing


def to_square_form_2(df_reachability):
    all_precursors = sorted((df_reachability.precursor_id.unique()))
    gene_pair_list = []

    reachability_dict = {}
    for i in df_reachability.index:
        gene_i = df_reachability.gene_i_id[i]
        gene_j = df_reachability.gene_j_id[i]
        gene_pair = gene_i, gene_j
        gene_pair_list.append(gene_pair)

        mask = (df_reachability.gene_i_id == gene_i) & (df_reachability.gene_j_id == gene_j)
        precursors = df_reachability.precursor_id[mask]
        reachability_dict[gene_pair] = sorted(precursors)

    columns = ["gene_i_id", "gene_j_id"] + all_precursors
    index = list(range(len(gene_pair_list)))
    df_square = pd.DataFrame(index=index, columns=columns)

    for i in index:
        gene_pair = gene_pair_list[i]
        precursors = reachability_dict[gene_pair]
        #     df_square.at[i, precursors] = 1
        df_square.at[i, "gene_i_id"] = gene_pair[0]
        df_square.at[i, "gene_j_id"] = gene_pair[1]
        for j in all_precursors:
            if j in precursors:
                df_square.at[i, j] = 1
            else:
                df_square.at[i, j] = 0


def to_square_form(df_reachability, element_col='gene_id', precursors_col='compound_name'):
    genes = df_reachability[element_col].unique()
    precursors = df_reachability[precursors_col].unique()

    df_square_form = pd.DataFrame(data=0., index=genes, columns=precursors)
    df_square_form.index.name = element_col

    for p in precursors:
        mask = df_reachability[precursors_col] == p

        gene_list = df_reachability.loc[mask, element_col].unique()
        df_square_form.at[gene_list, p] = 1

    return df_square_form


def _init_worker(tester):
    """Initialize a global reachability tester object for multiprocessing."""
    global _tester
    _tester = tester


class ReachabilityTester:

    def __init__(self, cobra_model, target_products,
                 epsilon=1e-4, tolerance=1e-7, report=True,
                 flux_bound=999999.):

        self._model = cobra_model.copy()
        self._var_mapping = {}
        self._epsilon = epsilon
        self._tolerance = tolerance
        self._demands_dict = {}
        self._product_to_demands_dict = {}
        self._original_bound = {}
        self._not_reachable_products = []

        assert len(target_products) > 0

        if report:
            print("===========================================================")
            print("Initializing Reachability Tester using")
            print("Model: %s" % cobra_model.id)

            print("- Nº of reactions: %i" % len(self._model.reactions))
            print("- Nº of metabolites: %i" % len(self._model.metabolites))
            print("- Nº of target products: %i" % len(target_products))

        if hasattr(target_products[0], 'id'):
            target_products = [m.id for m in target_products]

        for r in self._model.reactions:
            self._original_bound[r.id] = r.bounds
            if r.upper_bound > 0:
                r.upper_bound = flux_bound
            if r.lower_bound < 0:
                r.lower_bound = -flux_bound

        for m in target_products:
            m = self._model.metabolites.get_by_id(m)
            try:
                demand = self._model.add_boundary(m, type='demand')
            except (KeyError, ValueError) as e:
                demand_id = re.sub(r"^[^']*'([^']*)'.*", r"\1", e.args[0])
                demand = self._model.reactions.get_by_id(demand_id)

            self._demands_dict[demand.id] = m
            self._product_to_demands_dict[m.id] = demand.id

        self._init_lp_problems()
        not_reachable_targets = self.test_target_products()
        if len(not_reachable_targets) > 0:
            print("Warning the following target products cannot be reached")
            print(" ".join(not_reachable_targets))
            print("Removing compounds form the list of target products")
            for i in not_reachable_targets:
                demand = self._product_to_demands_dict[i]
                del self._demands_dict[demand]

            print("Updating LP models")
            self._init_lp_problems()

    @property
    def model(self):
        return self._model

    @property
    def epsilon(self):
        return self._epsilon

    @property
    def tolerance(self):
        return self._tolerance

    def _init_lp_problems(self):

        self._var_mapping = {}
        self._lp7 = None
        self._fva = None

        demands = list(self._demands_dict.keys())
        self._lp7 = Fastcore.create_optlang_lp7(self._model, demands, epsilon=self.epsilon)
        self._fva = Fastcore.create_optlang_fba(self._model)

        for rxn, met in self._demands_dict.items():
            z_var_id = Fastcore.AUXILIARY_VAR_PREFIX + rxn
            z_var = self._lp7.variables.get(z_var_id)
            self._var_mapping[z_var] = met

    def _run_lp7_reachability(self, reactions_to_block):
        not_produced = []
        variables_to_block = {}

        if len(reactions_to_block) > 0:
            if hasattr(reactions_to_block[0], 'id'):
                reactions_to_block = [r.id for r in reactions_to_block]

            for r in reactions_to_block:
                var = self._lp7.variables.get(r)
                variables_to_block[var] = (var.lb, var.ub)
                var.lb = 0
                var.ub = 0

        self._lp7.optimize()
        eps = 0.99 * self.epsilon
        for z_var, met in self._var_mapping.items():
            if z_var.primal - eps > self.tolerance:
                continue
            not_produced.append(met.id)

        for r in reactions_to_block:
            var = self._lp7.variables.get(r)
            (var.lb, var.ub) = variables_to_block[var]

        return not_produced

    def _run_fva_reachability(self, reactions_to_block):
        lp_model = self._fva
        not_produced = []
        if len(reactions_to_block) > 0:
            if hasattr(reactions_to_block[0], 'id'):
                reactions_to_block = [r.id for r in reactions_to_block]

        bounds_dict = {}
        for r in reactions_to_block:
            var = lp_model.variables.get(r)
            bounds_dict[var] = var.lb, var.ub
            var.lb = 0
            var.ub = 0

        objective_coefficients = {v: 0 for v in lp_model.variables}
        for r, m in self._demands_dict.items():
            var = lp_model.variables.get(r)
            objective_coefficients[var] = 1
            lp_model.objective.set_linear_coefficients(objective_coefficients)
            lp_model.update()
            lp_model.optimize()
            objective_coefficients[var] = 0

            if lp_model.status == 'infeasible':
                warnings.warn("Infeasible solution for %s" % m)

            if var.primal < self._tolerance:
                not_produced.append(m.id)

        for r in reactions_to_block:
            var = lp_model.variables.get(r)
            var.lb = bounds_dict[var][0]
            var.ub = bounds_dict[var][1]

        return not_produced

    def run_reactions_reachability(self, reactions_to_block, method='lp7'):

        if method == 'lp7':
            return self._run_lp7_reachability(reactions_to_block)
        elif method == 'fva':
            return self._run_fva_reachability(reactions_to_block)
        else:
            raise NotImplementedError

    def single_gene_reachability(self, gene_list=[], method='lp7', rxn_str_sep='|', debug=False):

        if len(gene_list) == 0:
            gene_list = [g.id for g in self._model.genes]

        if hasattr(gene_list[0], 'id'):
            gene_list = [g.id for g in gene_list]

        data = []
        for g in gene_list:

            if debug:
                print("Testing gene:", g)

            g = self._model.genes.get_by_id(g)

            reactions_to_block = find_gene_knockout_reactions(self._model, [g])
            if len(reactions_to_block) == 0:
                continue

            not_produced = self.run_reactions_reachability(reactions_to_block, method=method)
            if len(not_produced) == 0:
                continue

            reactions_strn = rxn_str_sep.join([r.id for r in reactions_to_block])
            for m in not_produced:
                m = self._model.metabolites.get_by_id(m)
                data.append([g.id, m.id, m.name, reactions_strn])

        columns = ['gene_id', 'compound_id', 'compound_name', 'reactions']
        df_reachability = pd.DataFrame(columns=columns, data=data)
        df_reachability.index.name = 'idx'

        return df_reachability

    def single_reaction_reachability(self, reaction_list=[], method='lp7', find_ums=False):

        if len(reaction_list) == 0:
            reaction_list = [r.id for r in self._model.reactions]

        if hasattr(reaction_list[0], 'id'):
            reaction_list = [r.id for r in reaction_list]

        data = []
        for r in reaction_list:

            not_produced = self.run_reactions_reachability([r], method=method)
            if len(not_produced) == 0:
                continue

            r = self._model.reactions.get_by_id(r)
            for m in not_produced:
                m = self._model.metabolites.get_by_id(m)
                data.append([r.id, m.id, m.name, r.gene_reaction_rule])

        columns = ['reaction_id', 'compound_id', 'compound_name', 'gpr']
        df_reachability = pd.DataFrame(columns=columns, data=data)
        df_reachability.index.name = 'idx'

        return df_reachability

    # def single_reachability(self, element_list, method='lp7', tpye="gene", find_ums=False):
    #     if args.deletion_type == 'gene':
    #         df_reachability = reachability_tester.single_gene_reachability(method=args.method, find_ums=find_ums)
    #
    #     elif args.deletion_type == 'reaction':
    #         df_reachability = reachability_tester.single_reaction_reachability(method=args.method, find_ums=find_ums)

    def test_target_products(self):
        self._not_reachable_products = self._run_lp7_reachability([])
        return self._not_reachable_products
