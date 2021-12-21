from BNReasoner import BNReasoner
from BayesNet import BayesNet
from collections import deque
from typing import Union ################################## set
import networkx as nx
from networkx.utils import UnionFind


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
        for node in set(self.bn.get_all_variables()):
            if len(self.bn.get_children(node)) == 0:
                l_nodes.append(node)
        while len(l_nodes) > 0:
            l = l_nodes.popleft()
            if l not in XYZ:
                for p in self.bn.get_parents(l):
                    if len(self.bn.get_children(p)) == 1:
                        l_nodes.append(p)
                self.bn.del_var(l)
        
        # Pruning Step 2: Removes all edges outgoing from nodes in Z.
        #
        # for edge in list(self.bn.structure.out_edge(Z)):
            # self.bn.del_edge(edge[0], edge[1])
            # self.bn.del_edges_from(list(self.out_edge(Z)))  

        self.bn.del_edges_from(self.bn.get_out_edge(Z))

        # To find connected paths in the pruned graph G'.
        # Ignoring Directedness i.e. udg -> Undirected Graph represented using disjoint sets.
        # Get weakly connected components.
        # 
        udg = UnionFind(set(self.bn.get_all_variables()))
        g = self.bn.copy_graph()
        for w_node in self.bn.wcc():        # Error here.
            udg.union(*w_node) 
        # Merge all. 
        udg.union(*X)
        udg.union(*Y)

        # False if atleast one connection found.
        #
        if X and Y and udg[next(iter(X))] == udg[next(iter(Y))]:
            return False
        else:
            return True 
        
        
X, Y, Z = {"light-on"}, {"dog-out"}, {"family-out"}
bnReasoner = DSeparation('testing/dog_problem.BIFXML', X, Y, Z)
print (bnReasoner.execute())

