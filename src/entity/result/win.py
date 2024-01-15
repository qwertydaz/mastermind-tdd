from src.entity.result.endresult import EndResult


class Win(EndResult):
    def __init__(self, num_of_guesses):
        super().__init__(num_of_guesses)
