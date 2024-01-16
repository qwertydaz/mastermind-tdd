import unittest

from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES, TEN_SECONDS, ONE_GUESS
from src.util.scoreutil import calculate_score
from src.model.result.win import Win


class ScoreUtilTest(unittest.TestCase):
    def test_score_after_winning_in_1_guess_and_10_seconds(self):
        win = Win(ONE_GUESS, TEN_SECONDS)
        final_score = calculate_score(win)
        self.assertEqual(1500, final_score)

    def test_score_after_winning_in_max_guesses(self):
        win = Win(MAX_NUM_OF_GUESSES, TEN_SECONDS)
        final_score = calculate_score(win)
        self.assertEqual(600, final_score)

    def test_score_after_win_with_guesses_outside_valid_range(self):
        with self.assertRaises(ValueError):
            win = Win(-1, TEN_SECONDS)
            calculate_score(win)
        with self.assertRaises(ValueError):
            win = Win(0, TEN_SECONDS)
            calculate_score(win)
        with self.assertRaises(ValueError):
            win = Win(MAX_NUM_OF_GUESSES + 1, TEN_SECONDS)
            calculate_score(win)

    def test_score_after_win_with_guesses_as_invalid_datatype(self):
        with self.assertRaises(TypeError):
            win = Win("1", TEN_SECONDS)
            calculate_score(win)
        with self.assertRaises(TypeError):
            win = Win("helloworld", TEN_SECONDS)
            calculate_score(win)
        with self.assertRaises(TypeError):
            win = Win(5.0, TEN_SECONDS)
            calculate_score(win)
        with self.assertRaises(TypeError):
            win = Win(None, TEN_SECONDS)
            calculate_score(win)
        with self.assertRaises(TypeError):
            win = Win(True, TEN_SECONDS)
            calculate_score(win)

    def test_score_with_invalid_end_result(self):
        with self.assertRaises(TypeError):
            calculate_score(None)
        with self.assertRaises(TypeError):
            calculate_score("helloworld")
        with self.assertRaises(TypeError):
            calculate_score(1)


if __name__ == "__main__":
    unittest.main()
