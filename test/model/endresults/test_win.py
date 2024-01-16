import unittest

from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES, TEN_SECONDS, ONE_GUESS
from src.model.endresults.endresult import EndResult
from src.model.endresults.win import Win


class WinTest(unittest.TestCase):
    def test_num_of_guesses_for_valid_win(self):
        win = Win(ONE_GUESS, TEN_SECONDS)
        self.assertEqual(ONE_GUESS, win.num_of_guesses)

    def test_win_with_invalid_range_of_guesses(self):
        with self.assertRaises(ValueError):
            Win(-1, TEN_SECONDS)
        with self.assertRaises(ValueError):
            Win(0, TEN_SECONDS)
        with self.assertRaises(ValueError):
            Win(MAX_NUM_OF_GUESSES + 1, TEN_SECONDS)

    def test_win_with_invalid_datatypes_for_guesses(self):
        with self.assertRaises(TypeError):
            Win("1", TEN_SECONDS)
        with self.assertRaises(TypeError):
            Win(1.0, TEN_SECONDS)
        with self.assertRaises(TypeError):
            Win(None, TEN_SECONDS)
        with self.assertRaises(TypeError):
            Win(True, TEN_SECONDS)

    def test_time_taken_in_seconds_for_valid_win(self):
        win = Win(ONE_GUESS, TEN_SECONDS)
        self.assertEqual(TEN_SECONDS, win.time_taken)

    def test_win_with_invalid_range_of_time_taken_in_seconds(self):
        with self.assertRaises(ValueError):
            Win(ONE_GUESS, -1.0)
        with self.assertRaises(ValueError):
            Win(ONE_GUESS, 0.0)

    def test_win_with_invalid_datatypes_for_time_taken_in_seconds(self):
        with self.assertRaises(TypeError):
            Win(ONE_GUESS, "10.0")
        with self.assertRaises(TypeError):
            Win(ONE_GUESS, 10)
        with self.assertRaises(TypeError):
            Win(ONE_GUESS, None)
        with self.assertRaises(TypeError):
            Win(ONE_GUESS, True)

    def test_win_is_instance_of_end_result(self):
        win = Win(ONE_GUESS, TEN_SECONDS)
        self.assertIsInstance(win, EndResult)


if __name__ == "__main__":
    unittest.main()
