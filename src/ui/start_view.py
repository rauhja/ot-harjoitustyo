from tkinter import ttk, constants


class StartView:
    """Class for the start view

    """

    def __init__(self, root, handle_play, handle_show_login_view, handle_show_create_user_view):
        """Constructor for the start view

        Args:
            root (tk.Tk): The root of the application. Created in index.py.
            handle_play (function): Function to handle the play button.
            handle_show_login_view (function): Function to handle the login button.
            handle_show_create_user_view (function): Function to handle the create user button.

        """

        self._root = root
        self._frame = None
        self._handle_play = handle_play
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_create_user_view = handle_show_create_user_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        """Initializes the start view
        
        """

        self._frame = ttk.Frame(master=self._root)
        header = ttk.Label(master=self._frame, text="WORD GUESSING GAME")

        play_button = ttk.Button(
            master=self._frame,
            text="Play",
            command=self._handle_play
        )

        signin_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._handle_show_login_view
        )

        signup_button = ttk.Button(
            master=self._frame,
            text="Sign Up",
            command=self._handle_show_create_user_view
        )

        self._frame.grid_columnconfigure(0, weight=1)

        header.grid(row=0, column=0)
        play_button.grid(padx=5, pady=5)
        signin_button.grid(padx=5, pady=5)
        signup_button.grid(padx=5, pady=5)
