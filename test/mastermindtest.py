import unittest
from random import Random

from colour import Colour
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


class MastermindStub(Mastermind):
    def __init__(self, code=None):
        super().__init__()
        self.code = code


if __name__ == "__main__":
    unittest.main()
