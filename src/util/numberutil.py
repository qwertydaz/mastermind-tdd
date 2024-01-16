from src.constants.mastermindconstants import MastermindConstants


def is_num_of_guesses_valid(num_of_guesses):
    if not isinstance(num_of_guesses, int) or type(num_of_guesses) is bool:
        raise TypeError("number of guesses must be an integer")
    if not 1 <= num_of_guesses <= MastermindConstants.MAX_NUM_OF_GUESSES:
        raise ValueError("number of guesses must be between 1 and " +
                         str(MastermindConstants.MAX_NUM_OF_GUESSES) + " inclusive")

    return True


def is_time_taken_in_seconds_valid(time_taken_in_seconds):
    if not isinstance(time_taken_in_seconds, float) or type(time_taken_in_seconds) is bool:
        raise TypeError("time taken in seconds must be a float")
    if time_taken_in_seconds <= 0.0:
        raise ValueError("time taken in seconds must be greater than 0.0")

    return True
