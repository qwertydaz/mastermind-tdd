from random import Random

from colour import Colour


class Mastermind:
    def __init__(self):
        self.random = Random()
        self.code = []

    def _generate_code(self):
        colours = [Colour.RED, Colour.BLUE, Colour.GREEN, Colour.YELLOW, Colour.BLACK]
        self.code = self.random.choices(colours, k=4)

    def guess(self, guess):
        result = [0, 0]

        for i in range(len(self.code)):
            if guess[i] == self.code[i]:
                result[0] += 1
            elif guess[i] in self.code:
                result[1] += 1

        return result
