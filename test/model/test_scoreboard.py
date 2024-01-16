import unittest

from stubs.stub_mastermind import MastermindStub
from enums.colour import Colour
from src.model.player import Player


class ScoreboardTest(unittest.TestCase):
    player = None
    ms = None

    def setUp(self):
        self.player = Player("scoreboardTest")
        self.ms = MastermindStub(self.player)

    def test_empty_scores(self):
        self.assertEqual([], self.ms.scoreboard.get_scores())

    def test_scoreboard_after_1_win(self):
        # WIN
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        self.assertEqual


if __name__ == "__main__":
    unittest.main()
