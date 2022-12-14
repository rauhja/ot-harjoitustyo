from entities.user import User
from db_connection import get_db_connection


class UserRepository:

    def __init__(self):
        """Constructor that establishes a connection to the database

        """

        self._connection = get_db_connection()

    @staticmethod
    def return_user(row):
        """Returns a user object from a row in the database

        Args:
            row (tuple): Row from the database
        """
        return User(row["username"], row["password"])

    def create_user(self, user):
        """Creates a user in the database

        Args:
            user (User): User object to be created in the database
        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO user_database \
            (username, password) VALUES (?, ?)", (user.username, user.password))
        self._connection.commit()
        cursor.close()

    def find_by_username(self, username):
        """Finds a user by username

        Args:
            username (str): Username of the user to be found

        Returns:
            User: User object if found, False if not found
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM user_database WHERE username = ?", [username])
        row = cursor.fetchone()
        if row:
            return UserRepository().return_user(row)
        return False

    def login(self, username, password):
        """Logs in a user

        Args:
            username (str): Username of the user to be logged in
            password (str): Password of the user to be logged in

        Returns:
            User: User object if found, False if not found
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM user_database WHERE (username, password)=(?,?)", (username, password))
        row = cursor.fetchone()
        if row is None:
            return None
        return UserRepository().return_user(row)

    def delete_data(self):
        """Deletes all data from the database

        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM user_database")
        self._connection.commit()
