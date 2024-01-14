import unittest

from util.scoreutil import ScoreUtil


class ScoreUtilTest(unittest.TestCase):
    def test_score_after_winning_in_1_guess(self):
        num_of_guesses = 1
        final_score = ScoreUtil.calculate_score(num_of_guesses)
        self.assertEqual(1000, final_score)


if __name__ == "__main__":
    unittest.main()
