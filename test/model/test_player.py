import unittest
from random import Random

from src.constants.mastermindconstants import MastermindConstants
from src.model.player import Player
from src.enums.colour import Colour
from stubs.stub_mastermind import MastermindStub


# TODO: add mock to track how many times increment_losses() and increment_wins() are called
class PlayerTest(unittest.TestCase):
    ms = None
    random = None

    @classmethod
    def setUpClass(cls):
        cls.random = Random()

    def setUp(self):
        self.ms = MastermindStub(Player())

    def tearDown(self):
        self.ms.player.reset_win_loss()

    def test_default_name(self):
        self.assertEqual("Player", self.ms.player.name)

    def test_initialise_name(self):
        self.ms.player = Player("Test")
        self.assertEqual("Test", self.ms.player.name)

    def test_initial_win_count(self):
        self.assertEqual(0, self.ms.player.wins)

    def test_win_count_after_win(self):
        # WIN
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        self.assertEqual(1, self.ms.player.wins)

    def test_win_count_after_loss(self):
        # LOSS
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)
            self.ms.guess(choice)

        self.assertEqual(0, self.ms.player.wins)

    def test_loss_count_after_loss(self):
        # LOSS
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)
            self.ms.guess(choice)

        self.assertEqual(1, self.ms.player.losses)

    def test_loss_count_after_win(self):
        # WIN
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        self.assertEqual(0, self.ms.player.losses)

    def test_win_loss_ratio_after_1_win_0_losses(self):
        # WIN
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        self.assertEqual(1.0, self.ms.player.win_loss_ratio)

    def test_win_loss_ratio_after_20_wins_0_losses(self):
        # WIN
        for i in range(20):
            self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
            choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
            self.ms.guess(choice)

        self.assertEqual(20.0, self.ms.player.win_loss_ratio)

    def test_win_loss_ratio_after_0_wins_1_loss(self):
        # LOSS
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)
            self.ms.guess(choice)

        self.assertEqual(0.0, self.ms.player.win_loss_ratio)

    def test_win_loss_ratio_after_0_wins_20_losses(self):
        # LOSS
        for i in range((MastermindConstants.MAX_NUM_OF_GUESSES * 20)):
            # simulate a code reset after a game is lost
            if i % 20 == 0:
                self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]

            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)
            self.ms.guess(choice)

        self.assertEqual(0.0, self.ms.player.win_loss_ratio)

    def test_win_loss_ratio_after_1_win_then_1_loss(self):
        # WIN
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        # LOSS
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)
            self.ms.guess(choice)

        self.assertEqual(1.0, self.ms.player.win_loss_ratio)

    def test_win_loss_ratio_after_1_loss_then_1_win(self):
        # LOSS
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)
            self.ms.guess(choice)

        # WIN
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        self.assertEqual(1.0, self.ms.player.win_loss_ratio)

    def test_win_loss_ratio_after_1_win_then_1_loss_then_1_win(self):
        # WIN
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        # LOSS
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)
            self.ms.guess(choice)

        # WIN
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        self.assertEqual(2.0, self.ms.player.win_loss_ratio)

    def test_win_loss_ratio_after_1_loss_then_1_win_then_1_loss(self):
        # LOSS
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLACK], k=4)
            self.ms.guess(choice)

        # WIN
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        choice = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        self.ms.guess(choice)

        # LOSS
        self.ms.code = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW]
        for i in range(MastermindConstants.MAX_NUM_OF_GUESSES):
            choice = self.random.choices([Colour.RED, Colour.BLUE, Colour.GREEN, Colour.BLUE], k=4)
            self.ms.guess(choice)

        self.assertEqual(0.5, self.ms.player.win_loss_ratio)


if __name__ == "__main__":
    unittest.main()
