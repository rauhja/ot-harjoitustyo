from tkinter import ttk, constants
from services.game_logic import GameLogic
from ui.game_view import GameView


class GameEvents:
    def __init__(self, root, handle_back):
        self._root = root
        self._frame = None
        # self._handle_back = handle_back
        self.game_logic = GameLogic()
        self.game_ui = GameView(root, handle_back)

        self._initialize()

    def _event_handler(self, event):
        if event.keysym == "BackSpace":
            letter_count = self.game_logic.letter_count_remove()
            self.game_ui.handle_backspace(letter_count)
            self.game_logic.remove_letter()

        if "a" <= event.char <= "z":
            letter_count = self.game_logic.letter_count_add()
            self.game_logic.add_letter(event.char)
            self.game_ui.handle_letter(event.char)

    def _initialize(self):
        self._root.bind("<Key>", self._event_handler)
