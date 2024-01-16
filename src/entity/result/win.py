from src.entity.result.endresult import EndResult


class Win(EndResult):
    def __init__(self, num_of_guesses, time_taken_in_seconds):
        super().__init__(num_of_guesses)
        self._time_taken_in_seconds = time_taken_in_seconds
