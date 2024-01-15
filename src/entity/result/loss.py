from constants.mastermindconstants import MastermindConstants
from src.entity.result.endresult import EndResult


class Loss(EndResult):
    def __init__(self):
        super().__init__(MastermindConstants.MAX_NUM_OF_GUESSES)
