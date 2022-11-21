class GameLogic:
    def __init__(self):
        self.guessnum = 1
        
    def _get_word(self):
        word = "steak"
        return word

    def _check_word(self, word, guessnum):
        if guessnum <= 5:
            print("Guess Word:")
            guess = input("")
            if len(guess) == 5:
                if guess == word:
                    print("Correct!")
                    return False
                else:
                    for i, c in enumerate(guess):
                        if c == word[i]:
                            print("Correct letter!")
                        if c in word and not c == word[i]:
                            print("Correct letter, wrong place")
                        if c not in word:
                            print("Not in a word")
                    return True
            else:
                print("Word too short")
                return True
        else:
            print(f"You lose, correct answer was {word}")
            return False

    def _handle_key_press(self):
        pass

    def _initialize(self):
        gameon = True
        word = self._get_word()
        while gameon:
            gameon = self._check_word(word, self.guessnum)
            self.guessnum += 1
        
