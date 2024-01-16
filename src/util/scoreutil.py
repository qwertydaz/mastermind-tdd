from src.model.result.win import Win
from src.constants.mastermindconstants import MastermindConstants
from src.util.numberutil import is_num_of_guesses_valid, is_time_taken_in_seconds_valid


def calculate_score(win: Win):
    if is_num_of_guesses_valid(win.num_of_guesses):
        return (MastermindConstants.MAX_NUM_OF_GUESSES - win.num_of_guesses + 1) * 100 + 500
