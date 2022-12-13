from tkinter import Tk
from ui.ui import UI


def main():
    """Function that launches the ui.

    """

    window = Tk()
    window.title("Word Guessing Game")
    window.geometry('260x400+600+100')
    ui_view = UI(window)
    ui_view.start()
    window.mainloop()


if __name__ == "__main__":
    main()
