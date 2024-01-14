import unittest

from constants.mastermindconstants import MastermindConstants
from entity.score.score import Score


class ScoreTest(unittest.TestCase):
    score = None

    def setUp(self):
        self.score = Score()

    def test_initial_score(self):
        self.assertEqual(0, self.score.current_score)

    def test_score_after_first_win(self):
        self.score.update_score(1)
        self.assertEqual(1000, self.score.current_score)

    def test_score_after_win_with_guesses_outside_valid_range(self):
        with self.assertRaises(ValueError):
            self.score.update_score(-1)
        with self.assertRaises(ValueError):
            self.score.update_score(0)
        with self.assertRaises(ValueError):
            self.score.update_score(MastermindConstants.MAX_NUM_OF_GUESSES + 1)

    def test_score_after_win_with_guesses_as_invalid_datatype(self):
        with self.assertRaises(TypeError):
            self.score.update_score("1")
        with self.assertRaises(TypeError):
            self.score.update_score("helloworld")
        with self.assertRaises(TypeError):
            self.score.update_score(5.0)
        with self.assertRaises(TypeError):
            self.score.update_score(True)


if __name__ == "__main__":
    unittest.main()
