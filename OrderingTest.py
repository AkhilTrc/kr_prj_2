import unittest

from Ordering import Ordering


class MyTestCase(unittest.TestCase):
    def test_ordering(self):
        orderer = Ordering("testing/dog_problem.BIFXML")
        X = ["light-on", "dog-out", "family-out"]
        result = orderer.min_degree(orderer.bn, X)
        print(result)


if __name__ == '__main__':
    unittest.main()
