from tkinter import ttk, constants, StringVar
import tkinter as tk

green = "#538d4e"
yellow = "#b59f3b"


class GameView:
    """Class for the game view"""

    def __init__(self, root, handle_back):
        """Constructor for the game view

        Args:
            root (tk.Tk): The root of the application. Created in index.py.
            handle_back (function): Function to handle the back button.
        """

        self._root = root
        self._frame = None
        self._handle_back = handle_back
        self.boxes = []
        self._winloselbl = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _grid_layout(self):
        for row in range(2, 7):
            for col in range(5):
                box = tk.Button(
                    master=self._frame,
                    text=" ",
                    width=1,
                    bg="white",
                    highlightbackground="white"
                )
                box.grid(row=row, column=col, ipadx=3, ipady=5)
                self.boxes.append(box)

    def handle_backspace(self, letter_count, lower_limit):
        """Function that handles the backspace button

        Args:
            letter_count (int): The current letter count.
            lower_limit (int): The lower limit of the letter count.
        """

        if letter_count >= lower_limit:
            self.boxes[letter_count]["text"] = " "

    def handle_letter(self, char, letter_count, upper_limit):
        """Function that handles the letter button

        Args:
            char (str): The letter to be displayed.
            letter_count (int): The current letter count.
            upper_limit (int): The upper limit of the letter count.
        """

        if letter_count < upper_limit:
            self.boxes[letter_count]["text"] = char.upper()

    def handle_enter(self, check, letter_count):
        """Function that handles the enter button

        Args:
            check (list): The list of the check colors.
            letter_count (int): The current letter count.

        """

        box_id = letter_count - 5
        for i, color in enumerate(check):
            if color == 1:
                self.boxes[box_id+i]["bg"] = green
                self.boxes[box_id+i]["highlightbackground"] = green
            if color == 2:
                self.boxes[box_id+i]["bg"] = yellow
                self.boxes[box_id+i]["highlightbackground"] = yellow

    def handle_winlose(self, winlose, answer):
        """Function that handles the win/lose message

        Args:
            winlose (str): The result of the game.
            answer (str): The correct word.

        """

        if winlose == "win":
            self._winloselbl.set(f"You've guessed it!")

        if winlose == "lose":
            self._winloselbl.set(f"Correct word was: {answer}")

    def _initialize(self):
        """Function that initializes the game view

        """

        self._frame = ttk.Frame(master=self._root)
        header = ttk.Label(master=self._frame, text="Guess Word")
        self._winloselbl = StringVar()
        self._winloselbl.set("")
        winlosetxt = ttk.Label(
            master=self._frame, textvariable=self._winloselbl)
        help_label = ttk.Label(master=self._frame,
                               text="Press Enter to check word\nPress backspace to delete a letter\n\nYellow: Correct letter, wrong position\nGreen: Correct letter, correct position")

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )

        self._frame.grid_columnconfigure(0)
        self._grid_layout()
        header.grid(row=0, column=0, columnspan=5, pady=5)
        winlosetxt.grid(row=8, column=0, columnspan=5, pady=10)
        back_button.grid(row=9, column=0, columnspan=5)
        help_label.grid(row=10, column=0, columnspan=5, pady=10, padx=5)
