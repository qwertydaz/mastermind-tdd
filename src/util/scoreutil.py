from constants.mastermindconstants import MastermindConstants


def calculate_score(num_of_guesses):
    if num_of_guesses < 1:
        raise ValueError("number of guesses must be greater or equal to 1")

    return (MastermindConstants.MAX_NUM_OF_GUESSES - num_of_guesses + 1) * 100
