import unittest

from constants.mastermindconstants import MastermindConstants
from src.entity.result.win import Win


class WinTest(unittest.TestCase):
    def test_valid_win(self):
        num_of_guesses = 1
        win = Win(num_of_guesses)

        self.assertEqual(1, win.num_of_guesses)

    def test_win_with_invalid_range_of_guesses(self):
        with self.assertRaises(ValueError):
            Win(-1)
        with self.assertRaises(ValueError):
            Win(0)
        with self.assertRaises(ValueError):
            Win(MastermindConstants.MAX_NUM_OF_GUESSES + 1)

    def test_win_with_invalid_datatypes_for_guesses(self):
        with self.assertRaises(TypeError):
            Win("1")
        with self.assertRaises(TypeError):
            Win(1.0)
        with self.assertRaises(TypeError):
            Win(None)
        with self.assertRaises(TypeError):
            Win(True)


if __name__ == "__main__":
    unittest.main()
