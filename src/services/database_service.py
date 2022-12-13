from repositories.user_repository import UserRepository
from repositories.score_repository import ScoreRepository
from entities.user import User
from entities.score import Score

class UsernameExistError(Exception):
    pass


class UsernameTooShortError(Exception):
    pass


class InvalidPassword(Exception):
    pass


class InvalidLogin(Exception):
    pass


class DatabaseService:
    """Database service class."""

    def __init__(self):
        """Initializes the database service class.

        """
        self._user = None
        self._is_logged = False
        self._user_repository = UserRepository()
        self._score_repository = ScoreRepository()

    @property
    def get_current_user(self):
        """Calling this property returns the current user.

        Returns:
            User: Current user"""

        current_user = self._user
        return current_user

    def __set_current_user(self, user):
        self._user = user

    def _check_password_validity(self, password):
        """Checks if the password is valid.

        """

        if len(password) < 6:
            return False
        if not any(i.isupper() for i in password):
            return False
        if not any(i.isdigit() for i in password):
            return False
        if not any(i.islower() for i in password):
            return False
        return True

    def create_user(self, username, password):
        """Creates a new user with the given username and password.

        Args:
            username (str): Username
            password (str): Password

        Raises:
            UsernameTooShortError: If the username is too short
            UsernameExistError: If the username already exists
            InvalidPassword: If the password is not valid

        """

        if len(username) < 3:
            raise UsernameTooShortError("Username too short")
        if self._user_repository.find_by_username(username=username):
            raise UsernameExistError("Username already exists")
        if self._check_password_validity(password) is False:
            raise InvalidPassword("Password is not valid")

        new_user = User(username, password)
        self._user_repository.create_user(new_user)

    def is_logged_in(self):
        """Checks if the user is logged in.

        Returns:
            bool: True if the user is logged in, False otherwise

        """

        logged_in = self._is_logged
        return logged_in

    def create_score(self, username):
        """Creates a scoretable for the given user.

        Args:
            username (str): Username
        """

        new_score = Score(username)
        self._score_repository.create_score(new_score)

    def update_games_played(self):
        """Updates the number of games played by the current user.

        """

        self._score_repository.update_played_games(self._user.username)

    def update_guessed_words(self):
        """Updates the number of guessed words by the current user.

        """

        self._score_repository.update_guessed_words(self._user.username)

    def get_guessed_words(self):
        """Gets the number of guessed words by the current user.

        Returns:
            int: Number of guessed words
        """

        guessed_words = self._score_repository.get_guessed_words(
            self._user.username)
        return guessed_words

    def get_games_played(self):
        """Gets the number of games played by the current user.

        Returns:
            int: Number of games played
        """

        played_games = self._score_repository.get_played_games(
            self._user.username)
        return played_games

    def login(self, username, password):
        """Logs in the user with the given username and password.

        Args:
            username (str): Username
            password (str): Password

        Raises:
            InvalidLogin: If the username or password is incorrect

        Returns:
            User: The logged in user
        """

        user = UserRepository().login(username, password)
        if not user:
            raise InvalidLogin("Username or password is incorrect")
        self.__set_current_user(user)
        self._is_logged = True
        return self._user

    def logout(self):
        """Logs out the current user.

        """

        self.__set_current_user(None)
        self._is_logged = False
