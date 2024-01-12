import unittest
from random import Random

from enums.colour import Colour
from mastermind import Mastermind

MAX_GUESSES = 10
WINNING_RESULT = [4, 0]


class MastermindTest(unittest.TestCase):
    ms = None
    random = None

    @classmethod
    def setUpClass(cls):
        cls.ms = MastermindStub()
        cls.random = Random()

    def test_win_with_1_guess(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        result = self.ms.guess(choice)
        self.assertEqual(WINNING_RESULT, result)

    def test_lose_with_max_guesses(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        for i in range(MAX_GUESSES):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)

            result = self.ms.guess(choice)
            self.assertNotEqual(WINNING_RESULT, result)

    def test_win_with_max_guesses(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        for i in range(MAX_GUESSES - 1):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)

            result = self.ms.guess(choice)
            self.assertNotEqual(WINNING_RESULT, result)

        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        result = self.ms.guess(choice)
        self.assertEqual(WINNING_RESULT, result)

    def test_all_correct_colours_in_wrong_position(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.GREEN, Colour.YELLOW, Colour.RED, Colour.BLUE]

        result = self.ms.guess(choice)
        self.assertEqual([0, 4], result)

    def test_win_with_duplicate_colours_in_code_and_guess(self):
        self.ms.code = [Colour.RED, Colour.RED, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.RED, Colour.GREEN, Colour.YELLOW]

        result = self.ms.guess(choice)
        self.assertEqual(WINNING_RESULT, result)

    def test_duplicate_colours_in_code_and_wrong_guess(self):
        self.ms.code = [Colour.RED, Colour.RED, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.RED, Colour.YELLOW, Colour.GREEN]

        result = self.ms.guess(choice)
        self.assertEqual([2, 2], result)

    def test_duplicate_colours_in_guess_in_wrong_position(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.BLUE, Colour.YELLOW]
        choice = [Colour.BLUE, Colour.RED, Colour.YELLOW, Colour.BLUE]

        result = self.ms.guess(choice)
        self.assertEqual([0, 4], result)

    def test_duplicate_colours_in_guess_with_1_in_wrong_position(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.RED, Colour.YELLOW]
        choice = [Colour.RED, Colour.RED, Colour.BLACK, Colour.GREEN]

        result = self.ms.guess(choice)
        self.assertEqual([1, 1], result)

    def test_win_with_1_colour_in_code(self):
        self.ms.code = [Colour.RED, Colour.RED, Colour.RED, Colour.RED]
        choice = [Colour.RED, Colour.RED, Colour.RED, Colour.RED]

        result = self.ms.guess(choice)
        self.assertEqual(WINNING_RESULT, result)

    def test_1_colour_code_and_3_colour_guess(self):
        self.ms.code = [Colour.RED, Colour.RED, Colour.RED, Colour.RED]
        choice = [Colour.YELLOW, Colour.RED, Colour.BLUE, Colour.GREEN]

        result = self.ms.guess(choice)
        self.assertEqual([1, 0], result)


class MastermindStub(Mastermind):
    def __init__(self, code=None):
        super().__init__()
        self.code = code


if __name__ == "__main__":
    unittest.main()
