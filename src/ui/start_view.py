from tkinter import ttk, constants

class StartView:
    
    def __init__(self, root, handle_play):
        self._root = root
        self._frame = None
        self._handle_play = handle_play
        
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="WORD GUESSING GAME")
        
        play_button = ttk.Button(
            master=self._frame,
            text="Play",
            command=self._handle_play
        )
        
        signin_button = ttk.Button(
            master=self._frame,
            text="Sign In"
        )
        
        signup_button = ttk.Button(
            master=self._frame,
            text="Sing Up"
        )
        
        self._frame.grid_columnconfigure(0, weight=1)
        
        label.grid(row=0,column=0)
        play_button.grid(padx=5, pady=5)
        signin_button.grid(padx=5, pady=5)
        signup_button.grid(padx=5, pady=5)
