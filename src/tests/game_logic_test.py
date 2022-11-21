import unittest
from game_logic import GameLogic

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()
        self.word = "steak"
    
    def test_get_word(self):
        self.assertTrue(self.game._get_word)
    
    def test_guessnum_over_five(self):
        self.guessnum = 6
        self.assertFalse(self.game._check_word(self.word, self.guessnum))