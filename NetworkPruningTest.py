import unittest

from NetworkPruning import NetworkPruning


class MyTestCase(unittest.TestCase):
    def test_pruning(self):
        X = {"Wet Grass?"}
        Y = {"Winter?"}
        Z = {"Rain?"}
        bnReasoner = NetworkPruning('testing/lecture_example2.BIFXML', X, Y, Z)
        bnReasoner.execute()
        bnReasoner.bn.draw_structure()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
