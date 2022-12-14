from services.game_logic import GameLogic


class GameEvents:
    """Class for handling events in the game.

    """

    def __init__(self, root, view, db_service):
        """Constructor for the game events class.

        Args:
            root (tk.Tk): The root of the application. Created in index.py.
            view (GameView): The game view.
            db_service (DatabaseService): Database service.
        """

        self._root = root
        self._frame = None
        self.game_logic = GameLogic()
        self.game_ui = view
        self._db_services = db_service

        self._initialize()

    def _event_handler(self, event):
        """Function that handles the events.

        Args:
            event (tk.Event): The event from the keyboard.

        """

        if "a" <= event.char <= "z":
            if self.game_logic.letter_count < self.game_logic.upper_limit \
                and self.game_logic.guess_num < 6:
                self.game_logic.add_letter(event.char)
                self.game_ui.handle_letter(event.char,
                                           self.game_logic.letter_count,
                                           self.game_logic.upper_limit
                                           )
                self.game_logic.increase_letter_count()

        if event.keysym == "BackSpace":
            if self.game_logic.letter_count > self.game_logic.lower_limit:
                self.game_logic.decrease_letter_count()
                self.game_ui.handle_backspace(self.game_logic.letter_count,
                                              self.game_logic.lower_limit
                                              )
                self.game_logic.remove_letter()

        if event.keysym == "Return":
            if self.game_logic.letter_count == self.game_logic.upper_limit:
                check = self.game_logic.check_word()
                self.game_ui.handle_enter(check, self.game_logic.letter_count)
                win_lose = self.game_logic.win_lose(self._db_services)
                self.game_ui.handle_winlose(win_lose, self.game_logic.word)
                self.game_logic.increase_lower_limit()
                self.game_logic.increase_upper_limit()

    def _initialize(self):
        self._root.bind("<Key>", self._event_handler)
