def _get_word():
    word = "steak"
    return word

def check_word(word, guessnum):
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

def handle_key_press():
    pass

def _initialize():
    guessnum = 1
    gameon = True
    word = _get_word()
    while gameon:
        gameon = check_word(word, guessnum)
        guessnum += 1
    
_initialize()