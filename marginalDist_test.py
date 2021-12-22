import unittest

from MarginalDistributions import MarginalDistributions


class MarginalDistTest(unittest.TestCase):
    def testMarginal(self):
        variables= {"Trauma", "Domestic Violence"}
        Evidence = {"Substance abuse": True, "Sociological factors": True}
        bnReasoner = MarginalDistributions('testing/crime_causes.BIFXML', variables, Evidence)
        result = bnReasoner.execute()
        print(result)

if __name__ == '__main__':
    unittest.main()
