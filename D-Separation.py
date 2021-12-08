from BNReasoner import BNReasoner
from BayesNet import BayesNet
from collections import deque
from typing import Union, set
import networkx as nx


class DSeparation(BNReasoner):
    def __init__(self, net: Union[str, BayesNet], X: set, Y: set, Z: set):
        super().__init__(net)
        self.X, self.Y, self.Z = X, Y, Z

    def execute(self):
        result = self.dsep(X, Y, Z)
        return result

    def dsep(self, X, Y, Z):
        XYZ = X.union(Y).union(Z)

        # Pruning Step 1: Find and remove leaf nodes that are not part of the X, Y, Z union.
        #
        l_nodes = deque()
        for node in self.nodes:
            if len(self.bn.get_children(node)) == 0:
                l_nodes.append(node)
        while len(l_nodes) > 0:
            l = l_nodes.popleft()
            if l not in XYZ:
                for p in self.predecessors(l):
                    if self.out_degree[p] == 1:
                        l_nodes.append(p)
                self.bn.del_var(l)
        
        # Pruning Step 2: Removes all edges outgoing from nodes in Z.
        #
        self.remove_edges_from(list(self.out_edge(Z)))  

        # To check closedness via Z.
        #
        

X, Y, Z = {"bowel-problem"}, {"light-on"}, {"hear-bark"}
bnReasoner = DSeparation('testing/dog_problem.BIFXML', X, Y, Z)
bnReasoner.execute()

