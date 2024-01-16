from src.model.result.win import Win
from src.constants.mastermindconstants import MastermindConstants
from src.util.numberutil import is_num_of_guesses_valid, is_time_taken_in_seconds_valid


def calculate_score(win: Win):
    score_for_num_of_guesses = calculate_score_for_num_of_guesses(win.num_of_guesses)
    score_for_time_taken_in_seconds = calculate_score_for_time_taken_in_seconds(win.time_taken_in_seconds)

    return score_for_num_of_guesses + score_for_time_taken_in_seconds


def calculate_score_for_num_of_guesses(num_of_guesses):
    is_num_of_guesses_valid(num_of_guesses)
    return (MastermindConstants.MAX_NUM_OF_GUESSES - num_of_guesses + 1) * 100


def calculate_score_for_time_taken_in_seconds(time_taken_in_seconds):
    is_time_taken_in_seconds_valid(time_taken_in_seconds)

    if time_taken_in_seconds <= MastermindConstants.MAX_TIME_FOR_SCORE_BONUS * 0.25:
        return MastermindConstants.MAX_TIME_BONUS
    elif time_taken_in_seconds <= MastermindConstants.MAX_TIME_FOR_SCORE_BONUS * 0.5:
        return MastermindConstants.MAX_TIME_BONUS * 0.5
    elif time_taken_in_seconds <= MastermindConstants.MAX_TIME_FOR_SCORE_BONUS * 0.75:
        return MastermindConstants.MAX_TIME_BONUS * 0.25

    return 0
