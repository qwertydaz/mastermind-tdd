import unittest

from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES, MAX_TIME_FOR_SCORE_BONUS, TEN_SECONDS, ONE_GUESS, \
    FIVE_GUESSES
from src.model.endresults.loss import Loss
from src.model.endresults.win import Win
from src.model.score import Score


class ScoreTest(unittest.TestCase):
    score = None

    def setUp(self):
        self.score = Score()

    def test_initial_score(self):
        self.assertEqual(0, self.score.current_score)

    def test_score_after_win_with_valid_guesses_and_10_seconds(self):
        win = Win(ONE_GUESS, TEN_SECONDS)
        self.score.update_score(win)
        self.assertEqual(1500, self.score.current_score)

        half_of_max_num_of_guesses = int(MAX_NUM_OF_GUESSES / 2)
        win = Win(half_of_max_num_of_guesses, TEN_SECONDS)
        self.score.update_score(win)
        self.assertEqual(1100, self.score.current_score)

        win = Win(MAX_NUM_OF_GUESSES, TEN_SECONDS)
        self.score.update_score(win)
        self.assertEqual(600, self.score.current_score)

    def test_score_after_win_with_5_guesses_and_valid_time_taken(self):
        win = Win(FIVE_GUESSES, 1.0)
        self.score.update_score(win)
        self.assertEqual(1100, self.score.current_score)

        less_than_50_percent_of_bonus_time = MAX_TIME_FOR_SCORE_BONUS / 2 - 2.0
        win = Win(FIVE_GUESSES, less_than_50_percent_of_bonus_time)
        self.score.update_score(win)
        self.assertEqual(850, self.score.current_score)

        exactly_50_percent_of_bonus_time = MAX_TIME_FOR_SCORE_BONUS / 2
        win = Win(FIVE_GUESSES, exactly_50_percent_of_bonus_time)
        self.score.update_score(win)
        self.assertEqual(850, self.score.current_score)

        more_than_50_percent_of_bonus_time = MAX_TIME_FOR_SCORE_BONUS / 2 + 2.0
        win = Win(FIVE_GUESSES, more_than_50_percent_of_bonus_time)
        self.score.update_score(win)
        self.assertEqual(725, self.score.current_score)

        win = Win(FIVE_GUESSES, MAX_TIME_FOR_SCORE_BONUS)
        self.score.update_score(win)
        self.assertEqual(600, self.score.current_score)

    def test_score_after_win_with_guesses_outside_valid_range(self):
        with self.assertRaises(ValueError):
            win = Win(-1, TEN_SECONDS)
            self.score.update_score(win)
        with self.assertRaises(ValueError):
            win = Win(0, TEN_SECONDS)
            self.score.update_score(win)
        with self.assertRaises(ValueError):
            win = Win(MAX_NUM_OF_GUESSES + 1, TEN_SECONDS)
            self.score.update_score(win)

    def test_score_after_win_with_time_taken_outside_valid_range(self):
        with self.assertRaises(ValueError):
            win = Win(ONE_GUESS, -1.0)
            self.score.update_score(win)
        with self.assertRaises(ValueError):
            win = Win(ONE_GUESS, 0.0)
            self.score.update_score(win)

    def test_score_after_win_with_guesses_as_invalid_datatype(self):
        with self.assertRaises(TypeError):
            win = Win("1", TEN_SECONDS)
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win("helloworld", TEN_SECONDS)
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win(5.0, TEN_SECONDS)
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win(True, TEN_SECONDS)
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win(None, TEN_SECONDS)
            self.score.update_score(win)

    def test_score_after_win_with_time_taken_as_invalid_datatype(self):
        with self.assertRaises(TypeError):
            win = Win(ONE_GUESS, "10.0")
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win(ONE_GUESS, 3)
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win(ONE_GUESS, None)
            self.score.update_score(win)
        with self.assertRaises(TypeError):
            win = Win(ONE_GUESS, True)
            self.score.update_score(win)

    def test_score_after_loss(self):
        self.score.update_score(Loss(TEN_SECONDS))
        self.assertEqual(0, self.score.current_score)


if __name__ == "__main__":
    unittest.main()
