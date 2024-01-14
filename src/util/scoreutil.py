from constants.mastermindconstants import MastermindConstants


def calculate_score(num_of_guesses):
    if not 1 <= num_of_guesses <= MastermindConstants.MAX_NUM_OF_GUESSES:
        raise ValueError("number of guesses must be between 1 and " +
                         str(MastermindConstants.MAX_NUM_OF_GUESSES) + " inclusive")

    return (MastermindConstants.MAX_NUM_OF_GUESSES - num_of_guesses + 1) * 100
