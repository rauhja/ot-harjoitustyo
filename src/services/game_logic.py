import random

class GameLogic:

    def __init__(self):
        self.letter_count = 0
        self.guess = ""
        self.guess_num = 1
        self.lower_limit = 0
        self.upper_limit = 5
        self.word = ""
        self.is_winner = False
        self.data = "./src/five.txt"

        self._initialize()

    def _get_word(self):
        with open(self.data, "r", encoding = 'utf-8') as file:
            all = file.read()
            words = list(map(str, all.split()))
            word = random.choice(words)
            file.close()
            return word

    def _increase_guess_num(self):
        self.guess_num += 1

    def increase_letter_count(self):
        self.letter_count += 1

    def decrease_letter_count(self):
        if self.letter_count > 0:
            self.letter_count -= 1

    def increase_lower_limit(self):
        self.lower_limit += 5

    def increase_upper_limit(self):
        self.upper_limit += 5

    def decrease_upper_limit(self):
        self.upper_limit -= 5

    def add_letter(self, char):
        self.guess = self.guess + char

    def remove_letter(self):
        self.guess = self.guess[:-1]

    def win_lose(self):
        if self.is_winner:
            return "win"
        if self.guess_num > 5 and not self.is_winner:
            return "lose"
        return None

    def check_word(self):
        check = []
        if self.guess_num <= 5:
            if self.guess == self.word:
                self.is_winner = True
                self.decrease_upper_limit()
            for i, char in enumerate(self.guess):
                if char == self.word[i]:
                    # 1 is green
                    check.append(1)
                if char in self.word and not char == self.word[i]:
                    # 2 is yellow
                    check.append(2)
                if char not in self.word:
                    check.append(0)
            self.guess = ""
            self._increase_guess_num()
            return check
        return [0,0,0,0,0]

    def _initialize(self):
        self.word = self._get_word()
