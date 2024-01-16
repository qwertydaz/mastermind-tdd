from src.util.numberutil import is_num_of_guesses_valid


class EndResult:
    def __init__(self, num_of_guesses):
        if is_num_of_guesses_valid(num_of_guesses):
            self._num_of_guesses = num_of_guesses

    @property
    def num_of_guesses(self):
        return self._num_of_guesses
