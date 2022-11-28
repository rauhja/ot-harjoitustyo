from tkinter import ttk

class GameEvents:
    def __init__(self, root):
        self._root = root
        
        self._initialize()
        
    def _initialize(self,event):
        if event.keysym == "BackSpace":
            pass
                