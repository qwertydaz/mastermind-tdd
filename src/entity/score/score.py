from src.util.scoreutil import calculate_score


class Score:
    def __init__(self):
        self._current_score = 0

    @property
    def current_score(self):
        return self._current_score

    def update_score(self, num_of_guesses):
        self._current_score = calculate_score(num_of_guesses)
