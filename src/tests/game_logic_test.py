import unittest
from services.game_logic import GameLogic

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()
        self.word = "steak"
    
    def test_get_word(self):
        self.assertTrue(self.game._get_word)
    
    def test_increase_guess_num(self):
        self.assertEqual(self.game.guess_num, 1)
        
        self.game._increase_guess_num()
        self.assertEqual(self.game.guess_num, 2)
    
    def test_increase_letter_count(self):
        self.assertEqual(self.game.letter_count, 0)
        self.game.increase_letter_count()
        self.assertEqual(self.game.letter_count, 1)
    
    def test_decrease_letter_count(self):
        self.game.letter_count = 1
        self.game.decrease_letter_count()
        self.assertEqual(self.game.letter_count, 0)
        self.game.decrease_letter_count()
        self.assertEqual(self.game.letter_count, 0)
        
    def test_increase_lower_limit(self):
        self.game.increase_lower_limit()
        self.assertEqual(self.game.lower_limit, 5)

    def test_increase_upper_limit(self):
        self.game.increase_upper_limit()
        self.assertEqual(self.game.upper_limit, 10)
    
    def test_decrease_upper_limit(self):
        self.game.upper_limit = 10
        self.game.decrease_upper_limit()
        self.assertEqual(self.game.upper_limit, 5)
    
    def test_add_letter(self):
        char = "a"
        self.game.add_letter(char)
        self.assertEqual(self.game.guess, "a")
    
    def test_remove_letter(self):
        self.game.guess = "test"
        self.game.remove_letter()
        self.assertEqual(self.game.guess, "tes")
    
    def test_win_lose(self):
        check = self.game.win_lose()
        self.assertEqual(check, None)
        
        self.game.is_winner = True
        check = self.game.win_lose()
        self.assertEqual(check, "win")
        
        self.game.is_winner = False
        self.game.guess_num = 6
        check = self.game.win_lose()
        self.assertEqual(check, "lose")
    
    def test_check_word(self):
        self.game.word = "apple"
        self.game.guess = "apple"
        self.game.check_word()
        
        self.assertTrue(self.game.is_winner)
        self.assertEqual(self.game.upper_limit, 0)
        
        self.game.guess = "maple"
        check = self.game.check_word()
        self.assertEqual(check, [0,2,1,1,1])
        
        self.game.guess_num = 6
        check = self.game.check_word()
        self.assertEqual(check, [0,0,0,0,0])