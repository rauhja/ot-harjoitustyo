from score_db_connection import get_score_db_connection
from entities.score import Score


class ScoreRepository:

    def __init__(self):
        """Constructor that establishes a connection to the database

        """

        self._connection = get_score_db_connection()

    @staticmethod
    def return_user(row):
        """Returns a user object from a row in the database

        Args:
            row (tuple): Row from the database
        """
        return Score(row["username"])

    def create_score(self, user):
        """Creates a new score in the database

        Args:
            user (User): User object to be created in the database

        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO score_database \
            (username, games_played, guessed_words) \
            VALUES (?, ?, ?)", (user.username, user.games_played, user.guessed_words))
        self._connection.commit()
        cursor.close()

    def find_by_username(self, username):
        """Finds a user by username

        Args:
            username (str): Username of the user to be found

        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM score_database WHERE username = ?", [username])
        row = cursor.fetchone()
        if row:
            return ScoreRepository().return_user(row)
        return False

    def update_played_games(self, username):
        """Updates the number of played games

        Args:
            username (str): Username of the user

        """

        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE score_database SET games_played = games_played+1 \
            WHERE username = ?", [username])
        self._connection.commit()
        cursor.close()

    def update_guessed_words(self, username):
        """Updates the number of guessed words

        Args:
            username (str): Username of the user

        """

        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE score_database SET guessed_words = guessed_words+1 \
            WHERE username = ?", [username])
        self._connection.commit()
        cursor.close()

    def get_played_games(self, username):
        """Returns the number of played games

        Args:
            username (str): Username of the user

        Returns:
            int: Number of played games

        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT games_played FROM score_database WHERE username = ?", [username])
        row = cursor.fetchone()
        return row["games_played"]

    def get_guessed_words(self, username):
        """Returns the number of guessed words

        Args:
            username (str): Username of the user

        Returns:
            int: Number of guessed words

        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT guessed_words FROM score_database WHERE username = ?", [username])
        row = cursor.fetchone()
        return row["guessed_words"]

    def delete_data(self):
        """Deletes all data from the database

        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM score_database")
        self._connection.commit()
