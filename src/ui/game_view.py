from tkinter import ttk, constants

class GameView:
    
    def __init__(self, root, handle_back):
        self._root = root
        self._frame = None
        self._handle_back = handle_back
        
        self._initialize()
        
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _grid_layout(self):
        for row in range(2,7):
            for col in range(5):
                box = ttk.Button(
                    master=self._frame,
                    text=" ",
                    width=1
                )
                box.grid(row=row, column=col, ipadx=3, ipady=5)
        
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