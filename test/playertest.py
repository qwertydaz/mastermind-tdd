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
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        for i in range(10):
            choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK]

            self.ms.guess(choice)

        self.assertEqual(0, self.player.wins)

    def test_loss_count_after_loss(self):
        self.ms.player = self.player
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

        for i in range(10):
            choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK]

            self.ms.guess(choice)

        self.assertEqual(1, self.player.losses)


if __name__ == '__main__':
    unittest.main()
