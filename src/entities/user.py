class User:
    """Class for user objects"""

    def __init__(self, username, password):
        """Constructor for User class

        Args:
            username (str): Username of the user
            password (str): Password of the user
        """
        self.username = username
        self.password = password
