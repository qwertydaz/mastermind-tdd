from random import Random

from src.constants.mastermindconstants import MastermindConstants
from src.model.result.results import Results
from src.model.score.scoreboard import Scoreboard
from src.enums.colour import Colour


class Mastermind:
    def __init__(self, player=None):
        self._random = Random()
        self._num_of_guesses = 0
        self._code = []

        # visible attributes
        self._player = player
        self._results = Results()
        self.scoreboard = Scoreboard()

    @property
    def player(self):
        return self._player

    @property
    def results(self):
        return self._results

    def _generate_code(self):
        colours = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW, Colour.BLACK]
        self.code = self._random.choices(colours, k=4)

    def _handle_win_loss_count(self, result):
        if result == MastermindConstants.WINNING_RESULT:
            self._player.increment_wins()
        elif self._num_of_guesses == MastermindConstants.MAX_NUM_OF_GUESSES:
            self._player.increment_losses()
            self._num_of_guesses = 0

    def guess(self, guess):
        self._num_of_guesses += 1
        result = [0, 0]

        for i in range(len(self.code)):
            if guess[i] == self.code[i]:
                result[0] += 1
            elif guess[i] in self.code:
                result[1] += 1

        self._handle_win_loss_count(result)
        self._results.add_result(result)
