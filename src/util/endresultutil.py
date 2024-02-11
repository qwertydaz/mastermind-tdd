from src.constants.mastermindconstants import WINNING_RESULT
from src.model.endresults.win import Win
from src.model.endresults.loss import Loss


def evaluate_end_result(results, time_taken):
    if results.get_last_result() == WINNING_RESULT:
        return Win(results.get_num_of_guesses(), time_taken)

    return Loss(time_taken)
