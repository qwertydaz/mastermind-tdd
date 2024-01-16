from src.util.scoreutil import calculate_score


class Score:
    def __init__(self):
        self._current_score = 0

    @property
    def current_score(self):
        return self._current_score

    def update_score(self, win):
        self._current_score = calculate_score(win)
