import unittest

from entity.player import Player
from enums.colour import Colour
from stubs.mastermindstub import MastermindStub


class ResultTest(unittest.TestCase):
    ms = None

    def setUp(self):
        self.ms = MastermindStub(Player())

    def test_empty_results(self):

        self.assertEqual([], self.ms.results.all_results)

    def test_add_result_after_win_in_1_guess(self):
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        self.assertEqual([[4, 0]], self.ms.results.all_results)


if __name__ == "__main__":
    unittest.main()
