class Player:
    def __init__(self, name="Player"):
        self.name = name
        self._wins = 0
        self._losses = 0
        self.win_loss_ratio = 1.0

    @property
    def wins(self):
        return self._wins

    def increment_wins(self):
        self._wins += 1
        self._update_win_loss_ratio()

    @property
    def losses(self):
        return self._losses

    def increment_losses(self):
        self._losses += 1
        self._update_win_loss_ratio()

    def reset_win_loss(self):
        self._wins = 0
        self._losses = 0
        self.win_loss_ratio = 1.0

    def _update_win_loss_ratio(self):
        self.win_loss_ratio = self._wins / (self._losses + 1)
