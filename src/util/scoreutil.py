from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES, MAX_TIME_FOR_SCORE_BONUS, MAX_TIME_BONUS
from src.util.numberutil import is_num_of_guesses_valid, is_time_taken_valid
from src.model.endresults.endresult import EndResult
from src.model.endresults.loss import Loss
from src.model.endresults.win import Win


def calculate_score(end_result: EndResult):
    if isinstance(end_result, Loss):
        return 0
    elif isinstance(end_result, Win):
        score_for_num_of_guesses = calculate_score_for_num_of_guesses(end_result.num_of_guesses)
        score_for_time_taken_in_seconds = calculate_score_for_time_taken_in_seconds(end_result.time_taken)

        return score_for_num_of_guesses + score_for_time_taken_in_seconds
    else:
        raise TypeError("invalid type for end_result")


def calculate_score_for_num_of_guesses(num_of_guesses):
    is_num_of_guesses_valid(num_of_guesses)

    return (MAX_NUM_OF_GUESSES - num_of_guesses + 1) * 100


def calculate_score_for_time_taken_in_seconds(time_taken_in_seconds):
    is_time_taken_valid(time_taken_in_seconds)

    if time_taken_in_seconds <= MAX_TIME_FOR_SCORE_BONUS * 0.25:
        return MAX_TIME_BONUS
    elif time_taken_in_seconds <= MAX_TIME_FOR_SCORE_BONUS * 0.5:
        return MAX_TIME_BONUS * 0.5
    elif time_taken_in_seconds <= MAX_TIME_FOR_SCORE_BONUS * 0.75:
        return MAX_TIME_BONUS * 0.25

    return 0


