from tkinter import ttk, constants, StringVar
from sqlite3 import OperationalError
from services.database_service import InvalidLogin


class LoginView:
    """Class for the login view

    """

    def __init__(self, root, handle_back, db_services, handle_logged_in_view):
        """Constructor for the login view

        Args:
            root (tk.Tk): The root of the application. Created in index.py.
            handle_back (function): Function to handle the back button.
            db_services (DatabaseService): Database service.
            handle_logged_in_view (function): Function to handle the logged in view.

        """
        self._root = root
        self._frame = None
        self._handle_back = handle_back
        self._handle_logged_in_view = handle_logged_in_view
        self._db_services = db_services
        self._username_entry = StringVar()
        self._password_entry = StringVar()
        self._error_variable = StringVar()
        self._initialize()

    def pack(self):
        """Pack the view"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy the view"""
        self._frame.destroy()

    def _handle_login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        try:
            self._db_services.login(username=username, password=password)
            self._handle_logged_in_view()
        except InvalidLogin:
            self._error_variable.set("Invalid username or password")
            self._error_label.grid()
        except OperationalError:
            self._error_variable.set(
                "Please run build -task before\n running the program")
            self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        """Initializes the login view

        """

        self._frame = ttk.Frame(master=self._root)
        header = ttk.Label(master=self._frame, text="Login")
        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(
            master=self._frame, textvariable=self._username_entry)
        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(
            master=self._frame, textvariable=self._password_entry)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_variable, foreground="red")

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._handle_login
        )

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )

        self._frame.grid_columnconfigure(0, weight=1)
        header.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        self._error_label.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
        username_label.grid(row=2, column=0, padx=0,
                            pady=5, sticky=(constants.EW))
        username_entry.grid(row=2, column=1, padx=0, pady=5)
        password_label.grid(row=3, column=0, padx=0,
                            pady=5, sticky=(constants.EW))
        password_entry.grid(row=3, column=1, padx=0, pady=5)
        login_button.grid(row=4, padx=5, pady=5, columnspan=2)
        back_button.grid(row=5, padx=5, pady=5, columnspan=2)
        self._hide_error()
