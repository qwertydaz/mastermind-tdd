import unittest
from random import Random

from constants.mastermindconstants import MastermindConstants
from entity.player import Player
from enums.colour import Colour
from stubs.mastermindstub import MastermindStub


class MastermindTest(unittest.TestCase):
    ms = None
    random = None

    @classmethod
    def setUpClass(cls):
        cls.ms = MastermindStub()
        cls.ms.player = Player()
        cls.random = Random()

    def test_win_with_1_guess(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        result = self.ms.guess(choice)
        self.assertEqual(MastermindConstants.WINNING_RESULT, result)

    def test_lose_with_max_guesses(self):
        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES):
            self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)

            result = self.ms.guess(choice)
            self.assertNotEqual(MastermindConstants.WINNING_RESULT, result)

    def test_win_with_max_guesses(self):
        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES - 1):
            self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)

            result = self.ms.guess(choice)
            self.assertNotEqual(MastermindConstants.WINNING_RESULT, result)

        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        result = self.ms.guess(choice)
        self.assertEqual(MastermindConstants.WINNING_RESULT, result)

    def test_all_correct_colours_in_wrong_position(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.GREEN, Colour.YELLOW, Colour.RED, Colour.BLUE]

        result = self.ms.guess(choice)
        self.assertEqual([0, 4], result)

    def test_win_with_duplicate_colours_in_code_and_guess(self):
        self.ms.code = [Colour.RED, Colour.RED, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.RED, Colour.GREEN, Colour.YELLOW]

        result = self.ms.guess(choice)
        self.assertEqual(MastermindConstants.WINNING_RESULT, result)

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
        self.assertEqual(MastermindConstants.WINNING_RESULT, result)

    def test_1_colour_code_and_3_colour_guess(self):
        self.ms.code = [Colour.RED, Colour.RED, Colour.RED, Colour.RED]
        choice = [Colour.YELLOW, Colour.RED, Colour.BLUE, Colour.GREEN]

        result = self.ms.guess(choice)
        self.assertEqual([1, 0], result)


if __name__ == "__main__":
    unittest.main()
