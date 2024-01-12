from mastermind import Mastermind


class MastermindStub(Mastermind):
    def __init__(self, player=None):
        super().__init__(player)

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player
