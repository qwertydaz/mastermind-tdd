import unittest

from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES, TEN_SECONDS, ONE_GUESS
from src.model.endresults.endresult import EndResult


class EndResultTest(unittest.TestCase):
    def test_end_result_with_valid_guesses_and_time_taken(self):
        end_result = EndResult(ONE_GUESS, TEN_SECONDS)
        self.assertEqual(ONE_GUESS, end_result.num_of_guesses)
        self.assertEqual(TEN_SECONDS, end_result.time_taken)

    def test_end_result_with_invalid_range_of_guesses(self):
        with self.assertRaises(ValueError):
            EndResult(-1, TEN_SECONDS)
        with self.assertRaises(ValueError):
            EndResult(0, TEN_SECONDS)
        with self.assertRaises(ValueError):
            EndResult(MAX_NUM_OF_GUESSES + 1, TEN_SECONDS)

    def test_end_result_with_invalid_datatypes_for_guesses(self):
        with self.assertRaises(TypeError):
            EndResult("1", TEN_SECONDS)
        with self.assertRaises(TypeError):
            EndResult(1.0, TEN_SECONDS)
        with self.assertRaises(TypeError):
            EndResult(None, TEN_SECONDS)
        with self.assertRaises(TypeError):
            EndResult(True, TEN_SECONDS)


if __name__ == "__main__":
    unittest.main()
