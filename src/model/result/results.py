class Results:
    def __init__(self):
        self._all_results = []

    def add_result(self, result):
        self._all_results.append(result)

    @property
    def all_results(self):
        return self._all_results

    def get_last_result(self):
        return self._all_results[-1]
