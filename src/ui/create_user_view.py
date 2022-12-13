from tkinter import ttk, constants, StringVar
from services.database_service import UsernameExistError, UsernameTooShortError, InvalidPassword
from sqlite3 import OperationalError


class CreateUserView:
    """Class for the create user view"""

    def __init__(self, root, handle_back, handle_login, db_services):
        """Constructor for the create user view

        Args:
            root (tk.Tk): The root of the application. Created in index.py.
            handle_back (function): Function to handle the back button.
            handle_login (function): Function to handle the login button.
            db_services (DatabaseService): Database service.
        """

        self._root = root
        self._frame = None
        self._handle_back = handle_back
        self._handle_login = handle_login
        self._username_entry = StringVar()
        self._password_entry = StringVar()
        self._error_variable = StringVar()
        self._user_created = StringVar()
        self._db_services = db_services
        self._initialize()

    def pack(self):
        """Pack the view

        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy the view

        """
        self._frame.destroy()

    def _handle_create_user(self):
        """Function that handles the create user button

        """

        username = self._username_entry.get()
        password = self._password_entry.get()
        try:
            self._db_services.create_user(username=username, password=password)
            self._db_services.create_score(username=username)
            self._user_created.set("User created")
            self._user_created_label.grid()
        except UsernameExistError:
            self._error_variable.set("Username already exists")
            self._error_label.grid()
        except OperationalError:
            self._error_variable.set("Database error")
            self._error_label.grid()
        except UsernameTooShortError:
            self._error_variable.set(
                "Username too short, minimum 3 characters")
            self._error_label.grid()
        except InvalidPassword:
            self._error_variable.set(
                "Password should be over 8 characters,\n include at least one number, uppercase and lowercase letter")
            self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _hide_label(self):
        self._user_created_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header = ttk.Label(master=self._frame, text="Create User")
        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(
            master=self._frame, textvariable=self._username_entry)
        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(
            master=self._frame, textvariable=self._password_entry)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_variable, foreground="red")
        self._user_created_label = ttk.Label(
            master=self._frame, textvariable=self._user_created, foreground="green")

        create_user_button = ttk.Button(
            master=self._frame,
            text="Sign Up",
            command=self._handle_create_user
        )

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )

        self._frame.grid_columnconfigure(0, weight=1)

        header.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        self._error_label.grid(row=1, padx=5, pady=5, columnspan=2)
        self._user_created_label.grid(row=1, padx=5, pady=5, columnspan=2)
        username_label.grid(row=2, column=0, padx=0,
                            pady=5, sticky=(constants.EW))
        username_entry.grid(row=2, column=1, padx=0, pady=5)
        password_label.grid(row=3, column=0, padx=0,
                            pady=5, sticky=(constants.EW))
        password_entry.grid(row=3, column=1, padx=0, pady=5)
        create_user_button.grid(row=4, padx=5, pady=5, columnspan=2)
        back_button.grid(row=5, padx=5, pady=5, columnspan=2)
        self._hide_error()
        self._hide_label()
