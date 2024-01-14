import unittest

from constants.mastermindconstants import MastermindConstants
from util.scoreutil import calculate_score


class ScoreUtilTest(unittest.TestCase):
    def test_score_after_winning_in_1_guess(self):
        final_score = calculate_score(1)
        self.assertEqual(1000, final_score)

    def test_score_after_winning_in_max_guesses(self):
        final_score = calculate_score(MastermindConstants.MAX_NUM_OF_GUESSES)
        self.assertEqual(100, final_score)

    def test_score_after_winning_with_negative_guesses(self):
        with self.assertRaises(ValueError):
            calculate_score(-1)

    def test_score_after_winning_with_more_than_max_guesses(self):
        with self.assertRaises(ValueError):
            calculate_score(MastermindConstants.MAX_NUM_OF_GUESSES + 1)


if __name__ == "__main__":
    unittest.main()
