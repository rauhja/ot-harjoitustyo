from tkinter import ttk, constants

class LoginView:
    
    def __init__(self, root):
        self._root = root
        self._frame = None
        
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button = ttk.Button(
            master=self._frame,
            text="Login"
        )
        
        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        # create_user_button.grid(padx=5, pady=5, sticky=constants.EW)