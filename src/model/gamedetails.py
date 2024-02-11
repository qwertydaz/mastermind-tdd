class GameDetails:
    def __init__(self, player, results, score):
        self._player = player
        self._results = results
        self._score = score

    @property
    def player(self):
        return self._player

    @property
    def results(self):
        return self._results

    @property
    def score(self):
        return self._score
