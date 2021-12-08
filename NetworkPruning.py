import copy
from typing import Union, Set

from BNReasoner import BNReasoner
from BayesNet import BayesNet


class NetworkPruning(BNReasoner):
    def __init__(self, net: Union[str, BayesNet], X: set, Y: set, Z: set):
        super().__init__(net)
        self.X = X
        self.Y = Y
        self.Z = Z

    def prune_nodes(self):
        nodes = set(self.bn.get_all_variables())
        leaves = self.get_leaf_nodes(nodes)
        remaining_nodes = self.X.union(self.Y).union(self.Z)
        bn_copy = copy.deepcopy(self.bn)
        for leaf in leaves:
            if leaf not in remaining_nodes:
                bn_copy.del_var(leaf)
        return bn_copy

    def prune_edges(self, pruned_bn):
        for z in self.Z:
            edges = []
            for f, t in self.bn.structure.edges(nbunch=self.Z):
                edges.append(t)
            for edge in edges:
                pruned_bn.del_edge((z, edge))
        return pruned_bn

    def execute(self):
        result = self.prune_nodes()
        result = self.prune_edges(result)
        return result

    def get_leaf_nodes(self, all_nodes):
        leaves = []
        for node in all_nodes:
            if len(self.bn.get_children(node)) == 0:
                leaves.append(node)
        return leaves


X = {"Wet Grass?"}
Y = {"Winter?"}
Z = {"Rain?"}
bnReasoner = NetworkPruning('testing/lecture_example2.BIFXML', X, Y, Z)
bnReasoner.execute()
bnReasoner.bn.draw_structure()
