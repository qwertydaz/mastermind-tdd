from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES, ONE_GUESS


def is_num_of_guesses_valid(num_of_guesses):
    if not isinstance(num_of_guesses, int) or type(num_of_guesses) is bool:
        raise TypeError("number of guesses must be an integer")
    if not ONE_GUESS <= num_of_guesses <= MAX_NUM_OF_GUESSES:
        raise ValueError("number of guesses must be between 1 and " + str(MAX_NUM_OF_GUESSES) + " inclusive")

    return True


def is_time_taken_valid(time_taken):
    if not isinstance(time_taken, float) or type(time_taken) is bool:
        raise TypeError("time taken must be a float")
    if time_taken <= 0.0:
        raise ValueError("time taken must be greater than 0.0")

    return True
