import unittest
from random import Random

from src.constants.mastermindconstants import WINNING_RESULT, MAX_NUM_OF_GUESSES
from src.model.player import Player
from src.enums.colour import Colour
from stubs.stub_mastermind import MastermindStub


class MastermindTest(unittest.TestCase):
    ms = None
    random = None

    @classmethod
    def setUpClass(cls):
        cls.random = Random()

    def setUp(self):
        self.ms = MastermindStub(Player())

    def test_player_name_is_correct(self):
        self.assertEqual("Player", self.ms.player.name)

    def test_generated_code_is_valid_length(self):
        self.ms._generate_code()
        self.assertEqual(4, len(self.ms.code))

    def test_generated_code_is_valid_datatype(self):
        for colour in self.ms.code:
            self.assertIn(colour, Colour)

    def test_win_with_1_guess(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        self.ms.guess(choice)
        self.assertEqual(WINNING_RESULT, self.ms.results.get_last_result())

    def test_lose_with_max_guesses(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        for i in range(MAX_NUM_OF_GUESSES):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)
            self.ms.guess(choice)

            self.assertNotEqual(WINNING_RESULT, self.ms.results.get_last_result())

    def test_win_with_max_guesses(self):
        for i in range(MAX_NUM_OF_GUESSES - 1):
            self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)

            self.ms.guess(choice)
            self.assertNotEqual(WINNING_RESULT, self.ms.results.get_last_result())

        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        self.ms.guess(choice)
        self.assertEqual(WINNING_RESULT, self.ms.results.get_last_result())

    def test_all_correct_colours_in_wrong_position(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.GREEN, Colour.YELLOW, Colour.RED, Colour.BLUE]

        self.ms.guess(choice)
        self.assertEqual([0, 4], self.ms.results.get_last_result())

    def test_win_with_duplicate_colours_in_code_and_guess(self):
        self.ms.code = [Colour.RED, Colour.RED, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.RED, Colour.GREEN, Colour.YELLOW]

        self.ms.guess(choice)
        self.assertEqual(WINNING_RESULT, self.ms.results.get_last_result())

    def test_duplicate_colours_in_code_and_wrong_guess(self):
        self.ms.code = [Colour.RED, Colour.RED, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.RED, Colour.YELLOW, Colour.GREEN]

        self.ms.guess(choice)
        self.assertEqual([2, 2], self.ms.results.get_last_result())

    def test_duplicate_colours_in_guess_in_wrong_position(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.BLUE, Colour.YELLOW]
        choice = [Colour.BLUE, Colour.RED, Colour.YELLOW, Colour.BLUE]

        self.ms.guess(choice)
        self.assertEqual([0, 4], self.ms.results.get_last_result())

    def test_duplicate_colours_in_guess_with_1_in_wrong_position(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.RED, Colour.YELLOW]
        choice = [Colour.RED, Colour.RED, Colour.BLACK, Colour.GREEN]

        self.ms.guess(choice)
        self.assertEqual([1, 1], self.ms.results.get_last_result())

    def test_win_with_1_colour_in_code(self):
        self.ms.code = [Colour.RED, Colour.RED, Colour.RED, Colour.RED]
        choice = [Colour.RED, Colour.RED, Colour.RED, Colour.RED]

        self.ms.guess(choice)
        self.assertEqual(WINNING_RESULT, self.ms.results.get_last_result())

    def test_1_colour_code_and_3_colour_guess(self):
        self.ms.code = [Colour.RED, Colour.RED, Colour.RED, Colour.RED]
        choice = [Colour.YELLOW, Colour.RED, Colour.BLUE, Colour.GREEN]

        self.ms.guess(choice)
        self.assertEqual([1, 0], self.ms.results.get_last_result())


if __name__ == "__main__":
    unittest.main()
