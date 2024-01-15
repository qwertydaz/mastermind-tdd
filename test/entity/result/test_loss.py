import unittest

from constants.mastermindconstants import MastermindConstants
from src.entity.result.loss import Loss


class LossTest(unittest.TestCase):
    def test_valid_loss(self):
        loss = Loss()
        self.assertEqual(MastermindConstants.MAX_NUM_OF_GUESSES, loss.num_of_guesses)


if __name__ == "__main__":
    unittest.main()
