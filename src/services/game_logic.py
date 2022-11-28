import tkinter as tk

class GameLogic:
    def __init__(self):
        self.guessnum = 1
        self.letter_count = 0
        self.letters = []
        self.letter_count = 0
        self.guess = ""
        self.guessnum = 1
        self.lower_limit = 0
        self.upper_limit = 5
        self.word = "steak"
        self.green = "#538d4e"
        self.yellow = "#b59f3b"

    def _get_word(self):
        word = "steak"
        return word

    def _check_word(self, guess, guessnum, word):
        if guessnum <= 5:
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

    def create_grid(self):
        for row in range(2,7):
            for col in range(5):        
                box = tk.Button(
                    master=self._frame,
                    text=" ",
                    width=1,
                    bg="white",
                    highlightbackground="white"
                )
                box.grid(row=row, column=col, ipadx=3, ipady=5)
                self.letters.append(box)
    
    # def handle_keypress(self, event):
    #     if event.keysym == "BackSpace":
    #         if self.letter_count > self.lower_limit:
    #             print(self.letter_count)
    #             self.letter_count -= 1
    #             self.letters[self.letter_count]["text"] = " "
    #             self.guess = self.guess[:-1]
    #             print(self.guess)
                
    #     if self.letter_count < self.upper_limit:
    #         if "a" <= event.char <= "z":
    #             self.letters[self.letter_count]["text"] = event.char.upper()
    #             self.letters[self.letter_count].focus()
    #             self.guess = self.guess + event.char
    #             print(self.guess)
    #             self.letter_count += 1
    #             print(self.letter_count)
                
    #     if event.keysym == "Return":
    #         print(self.guess)
    #         if self.letter_count % 5 == 0:
    #             box_idx = self.letter_count - 5
    #             for i, c in enumerate(self.guess):
    #                 if c == self.word[i]:
    #                     self.letters[box_idx+i]["bg"] = self.green
    #                     self.letters[box_idx+i]["highlightbackground"] = self.green
                        
    #                 if c in self.word and not c == self.word[i]:
    #                     self.letters[box_idx+i]["bg"] = self.yellow
    #                     self.letters[box_idx+i]["highlightbackground"] = self.yellow

    #             self.guess = ""
    #             self.lower_limit += 5
    #             self.upper_limit += 5
                
    # def _initialize(self):
    #     word = self._get_word()
