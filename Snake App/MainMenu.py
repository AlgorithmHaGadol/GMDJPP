from tkinter import ttk
import tkinter as tk

from info import *
#from dropmenu import *

from BasicVenom import *
from HaemoToxic import *
from CytoToxic import *
from NeuroToxic import *
from MyoToxic import *

from BitisArietans import *
from BitisAtropas import *
from BitisGabonica import *
from CaususRhombeatus import *

TITLE_FONT = (
    "Jokerman",
    18,
    "bold",
    "underline",
    "italic"
    )

class SnakeApp(tk.Tk):

    def __init__(
        self,
        *args,
        **kwargs
        ):
        tk.Tk.__init__(
            self,
            *args,
            **kwargs
            )

        tk.Tk.iconbitmap(
           self,
           default="icon.ico"
           )

        container = tk.Frame(self)
        container.pack(
            side="top",
            fill="both",
            expand=True
            )
        container.grid_rowconfigure(
            0,
            weight=1
            )
        container.grid_columnconfigure(
            0,
            weight=1
            )

        self.frames = {}
        for F in (
            MainMenu,
           # DropMenu,
            BitisArietans,
            BitisAtropas,
            BitisGabonica,
            CaususRhombeatus,
            VenomBasics,
            HaemoToxic,
            CytoToxic,
            NeuroToxic,
            MyoToxic
            ):
            page_name = F.__name__

            frame = F(
                parent=container,
                controller = self
                )
            self.frames[page_name] = frame

            frame.grid(
                row=0,
                column=0,
                sticky="nsew"
                )

        self.show_frame("MainMenu")

    def show_frame(
        self,
        page_name
        ):
        frame = self.frames[
            page_name
            ]
        frame.tkraise()

class MainMenu(tk.Frame):

    def __init__(
        self,
        parent,
        controller
        ):
        tk.Frame.__init__(
            self,
            parent
            )

if __name__ == "__main__":
    
    app=SnakeApp()
    app.title("SnakeApp | Coded by : ALGORITHM")
    app.geometry("1000x600")
    app.mainloop()
