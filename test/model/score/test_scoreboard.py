import unittest

from src.model.player import Player
from stubs.stub_mastermind import MastermindStub


class ScoreboardTest(unittest.TestCase):
    ms = None

    def setUp(self):
        self.ms = MastermindStub(Player())

    def test_empty_scores(self):
        self.assertEqual([], self.ms.scoreboard.get_scores())


if __name__ == "__main__":
    unittest.main()
