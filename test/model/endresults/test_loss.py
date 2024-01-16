import unittest

from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES, TEN_SECONDS
from src.model.endresults.loss import Loss


class LossTest(unittest.TestCase):
    def test_valid_loss(self):
        loss = Loss(TEN_SECONDS)
        self.assertEqual(MAX_NUM_OF_GUESSES, loss.num_of_guesses)
        self.assertEqual(TEN_SECONDS, loss.time_taken)


if __name__ == "__main__":
    unittest.main()
