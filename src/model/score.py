from src.util.scoreutil import calculate_score
from src.util.endresultutil import evaluate_end_result
from src.util.numberutil import is_time_taken_valid
from src.model.results import Results, is_results_valid


class Score:
    def __init__(self):
        self._points = 0

    @property
    def points(self):
        return self._points

    def update_score(self, results: Results, time_taken: float):
        if is_results_valid(results) and is_time_taken_valid(time_taken):
            end_result = evaluate_end_result(results, time_taken)
            self._points = calculate_score(end_result)
