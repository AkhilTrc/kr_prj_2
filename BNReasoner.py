from typing import Union
from BayesNet import BayesNet
from abc import ABC, abstractmethod
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import pandas as pd


def sum_out(cpt: pd.DataFrame, variable: str) -> pd.DataFrame:

    columns = [column for column in cpt if (column != 'p' and column != variable)]

    partition_t = cpt[variable] == True
    partition_t_cpt = cpt[partition_t].drop(variable, axis=1)
    partition_f_cpt = cpt[~partition_t].drop(variable, axis=1)

    print(columns)
    summed_cpt = pd.concat([partition_t_cpt, partition_f_cpt]).groupby(columns, as_index=False)["p"].sum()
    return summed_cpt


class BNReasoner(ABC):
    def __init__(self, net: Union[str, BayesNet]):
        """
        :param net: either file path of the bayesian network in BIFXML format or BayesNet object
        """
        if type(net) == str:
            # constructs a BN object
            self.bn = BayesNet()
            # Loads the BN from an BIFXML file
            self.bn.load_from_bifxml(net)
        else:
            self.bn = net

    # TODO: This is where your methods should go

    @abstractmethod
    def execute(self):
        pass
