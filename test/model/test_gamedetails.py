import unittest

from src.constants.mastermindconstants import WINNING_RESULT, TEN_SECONDS, LOSING_RESULTS
from src.model.score import Score
from src.model.results import Results
from src.model.gamedetails import GameDetails
from src.model.player import Player


class GameDetailsTest(unittest.TestCase):
    player = None
    results = None
    score = None

    def setUp(self):
        self.player = Player("game_details_test_player")
        self.results = Results()
        self.score = Score()

    def test_game_details_after_winning_once(self):
        self.results.add_result(WINNING_RESULT)
        self.score.update_score(self.results, TEN_SECONDS)
        game_details = GameDetails(self.player, self.results, self.score)

        self.assertEqual("game_details_test_player", game_details.player.name)
        self.assertEqual([WINNING_RESULT], game_details.results.all_results)
        self.assertEqual(1500, game_details.score.points)

    def test_game_details_after_losing_once(self):
        self.results.add_result(LOSING_RESULTS)
        self.score.update_score(self.results, TEN_SECONDS)
        game_details = GameDetails(self.player, self.results, self.score)

        self.assertEqual("game_details_test_player", game_details.player.name)
        self.assertEqual([LOSING_RESULTS], game_details.results.all_results)
        self.assertEqual(0, game_details.score.points)


if __name__ == "__main__":
    unittest.main()
