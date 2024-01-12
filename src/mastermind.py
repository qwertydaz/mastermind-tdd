from random import Random

from constants.mastermindconstants import MastermindConstants
from enums.colour import Colour


class Mastermind:
    def __init__(self):
        self.random = Random()
        self.code = []
        self.player = None
        self.guesses = 0

    def _generate_code(self):
        colours = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW, Colour.BLACK]
        self.code = self.random.choices(colours, k=4)

    def _handle_win_loss_count(self, result):
        if result == MastermindConstants.WINNING_RESULT:
            self.player.wins += 1
        elif self.guesses == MastermindConstants.MAX_GUESSES:
            self.player.losses += 1

    def guess(self, guess):
        self.guesses += 1
        result = [0, 0]

        for i in range(len(self.code)):
            if guess[i] == self.code[i]:
                result[0] += 1
            elif guess[i] in self.code:
                result[1] += 1

        self._handle_win_loss_count(result)

        return result
