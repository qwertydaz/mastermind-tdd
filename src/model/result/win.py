from src.model.result.endresult import EndResult
from src.util.numberutil import is_time_taken_in_seconds_valid


class Win(EndResult):
    def __init__(self, num_of_guesses, time_taken_in_seconds):
        super().__init__(num_of_guesses)

        if is_time_taken_in_seconds_valid(time_taken_in_seconds):
            self._time_taken_in_seconds = time_taken_in_seconds

    @property
    def time_taken_in_seconds(self):
        return self._time_taken_in_seconds
