import unittest

from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES, MAX_TIME_FOR_SCORE_BONUS, TEN_SECONDS, \
    FIVE_GUESSES, LOSING_RESULTS, WINNING_RESULT
from src.model.score import Score
from src.model.results import Results


class ScoreTest(unittest.TestCase):
    score = None
    winning_results = None

    def setUp(self):
        self.score = Score()
        self.winning_results = Results()

    def test_initial_score(self):
        self.assertEqual(0, self.score.points)

    def test_score_after_win_with_valid_guesses_and_10_seconds(self):
        self.winning_results.add_result(WINNING_RESULT)
        self.score.update_score(self.winning_results, TEN_SECONDS)
        self.assertEqual(1500, self.score.points)

        half_of_max_num_of_guesses = int(MAX_NUM_OF_GUESSES / 2)
        self.winning_results.all_results = [[1, 0]] * (half_of_max_num_of_guesses - 1)
        self.winning_results.add_result(WINNING_RESULT)
        self.score.update_score(self.winning_results, TEN_SECONDS)
        self.assertEqual(1100, self.score.points)

        self.winning_results.all_results = [[1, 0]] * (MAX_NUM_OF_GUESSES - 1)
        self.winning_results.add_result(WINNING_RESULT)
        self.score.update_score(self.winning_results, TEN_SECONDS)
        self.assertEqual(600, self.score.points)

    def test_score_after_win_with_5_guesses_and_valid_time_taken(self):
        self.winning_results.all_results = [[1, 0]] * (FIVE_GUESSES - 1)
        self.winning_results.add_result(WINNING_RESULT)

        # 5 guesses and 1 second
        self.score.update_score(self.winning_results, 1.0)
        self.assertEqual(1100, self.score.points)

        # 5 guesses and less than 50% of bonus time
        less_than_50_percent_of_bonus_time = MAX_TIME_FOR_SCORE_BONUS / 2 - 2.0
        self.score.update_score(self.winning_results, less_than_50_percent_of_bonus_time)
        self.assertEqual(850, self.score.points)

        # 5 guesses and exactly 50% of bonus time
        exactly_50_percent_of_bonus_time = MAX_TIME_FOR_SCORE_BONUS / 2
        self.score.update_score(self.winning_results, exactly_50_percent_of_bonus_time)
        self.assertEqual(850, self.score.points)

        # 5 guesses and more than 50% of bonus time
        more_than_50_percent_of_bonus_time = MAX_TIME_FOR_SCORE_BONUS / 2 + 2.0
        self.score.update_score(self.winning_results, more_than_50_percent_of_bonus_time)
        self.assertEqual(725, self.score.points)

        # 5 guesses and exactly on the limit for bonus time
        self.score.update_score(self.winning_results, MAX_TIME_FOR_SCORE_BONUS)
        self.assertEqual(600, self.score.points)

    def test_score_after_win_with_guesses_outside_valid_range(self):
        with self.assertRaises(ValueError):
            self.score.update_score(self.winning_results, TEN_SECONDS)
        with self.assertRaises(ValueError):
            self.winning_results.all_results = [[1, 0]] * MAX_NUM_OF_GUESSES
            self.winning_results.add_result(WINNING_RESULT)  # 1 extra guess than allowed
            self.score.update_score(self.winning_results, TEN_SECONDS)

    def test_score_after_win_with_time_taken_outside_valid_range(self):
        self.winning_results.add_result(WINNING_RESULT)

        with self.assertRaises(ValueError):
            self.score.update_score(self.winning_results, -1.0)
        with self.assertRaises(ValueError):
            self.score.update_score(self.winning_results, 0.0)

    def test_score_after_win_with_results_as_invalid_datatype(self):
        with self.assertRaises(TypeError):
            self.score.update_score("1", TEN_SECONDS)
        with self.assertRaises(TypeError):
            self.score.update_score("helloworld", TEN_SECONDS)
        with self.assertRaises(TypeError):
            self.score.update_score(5.0, TEN_SECONDS)
        with self.assertRaises(TypeError):
            self.score.update_score(True, TEN_SECONDS)
        with self.assertRaises(TypeError):
            self.score.update_score(None, TEN_SECONDS)

    def test_score_after_win_with_time_taken_as_invalid_datatype(self):
        self.winning_results.add_result(WINNING_RESULT)

        with self.assertRaises(TypeError):
            self.score.update_score(self.winning_results, "10.0")
        with self.assertRaises(TypeError):
            self.score.update_score(self.winning_results, 3)
        with self.assertRaises(TypeError):
            self.score.update_score(self.winning_results, None)
        with self.assertRaises(TypeError):
            self.score.update_score(self.winning_results, True)

    def test_score_after_loss(self):
        losing_results = Results()
        for result in LOSING_RESULTS:
            losing_results.add_result(result)

        self.score.update_score(losing_results, TEN_SECONDS)
        self.assertEqual(0, self.score.points)


if __name__ == "__main__":
    unittest.main()
