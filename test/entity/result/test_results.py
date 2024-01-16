import unittest

from constants.mastermindconstants import MastermindConstants
from src.entity.player import Player
from enums.colour import Colour
from stubs.stub_mastermind import MastermindStub


class ResultTest(unittest.TestCase):
    ms = None
    random = None

    def setUp(self):
        self.ms = MastermindStub(Player())

    def test_empty_results(self):
        self.assertEqual([], self.ms.results.all_results)

    def test_add_result_after_win_in_1_guess(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        self.assertEqual([MastermindConstants.WINNING_RESULT], self.ms.results.all_results)

    def test_results_after_winning_on_last_guess(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK]

        nine_wrong_guesses = [
            [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW],
            [Colour.RED, Colour.RED, Colour.GREEN, Colour.YELLOW],
            [Colour.BLUE, Colour.BLUE, Colour.GREEN, Colour.YELLOW],
            [Colour.GREEN, Colour.BLUE, Colour.BLUE, Colour.YELLOW],
            [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW],
            [Colour.YELLOW, Colour.GREEN, Colour.BLUE, Colour.RED],
            [Colour.RED, Colour.YELLOW, Colour.GREEN, Colour.YELLOW],
            [Colour.BLACK, Colour.BLUE, Colour.GREEN, Colour.YELLOW],
            [Colour.BLACK, Colour.BLACK, Colour.GREEN, Colour.BLUE],
        ]

        correct_guess = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK]

        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES - 1):
            self.ms.guess(nine_wrong_guesses[i])

        self.ms.guess(correct_guess)

        self.assertEqual([[3, 0], [2, 1], [2, 1], [1, 2], [3, 0], [0, 3], [2, 0], [2, 1], [1, 3], [4, 0]],
                         self.ms.results.all_results)


if __name__ == "__main__":
    unittest.main()
