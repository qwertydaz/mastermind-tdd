from constants.mastermindconstants import MAX_NUM_OF_GUESSES


def is_results_list_valid(results_list):
    if not isinstance(results_list, list):
        raise TypeError(f"results must be a list, not type {type(results_list)}")

    if not 1 <= len(results_list) <= MAX_NUM_OF_GUESSES:
        raise ValueError(f"results must contains at least 1 result and at most {str(MAX_NUM_OF_GUESSES)} results, "
                         f"not {str(len(results_list))} result(s)")

    return all(is_result_valid(result) for result in results_list)


def is_result_valid(result):
    if not isinstance(result, list) and len(result) == 2:
        raise TypeError("each result must be a list of length 2, not type {type(result)} and length {len(result)}")

    if not isinstance(result[0], int) and isinstance(result[1], int):
        raise TypeError("each result must comprise of 2 integers, not type {type(result[0])} and "
                        "type {type(result[1])}")

    return True


def is_results_valid(results):
    if not isinstance(results, Results):
        raise TypeError(f"results must be Results, not type {type(results)}")

    return is_results_list_valid(results.all_results)


class Results:
    def __init__(self):
        self._all_results = []

    def add_result(self, result):
        if is_result_valid(result):
            self._all_results.append(result)

    @property
    def all_results(self):
        return self._all_results

    @all_results.setter
    def all_results(self, all_results):
        if is_results_list_valid(all_results):
            self._all_results = all_results

    def get_last_result(self):
        return self._all_results[-1]

    def get_num_of_guesses(self):
        return len(self._all_results)
