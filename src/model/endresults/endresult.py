from src.util.numberutil import is_num_of_guesses_valid, is_time_taken_valid


class EndResult:
    def __init__(self, num_of_guesses, time_taken):
        if is_num_of_guesses_valid(num_of_guesses):
            self._num_of_guesses = num_of_guesses
        if is_time_taken_valid(time_taken):
            self._time_taken = time_taken

    @property
    def num_of_guesses(self):
        return self._num_of_guesses

    @property
    def time_taken(self):
        return self._time_taken
