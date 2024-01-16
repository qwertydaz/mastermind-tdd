from src.model.endresults.endresult import EndResult


class Win(EndResult):
    def __init__(self, num_of_guesses, time_taken):
        super().__init__(num_of_guesses, time_taken)
