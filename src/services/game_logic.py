import random


class GameLogic:
    """Game logic for the game.

    """

    def __init__(self):
        """Initializes the GameLogic class.
        """
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
        """Gets a random word from the file.

        """
        with open(self.data, "r", encoding='utf-8') as file:
            all = file.read()
            words = list(map(str, all.split()))
            word = random.choice(words)
            file.close()
            return word

    def _increase_guess_num(self):
        """Increases the guess number.

        """
        self.guess_num += 1

    def increase_letter_count(self):
        """Increases the letter count.

        """
        self.letter_count += 1

    def decrease_letter_count(self):
        """Decreases the letter count.

        """
        if self.letter_count > 0:
            self.letter_count -= 1

    def increase_lower_limit(self):
        """Increases the lower limit of letters.

        """
        self.lower_limit += 5

    def increase_upper_limit(self):
        """Increases the upper limit of letters.

        """
        self.upper_limit += 5

    def decrease_upper_limit(self):
        """Decreases the upper limit of letters.

        """
        self.upper_limit -= 5

    def add_letter(self, char):
        """Adds a letter to the guess.

        Args:
            char (str): The letter to add.
        """

        self.guess = self.guess + char

    def remove_letter(self):
        """Removes the last letter from the guess.

        """

        self.guess = self.guess[:-1]

    def win_lose(self, db_service):
        """Checks if the player has won or lost.

        Args:
            db_service (DatabaseService): The database service.

        Returns:
            str: The result of the game.
        """

        if self.is_winner:
            if db_service.is_logged_in():
                db_service.update_guessed_words()
                return "win"
            return "win"
        if self.guess_num > 5 and not self.is_winner:
            return "lose"
        return None

    def check_word(self):
        """Checks the guess against the word.

        Returns:
            list: A list of 0, 1, 2. 0 is no color, 1 is green, 2 is yellow.
        """

        check = []
        if self.guess_num <= 5:
            if self.guess == self.word:
                self.is_winner = True
                self.decrease_upper_limit()
            for i, char in enumerate(self.guess):
                if char == self.word[i]:
                    check.append(1)
                if char in self.word and not char == self.word[i]:
                    check.append(2)
                if char not in self.word:
                    check.append(0)
            self.guess = ""
            self._increase_guess_num()
            return check
        return [0, 0, 0, 0, 0]

    def _initialize(self):
        self.word = self._get_word()
