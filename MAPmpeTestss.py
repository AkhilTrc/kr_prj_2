import unittest


from MAPandMPE import MapAndMpe


class MyTestCase(unittest.TestCase):
    def test_map(self):
        query = {"X", "I"}
        evidence = {"J": True}
        bnReasoner = MapAndMpe('testing/crime_causes.BIFXML', query, evidence)
        reasoner_map = bnReasoner.map('min_degree')
        print(reasoner_map)  # add assertion here # add assertion here

    def test_mep(self):
        query = {"X", "I"}
        evidence = {"J": True}
        bnReasoner = MapAndMpe('testing/crime_causes.BIFXML', query, evidence)
        reasoner_map = bnReasoner.mpe('min_degree')
        print(reasoner_map)  # add assertion here # add assertion here


if __name__ == '__main__':
    unittest.main()
