class Score:

    def __init__(self, username):
        """Constructor for Score class

        Args:
            username (str): Username of the user
        """

        self.username = username
        self.games_played = 0
        self.guessed_words = 0
