from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES
from src.model.endresults.endresult import EndResult


class Loss(EndResult):
    def __init__(self, time_taken):
        super().__init__(MAX_NUM_OF_GUESSES, time_taken)
