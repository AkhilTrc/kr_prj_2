import copy
from typing import Union
from BNReasoner import BNReasoner, sum_out
from BayesNet import BayesNet
import pandas as pd


class MarginalDistributions(BNReasoner):
    def __init__(self, net: Union[str, BayesNet], varibales: str):
        super().__init__(net)
        self.varibales = varibales

    def execute(self):
        pass
        # result = self.marginal_joint(self.varibales)
        # print(result['family-out'])
        # return result

    # P(Q)
    def marginal_joint(self, Q: list):

        # load the network / cpt
        all_cpts = self.bn.get_all_cpts()

        # get order for Q
        order_for_Q = []
        if order_for_Q > 0:
            for i in order_for_Q:
                self.var_elimination(i)

    # compute elimination for each variable other than Q
    def marginal_posterior(self):
        all_cpts = self.bn.get_all_cpts()

    def var_elimination(self, X):
        all_cpts = self.bn.get_all_cpts()
        factor = []
        projection_over = ''
        for var_name in all_cpts:
            # print(var_name)
            if var_name == X:
                factor.append(all_cpts[var_name])
            elif X in all_cpts[var_name].columns:
                projection_over = var_name
                factor.append(all_cpts[var_name])
        if factor != []:
            combined_cpt = self.multiply_factors(factor, X)
            factor_over_var = sum_out(combined_cpt, X)
            self.bn.update_cpt(projection_over, factor_over_var)

    def multiply_factors(self):
        pass

    def multiply_factors(self, cpts: list[pd.DataFrame], variable) -> pd.DataFrame:
        # print(cpts.split())
        cpt1, cpt2 = cpts
        combined_cpt = pd.merge(left=cpt1, right=cpt2, on=variable, how='inner')
        # print(combined_cpt)

        combined_cpt['p'] = (combined_cpt['p_x'] * combined_cpt['p_y'])
        combined_cpt.drop(['p_x', 'p_y'], inplace=True, axis=1)
        return combined_cpt

    def reduce_using_evidence(self):

        pass


variables = {"bowel-problem", "family-out"}
bnReasoner = MarginalDistributions('testing/dog_problem.BIFXML', variables)
bnReasoner.execute()
