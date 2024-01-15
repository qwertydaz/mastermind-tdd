import unittest

from constants.mastermindconstants import MastermindConstants
from src.entity.result.endresult import EndResult


class EndResultTest(unittest.TestCase):
    def test_end_result_with_invalid_range_of_guesses(self):
        with self.assertRaises(ValueError):
            EndResult(-1)
        with self.assertRaises(ValueError):
            EndResult(0)
        with self.assertRaises(ValueError):
            EndResult(MastermindConstants.MAX_NUM_OF_GUESSES + 1)

    def test_end_result_with_invalid_datatypes_for_guesses(self):
        with self.assertRaises(TypeError):
            EndResult("1")
        with self.assertRaises(TypeError):
            EndResult(1.0)
        with self.assertRaises(TypeError):
            EndResult(None)
        with self.assertRaises(TypeError):
            EndResult(True)


if __name__ == "__main__":
    unittest.main()
