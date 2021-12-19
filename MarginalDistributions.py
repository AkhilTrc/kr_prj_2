import copy
from typing import Union
from BNReasoner import BNReasoner
from BayesNet import BayesNet
import pandas as pd


class MarginalDistributions(BNReasoner):
    def __init__(self, net: Union[str, BayesNet], varibales:str):
        super().__init__(net)
        self.varibales =  varibales


    def execute(self):
        result = self.get__all_cpts_for_x(self.varibales)
        # print(result['family-out'])
        return result
    
    #P(Q)
    def marginal_joint():

        #load the network / cpt

        #get order

        #compute elimination for each variable other than Q
        pass
    def marginal_posterior(self):
        all_cpts = self.bn.get_all_cpts()


        
    def get__all_cpts_for_x(self, X):
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
            factor_over_var = self.sum_out(combined_cpt, X)
            self.bn.update_cpt(projection_over, factor_over_var)
            print(self.bn.get_cpt(projection_over))
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


variables = {"bowel-problem","family-out"}
bnReasoner = MarginalDistributions('testing/dog_problem.BIFXML', "bowel-problem")
bnReasoner.execute()
    
