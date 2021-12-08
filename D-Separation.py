from BNReasoner import BNReasoner
from collections import deque
import networkx as nx


class DSeparation(BNReasoner):
    def execute(self):
        pass

    def dsep(self, X, Y, Z):
        g = self.bn.copy()
        XYZ = X.union(Y).union(Z)

        # Find and remove leaf nodes that are not part of the x, y, z union.
        #
        l_nodes = deque()
        for node in g.nodes:
            if g.out_degree[node] == 0:     # Finds all the leaf nodes.
                l_nodes.append(node)
        while len(l_nodes) > 0:
            l = l_nodes.popleft()
            if l not in XYZ:
                # need a way to add parent to l.
                g.bn.del_var(l)

        g.remove_edges_from(g.out_edge(Z))  # Removes all edges outgoing from nodes in Z.

        # To check closedness via Z.
