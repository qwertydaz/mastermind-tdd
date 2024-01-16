import unittest

from src.constants.mastermindconstants import MAX_NUM_OF_GUESSES
from src.model.result.loss import Loss


class LossTest(unittest.TestCase):
    def test_valid_loss(self):
        loss = Loss(10.0)
        self.assertEqual(MAX_NUM_OF_GUESSES, loss.num_of_guesses)
        self.assertEqual(10.0, loss.time_taken)


if __name__ == "__main__":
    unittest.main()
