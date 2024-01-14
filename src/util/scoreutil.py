from constants.mastermindconstants import MastermindConstants


def calculate_score(num_of_guesses):
    return (MastermindConstants.MAX_NUM_OF_GUESSES - num_of_guesses + 1) * 100
