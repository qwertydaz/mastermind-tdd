import unittest

from entity.player import Player
from enums.colour import Colour
from stubs.mastermindstub import MastermindStub


class PlayerTest(unittest.TestCase):
    player = None
    ms = None

    @classmethod
    def setUpClass(cls):
        cls.player = Player()
        cls.ms = MastermindStub()

    def tearDown(self):
        self.player.reset_win_loss()

    def test_default_name(self):
        self.assertEqual("Player", self.player.name)

    def test_initialise_name(self):
        self.player = Player("Test")
        self.assertEqual("Test", self.player.name)

    def test_initial_win_count(self):
        self.assertEqual(0, self.player.wins)

    def test_win_count_after_win(self):
        self.ms.player = self.player
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        self.ms.guess(choice)

        self.assertEqual(1, self.player.wins)

    def test_win_count_after_loss(self):
        self.ms.player = self.player

        for i in range(10):
            self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
            choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK]
            self.ms.guess(choice)

        self.assertEqual(0, self.player.wins)

    def test_loss_count_after_loss(self):
        self.ms.player = self.player

        for i in range(10):
            self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
            choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK]
            self.ms.guess(choice)

        self.assertEqual(1, self.player.losses)

    def test_loss_count_after_win(self):
        self.ms.player = self.player
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        self.ms.guess(choice)

        self.assertEqual(0, self.player.losses)

    def test_win_loss_ratio_after_1_win_0_losses(self):
        self.ms.player = self.player

        # WIN
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        self.assertEqual(1.0, self.player.win_loss_ratio)

    def test_win_loss_ratio_after_20_wins_0_losses(self):
        self.ms.player = self.player

        # WIN
        for i in range(20):
            self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
            choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
            self.ms.guess(choice)

        self.assertEqual(20.0, self.player.win_loss_ratio)


if __name__ == '__main__':
    unittest.main()
