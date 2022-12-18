from tkinter import ttk, constants, StringVar


class LoggedInView:
    """Class for the logged in view

    """

    def __init__(self, root, handle_play, handle_logout, db_services):
        """Constructor for the logged in view

        Args:
            root (tk.Tk): The root of the application. Created in index.py.
            handle_play (function): Function to handle the play button.
            handle_logout (function): Function to handle the logout button.
            db_services (DatabaseService): Database service.
        """

        self._root = root
        self._frame = None
        self._handle_play = handle_play
        self._handle_logout = handle_logout
        self._db_services = db_services
        self._num_guessed_words = StringVar()
        self._num_games_played = StringVar()
        self._num_games = 0
        self._num_words = 0

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_stats(self):
        """Function that get the stats"""
        self._num_games = self._db_services.get_games_played()
        self._num_words = self._db_services.get_guessed_words()

    def _initialize(self):
        """Initializes the logged in view

        """
        self._frame = ttk.Frame(master=self._root)
        self._handle_stats()
        header = ttk.Label(master=self._frame, text="WORD GUESSING GAME")
        guessed_words = ttk.Label(
            master=self._frame, text=f"Guessed Words: {self._num_words}")
        games_played = ttk.Label(
            master=self._frame, text=f"Games Played: {self._num_games}")
        num_guessed_words = ttk.Label(
            master=self._frame, textvariable=self._num_guessed_words)
        num_games_played = ttk.Label(
            master=self._frame, textvariable=self._num_games_played)

        play_button = ttk.Button(
            master=self._frame,
            text="Play",
            command=self._handle_play
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Log Out",
            command=self._handle_logout
        )

        self._frame.grid_columnconfigure(0, weight=1)

        header.grid(row=0, column=0, columnspan=2)
        play_button.grid(row=1, padx=5, pady=5, columnspan=2)
        logout_button.grid(row=2, padx=5, pady=5, columnspan=2)
        guessed_words.grid(row=3, column=0)
        num_guessed_words.grid(row=3, column=1)
        games_played.grid(row=4, column=0)
        num_games_played.grid(row=4, column=1)
