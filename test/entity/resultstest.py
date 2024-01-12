import unittest

from entity.results import Results


class ResultTest(unittest.TestCase):
    result = None

    def setUp(self):
        self.results = Results()

    def test_empty_results(self):
        self.assertEqual([], self.results.all_results)


if __name__ == "__main__":
    unittest.main()
