import copy
from typing import Union
from BNReasoner import BNReasoner
from BayesNet import BayesNet
import pandas as pd


class MarginalDistributions(BNReasoner):
    def __init__(self, net: Union[str, BayesNet], factor: pd.DataFrame, varibales:str):
        super().__init__(net)
        self.factor = factor
        self.varibales =  varibales


    def execute(self):
        result = self.get__all_cpts_for_x(self.varibales)
        # print(result['family-out'])
        return result

    def get__all_cpts_for_x(self, X):
        all_cpts = self.bn.get_all_cpts()
        factor = []
        for var_name in all_cpts:
            # print(var_name)
            if var_name == X:
                factor.append(all_cpts[var_name])
            elif X in all_cpts[var_name].columns:
                factor.append(all_cpts[var_name])
        if factor != []:
            combined_cpt = self.multiply_factors(factor, X)
            factor_over_var = self.sum_out(combined_cpt, X)
            print(factor_over_var)
        # print(self.sum_out(factor_over_car, X))
        return factor

    def multiply_factors():
        pass


    def sum_out(self, cpt: pd.DataFrame, variable: str) -> pd.DataFrame:
        
        columns = [column for column in cpt if (column != 'p' and column != variable)]

        partition_t = cpt[variable] == True
        partition_t_cpt= cpt[partition_t].drop(variable, axis=1)
        partition_f_cpt = cpt[~partition_t].drop(variable, axis=1)

        print(columns)
        summed_cpt = pd.concat([partition_t_cpt, partition_f_cpt]).groupby(columns, as_index=False)["p"].sum()
        return summed_cpt

    def multiply_factors(self, cpts: list[pd.DataFrame], variable) -> pd.DataFrame:
        # print(cpts.split())
        cpt1, cpt2 = cpts
        combined_cpt = pd.merge(left = cpt1, right = cpt2, on=variable, how='inner')
        # print(combined_cpt)

        combined_cpt['p'] = (combined_cpt['p_x'] * combined_cpt['p_y'])
        combined_cpt.drop(['p_x', 'p_y'], inplace=True, axis=1)
        return combined_cpt

    def reduce_using_evidence():

        pass


variable = "bowel-problem"
bnReasoner = MarginalDistributions('testing/dog_problem.BIFXML', variable, variable)
bnReasoner.execute()
    
