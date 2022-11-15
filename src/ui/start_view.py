from tkinter import ttk, constants

class StartView:
    
    def __init__(self, root):
        self._root = root
        self._frame = None
        
        self._initialize()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        play_button = ttk.Button(
            master=self._frame,
            text="Play"
        )
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        
        play_button.grid(padx=5,pady=5, sticky = constants.EW)
