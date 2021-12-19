import unittest

from NetworkPruning import NetworkPruning


class MyTestCase(unittest.TestCase):
    def test_pruning(self):
        X = {"X"}
        Y = {"I"}
        Z = {"J"}
        bnReasoner = NetworkPruning('testing/lecture_example2.BIFXML', X, Y, Z)
        bnReasoner.bn = bnReasoner.execute()
        bnReasoner.bn.draw_structure()
        self.assertEqual(len(bnReasoner.bn.get_all_variables()), 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
