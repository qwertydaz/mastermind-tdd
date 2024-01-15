from constants.mastermindconstants import MastermindConstants
from src.util.intutil import is_num_of_guesses_valid


def calculate_score(num_of_guesses):
    if is_num_of_guesses_valid(num_of_guesses):
        return (MastermindConstants.MAX_NUM_OF_GUESSES - num_of_guesses + 1) * 100
