import unittest

from constants.mastermindconstants import MastermindConstants
from src.entity.result.endresult import EndResult
from src.entity.result.win import Win


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
            Win(MastermindConstants.MAX_NUM_OF_GUESSES + 1, 10.0)

    def test_win_with_invalid_datatypes_for_guesses(self):
        with self.assertRaises(TypeError):
            Win("1", 10.0)
        with self.assertRaises(TypeError):
            Win(1.0, 10.0)
        with self.assertRaises(TypeError):
            Win(None, 10.0)
        with self.assertRaises(TypeError):
            Win(True, 10.0)

    def test_win_is_instance_of_end_result(self):
        win = Win(1, 10.0)
        self.assertIsInstance(win, EndResult)


if __name__ == "__main__":
    unittest.main()
