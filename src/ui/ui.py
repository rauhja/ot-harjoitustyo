from ui.start_view import StartView
from ui.game_view import GameView
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.logged_view import LoggedInView
from services.game_events import GameEvents
from services.database_service import DatabaseService


class UI:
    """Class controlling the UI

    """

    def __init__(self, root):
        """Initializes the UI class.

        Args:
            root (tk.Tk): The root of the application. Created in index.py.

        """

        self._root = root
        self._current_view = None
        self._db_service = DatabaseService()

    def start(self):
        """Function that starts the UI.

        """

        self._show_start_view()

    def _hide_current_view(self):
        """Function that hides the current view.

        """

        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _handle_play(self):
        self._show_game_view()

    def _handle_play_logged_in(self):
        self._db_service.update_games_played()
        self._show_game_view()

    def _handle_back(self):
        if self._db_service.is_logged_in():
            self._show_logged_in_view()
        else:
            self._show_start_view()

    def _handle_back_logged(self):
        self._show_logged_in_view()

    def _handle_show_login_view(self):
        self._show_login_view()

    def _handle_show_create_user_view(self):
        self._show_create_user_view()

    def _handle_show_logged_in_view(self):
        self._show_logged_in_view()

    def _handle_logout(self):
        self._show_start_view()
        self._db_service.logout()

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._handle_play,
            self._handle_show_login_view,
            self._handle_show_create_user_view
        )
        self._current_view.pack()

    def _show_game_view(self):
        self._hide_current_view()

        self._current_view = GameView(
            self._root,
            self._handle_back
        )
        GameEvents(self._root, self._current_view, self._db_service)

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_back,
            self._db_service,
            self._handle_show_logged_in_view
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._handle_back,
            self._handle_show_login_view,
            self._db_service
        )
        self._current_view.pack()

    def _show_logged_in_view(self):
        self._hide_current_view()

        self._current_view = LoggedInView(
            self._root,
            self._handle_play_logged_in,
            self._handle_logout,
            self._db_service
        )
        self._current_view.pack()
