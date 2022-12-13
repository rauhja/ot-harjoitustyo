from db_connection import get_db_connection
from score_db_connection import get_score_db_connection


class CreateDatabase:
    """Class to create the database and tables"""

    def __init__(self):
        """Constructor that establishes a connection to the database

        """

        self._connection = get_db_connection()
        self._score_connection = get_score_db_connection()

    def drop_table(self):
        """Drops the table if it exists

        """

        user_cursor = self._connection.cursor()
        user_cursor.execute("DROP TABLE IF EXISTS user_database")
        self._connection.commit()

        score_cursor = self._score_connection.cursor()
        score_cursor.execute("DROP TABLE IF EXISTS score_database")

    def create_user_database(self):
        """Creates a database and a table for the user information

        """

        cursor = self._connection.cursor()
        cursor.execute("CREATE TABLE user_database \
            (username TEXT PRIMARY KEY NOT NULL, \
            password TEXT NOT NULL \
            )")
        self._connection.commit()
        cursor.close()

    def create_score_database(self):
        """Creates a database and a table for the user game statistics

        """

        cursor = self._score_connection.cursor()
        cursor.execute("CREATE TABLE score_database \
            (username TEXT PRIMARY KEY, \
            games_played INTEGER NOT NULL,\
            guessed_words INTEGER NOT NULL)")
        self._score_connection.commit()
        cursor.close()

    def initialize_database(self):
        """Initializes the database

        """
        self.drop_table()

        self.create_user_database()
        self.create_score_database()


if __name__ == "__main__":
    CreateDatabase().initialize_database()
