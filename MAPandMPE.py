from typing import Union

import pandas as pd

from BNReasoner import BNReasoner, multiply_factors
from BayesNet import BayesNet
from MarginalDistributions import MarginalDistributions
from NetworkPruning import NetworkPruning
from Ordering import Ordering


class MapAndMpe(BNReasoner):
    def __init__(self, net: Union[str, BayesNet], query: set, evidence: set):
        super().__init__(net)
        self.query = query
        self.evidence = evidence
        self.res = {}

    def execute(self):
        pass

    def map(self):
        pruner = NetworkPruning(self.bn, self.query, self.evidence)
        pruned_bn = pruner.execute()

        q = pruned_bn.get_all_variables()
        order = Ordering(self.bn)
        # if order == 'min_degree':
        #     q = order.min_degree(q, priority=[var for var in Q if var not in query])
        # elif order == 'min_fill':
        #     q = order.min_fill(q, priority=[var for var in Q if var not in query])
        s = list(self.bn.get_all_cpts().values())

        for variable in q:
            factors = []
            for cpt in s:
                if variable in cpt.columns:
                    factors.append(cpt)
            multiplied_factors = multiply_factors(factors, variable)
            if variable in self.query:
                res_factors = self.max_factors(multiplied_factors, variable)
            else:
                marginalize = MarginalDistributions(self.bn, variable)
                res_factors = marginalize.execute()
            column_names = [list(factor.columns) for factor in factors]
            for indx, cpt in enumerate(s):
                if list(cpt.columns) in column_names:
                    s.pop(indx)
            s.append(res_factors)

        result = pd.DataFrame({'p': [1.0], 'MAP': [self.res]})
        result['p'] = []
        for i in range(len(s) - 1):
            result['p'].append(s[i].iloc[0]['p'] * s[i + 1].iloc[0]['p'])
        return result

    def mpe(self, order: str):

        pruner = NetworkPruning(self.bn, self.query, self.evidence)
        pruned_bn = pruner.prune_edges(self.bn)
        q = pruned_bn.get_all_variables()
        order = Ordering(self.bn)
        # if order == 'min_degree':
        #     q = order.min_degree(q)
        # elif order == 'min_fill':
        #     q = order.min_fill(q)

        s = list(self.bn.get_all_cpts().values())

        for variable in q:
            factors = []
            for cpt in s:
                if variable in cpt.columns:
                    factors.append(cpt)
            multiplied_factors = multiply_factors(factors, variable)
            maximized_factors = self.max_factors_instances(multiplied_factors, variable)
            column_names = [list(factor.columns) for factor in factors]
            for indx, cpt in enumerate(s):
                if list(cpt.columns) in column_names:
                    s.pop(indx)
            s.append(maximized_factors)

        result = pd.DataFrame({'p': [1.0], 'MPE': [self.res]})
        result['p'] = []
        for i in range(len(s) - 1):
            result['p'].append(s[i].iloc[0]['p'] * s[i + 1].iloc[0]['p'])
        return result

    def edge_pruning(self):
        pass

    def max_factors_instances(self, factors, variable):
        values = factors[variable].unique()
        maximums = []
        for value in values:
            idxmax = factors.loc[factors[variable] == value]['p'].idxmax()
            maximum = factors.loc[idxmax]
            maximums.append(maximum)
        factors = pd.concat(maximums).reset_index().transpose()

        for instance in factors:
            self.res[factors[instance].columns[-2]] = factors[instance].loc[instance, factors[instance].columns[-2]]
        return self.res

    def max_factors(self, factor, variable):
        max_true_value = factor.loc[factor[variable]].max().to_frame()
        max_false_value = factor.loc[not factor[variable]].max().to_frame()

        factor = pd.concat([max_true_value, max_false_value]).reset_index().transpose()

        return factor
