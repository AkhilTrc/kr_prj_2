import copy
from typing import Union, Set

from BNReasoner import BNReasoner
from BayesNet import BayesNet


class NetworkPruning(BNReasoner):
    def __init__(self, net: Union[str, BayesNet], query: set, evidence: {}):
        super().__init__(net)
        self.query = query
        self.evidence = evidence

    def prune_nodes(self):
        nodes = set(self.bn.get_all_variables())
        leaves = self.get_leaf_nodes(nodes)
        remaining_nodes = self.query.union(self.evidence)
        bn_copy = copy.deepcopy(self.bn)
        for leaf in leaves:
            if leaf not in remaining_nodes:
                bn_copy.del_var(leaf)
        return bn_copy

    def prune_edges(self, pruned_bn):
        for e in self.evidence:
            edges = []
            for f, t in self.bn.structure.edges(nbunch=self.evidence):
                edges.append(t)
            for edge in edges:
                pruned_bn.del_edge((e, edge))
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


# query = {"X"}
# evidence = {"J"}
# bnReasoner = NetworkPruning('testing/lecture_example2.BIFXML', query, evidence)
# bnReasoner.bn = bnReasoner.execute()
# bnReasoner.bn.draw_structure()
