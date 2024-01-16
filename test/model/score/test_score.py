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

    def test_score_after_win_with_valid_guesses_and_10_seconds(self):
        win = Win(1, 10.0)
        self.score.update_score(win)
        self.assertEqual(1500, self.score.current_score)

        half_of_max_num_of_guesses = int(MastermindConstants.MAX_NUM_OF_GUESSES / 2)
        win = Win(half_of_max_num_of_guesses, 10.0)
        self.score.update_score(win)
        self.assertEqual(1100, self.score.current_score)

        win = Win(MastermindConstants.MAX_NUM_OF_GUESSES, 10.0)
        self.score.update_score(win)
        self.assertEqual(600, self.score.current_score)

    def test_score_after_win_with_5_guesses_and_valid_time_taken(self):
        win = Win(5, 1.0)
        self.score.update_score(win)
        self.assertEqual(1100, self.score.current_score)

        less_than_50_percent_of_bonus_time = MastermindConstants.MAX_TIME_FOR_SCORE_BONUS / 2 - 2.0
        win = Win(5, less_than_50_percent_of_bonus_time)
        self.score.update_score(win)
        self.assertEqual(850, self.score.current_score)

        exactly_50_percent_of_bonus_time = MastermindConstants.MAX_TIME_FOR_SCORE_BONUS / 2
        win = Win(5, exactly_50_percent_of_bonus_time)
        self.score.update_score(win)
        self.assertEqual(850, self.score.current_score)

        more_than_50_percent_of_bonus_time = MastermindConstants.MAX_TIME_FOR_SCORE_BONUS / 2 + 2.0
        win = Win(5, more_than_50_percent_of_bonus_time)
        self.score.update_score(win)
        self.assertEqual(725, self.score.current_score)

        win = Win(5, MastermindConstants.MAX_TIME_FOR_SCORE_BONUS)
        self.score.update_score(win)
        self.assertEqual(600, self.score.current_score)

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
