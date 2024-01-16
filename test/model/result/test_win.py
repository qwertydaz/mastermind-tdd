import unittest

from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES
from src.model.result.endresult import EndResult
from src.model.result.win import Win


class WinTest(unittest.TestCase):
    def test_num_of_guesses_for_valid_win(self):
        win = Win(1, 10.0)
        self.assertEqual(1, win.num_of_guesses)

    def test_win_with_invalid_range_of_guesses(self):
        with self.assertRaises(ValueError):
            Win(-1, 10.0)
        with self.assertRaises(ValueError):
            Win(0, 10.0)
        with self.assertRaises(ValueError):
            Win(MAX_NUM_OF_GUESSES + 1, 10.0)

    def test_win_with_invalid_datatypes_for_guesses(self):
        with self.assertRaises(TypeError):
            Win("1", 10.0)
        with self.assertRaises(TypeError):
            Win(1.0, 10.0)
        with self.assertRaises(TypeError):
            Win(None, 10.0)
        with self.assertRaises(TypeError):
            Win(True, 10.0)

    def test_time_taken_in_seconds_for_valid_win(self):
        win = Win(1, 10.0)
        self.assertEqual(10.0, win.time_taken)

    def test_win_with_invalid_range_of_time_taken_in_seconds(self):
        with self.assertRaises(ValueError):
            Win(1, -1.0)
        with self.assertRaises(ValueError):
            Win(1, 0.0)

    def test_win_with_invalid_datatypes_for_time_taken_in_seconds(self):
        with self.assertRaises(TypeError):
            Win(1, "10.0")
        with self.assertRaises(TypeError):
            Win(1, 10)
        with self.assertRaises(TypeError):
            Win(1, None)
        with self.assertRaises(TypeError):
            Win(1, True)

    def test_win_is_instance_of_end_result(self):
        win = Win(1, 10.0)
        self.assertIsInstance(win, EndResult)


if __name__ == "__main__":
    unittest.main()
