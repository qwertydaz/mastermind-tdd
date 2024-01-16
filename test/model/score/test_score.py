import unittest

from src.model.result.win import Win
from src.constants.mastermindconstants import MastermindConstants
from src.model.score.score import Score


class ScoreTest(unittest.TestCase):
    score = None

    def setUp(self):
        self.score = Score()

    def test_initial_score(self):
        self.assertEqual(0, self.score.current_score)

    def test_score_after_first_win_in_1_guess_and_10_seconds(self):
        win = Win(1, 10.0)
        self.score.update_score(win)
        self.assertEqual(1500, self.score.current_score)

    def test_score_after_win_with_guesses_outside_valid_range(self):
        with self.assertRaises(ValueError):
            win = Win(-1, 10.0)
            self.score.update_score(win)
        with self.assertRaises(ValueError):
            win = Win(0, 10.0)
            self.score.update_score(win)
        with self.assertRaises(ValueError):
            win = Win(MastermindConstants.MAX_NUM_OF_GUESSES + 1, 10.0)
            self.score.update_score(win)

    def test_score_after_win_with_guesses_as_invalid_datatype(self):
        with self.assertRaises(TypeError):
            win = Win("1", 10.0)
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win("helloworld", 10.0)
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win(5.0, 10.0)
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win(True, 10.0)
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win(None, 10.0)
            self.score.update_score(win)


if __name__ == "__main__":
    unittest.main()
