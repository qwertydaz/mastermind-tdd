import unittest

from entity.score import Score


class ScoreTest(unittest.TestCase):
    score = None

    def setUp(self):
        self.score = Score()

    def test_initial_score(self):
        self.assertEqual(0, self.score.current_score)

    def test_score_after_first_win(self):
        self.score.update_score(1)
        self.assertEqual(1000, self.score.current_score)


if __name__ == "__main__":
    unittest.main()
