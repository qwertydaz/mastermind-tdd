import unittest

from entity.player import Player


class PlayerTest(unittest.TestCase):
    player = None

    @classmethod
    def setUpClass(cls):
        cls.player = Player()

    def test_default_player_name(self):
        self.assertEqual("Player", self.player.name)


if __name__ == '__main__':
    unittest.main()
