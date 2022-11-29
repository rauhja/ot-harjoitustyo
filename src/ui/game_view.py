from tkinter import ttk, constants
import tkinter as tk
from services.game_logic import GameLogic

green = "#538d4e"
yellow = "#b59f3b"

class GameView:
    
    def __init__(self, root, handle_back):
        self._root = root
        self._frame = None
        self._handle_back = handle_back
        self.boxes = []
        self.guess = ""
        self.guessnum = 1
        self.lower_limit = 0
        self.upper_limit = 5
        self.letter_count = 0
        
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
    
    def handle_backspace(self, letter_count):
        if letter_count > self.lower_limit:
            self.boxes[letter_count]["text"] = " "
    
    def handle_letter(self, char):
        if self.letter_count < self.upper_limit:
            
            self.boxes[self.letter_count]["text"] = char
            # self.boxes[self.letter_count].focus()
                
    # def _handle_key_press(self, event):

        # if event.keysym == "BackSpace":
        #     if self.letter_count > self.lower_limit:
        #         # print(self.letter_count)
        #         self.letter_count -= 1
        #         self.boxes[self.letter_count]["text"] = " "
        #         self.guess = self.guess[:-1]
        #         print(self.guess)
                
        # if self.letter_count < self.upper_limit:
        #     if "a" <= event.char <= "z":
        #         self.boxes[self.letter_count]["text"] = event.char.upper()
        #         self.boxes[self.letter_count].focus()
        #         self.guess = self.guess + event.char
        #         print(self.guess)
        #         self.letter_count += 1
        #         print(self.letter_count)
                
                    
        # if event.keysym == "Return":
        #     print(self.guess)
        #     if self.letter_count % 5 == 0:
        #         box_idx = self.letter_count - 5
        #         for i, c in enumerate(self.guess):
        #             if c == word[i]:
        #                 self.boxes[box_idx+i]["bg"] = green
        #                 self.boxes[box_idx+i]["highlightbackground"] = green
                        
        #             if c in word and not c == word[i]:
        #                 self.boxes[box_idx+i]["bg"] = yellow
        #                 self.boxes[box_idx+i]["highlightbackground"] = yellow
        #             # if c not in word:
        #             #     print("Not in a word")
        #         self.guess = ""
        #         self.lower_limit += 5
        #         self.upper_limit += 5
                
                
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Guess Word")
        
        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )
        
        self._frame.grid_columnconfigure(0)
        self._grid_layout()
        label.grid(row=0, column=0, columnspan=5)
        back_button.grid(row=8, column=0, columnspan=5)
        # self._root.bind("<Key>", self._handle_key_press)