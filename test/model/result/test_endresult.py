import unittest

from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES
from src.model.result.endresult import EndResult


class EndResultTest(unittest.TestCase):
    def test_end_result_with_valid_guesses_and_time_taken(self):
        end_result = EndResult(1, 10.0)
        self.assertEqual(1, end_result.num_of_guesses)
        self.assertEqual(10.0, end_result.time_taken)

    def test_end_result_with_invalid_range_of_guesses(self):
        with self.assertRaises(ValueError):
            EndResult(-1, 10.0)
        with self.assertRaises(ValueError):
            EndResult(0, 10.0)
        with self.assertRaises(ValueError):
            EndResult(MAX_NUM_OF_GUESSES + 1, 10.0)

    def test_end_result_with_invalid_datatypes_for_guesses(self):
        with self.assertRaises(TypeError):
            EndResult("1", 10.0)
        with self.assertRaises(TypeError):
            EndResult(1.0, 10.0)
        with self.assertRaises(TypeError):
            EndResult(None, 10.0)
        with self.assertRaises(TypeError):
            EndResult(True, 10.0)


if __name__ == "__main__":
    unittest.main()
