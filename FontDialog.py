import tkinter
from tkinter import simpledialog
from tkinter import Frame
from tkinter import ttk
from tkinter import font

from main import Main


class FontDialog(tkinter.simpledialog.Dialog):
    def __init__(self, master, main: Main, title=None) -> None:
        self.main = main
        super(FontDialog, self).__init__(parent=master, title=title)

    def body(self, master) -> None:
        frame_1 = Frame(master)
        frame_1.pack(side="left", fill="both", expand=True)
        fonts = font.families()
        global combo
        combo = ttk.Combobox(frame_1, values=fonts)
        combo.pack(side="left", fill="x", expand=True)

    def apply(self) -> None:
        self.main.entry.configure(font=(combo.get(), 16))