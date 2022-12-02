from tkinter import ttk, constants, StringVar
import tkinter as tk

green = "#538d4e"
yellow = "#b59f3b"

class GameView:

    def __init__(self, root, handle_back):
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
        for row in range(2,7):
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
        if letter_count >= lower_limit:
            self.boxes[letter_count]["text"] = " "
    
    def handle_letter(self, char, letter_count, upper_limit):
        if letter_count < upper_limit:
            self.boxes[letter_count]["text"] = char.upper()
    
    def handle_enter(self, check, letter_count):
        box_id = letter_count - 5
        for i, color in enumerate(check):
            if color == 1:
                self.boxes[box_id+i]["bg"] = green
                self.boxes[box_id+i]["highlightbackground"] = green
            if color == 2:
                self.boxes[box_id+i]["bg"] = yellow
                self.boxes[box_id+i]["highlightbackground"] = yellow
    
    def handle_winlose(self, winlose, answer):
        if winlose == "win":
            self._winloselbl.set(f"You've guessed it!")
            
        if winlose == "lose": 
            self._winloselbl.set(f"Correct word was: {answer}")
                
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Guess Word")
        self._winloselbl = StringVar()
        self._winloselbl.set("")
        winlosetxt = ttk.Label(master=self._frame, textvariable=self._winloselbl)
        
        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )
        
        self._frame.grid_columnconfigure(0)
        self._grid_layout()
        label.grid(row=0, column=0, columnspan=5)
        winlosetxt.grid(row=8, column=0, columnspan=5, pady=10)
        back_button.grid(row=9, column=0, columnspan=5)