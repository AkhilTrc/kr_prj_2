import unittest

from MAPandMPE import MapAndMpe


class MyTestCase(unittest.TestCase):
    def test_mpe(self):
        query = {"X", "Y"}
        evidence = {"J": True}
        bnReasoner = MapAndMpe('testing/lecture_example2.BIFXML', query, evidence)
        reasoner_map = bnReasoner.mpe('min_degree')
        print(reasoner_map)  # add assertion here

    def test_map(self):
        query = {"X", "I"}
        evidence = {"Y": True}
        bnReasoner = MapAndMpe('testing/lecture_example2.BIFXML', query, evidence)
        reasoner_map = bnReasoner.map('min_degree')
        print(reasoner_map)  # add assertion here


if __name__ == '__main__':
    unittest.main()
