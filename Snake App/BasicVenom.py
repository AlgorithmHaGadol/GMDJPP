from tkinter import ttk
import tkinter as tk   
from PIL import Image, ImageTk

import MainMenu as mm
import info as inf

basicvenom = """
      Cytotoxins - cause local tissue damage.
      Hemotoxins - cause internal bleeding.
      Neurotoxins - affect the nervous system.
      Cardiotoxins - act directly on the heart.

A snake can have a number of venom types, and will require comprehensive treatment to address each clinical issue as it presents.
Note – there is a small, but significant risk of getting antivenin to treat venomous snakebite. When a bite victim is allergic to the antivenin,
shock and death can result. Please ensure the following:
1.    Do not get treated with antivenin before you have any symptoms of envenomation,
      even if you know the exact species of snake that bit you. Dry bites (without venom injection) occurs during about 30-50% of all bites.
2.    If you will be treated with antivenin, insist on a very small dose to test whether you are allergic to it,
      before the full quantity is administered. Much safer this way!

"""

class VenomBasics(tk.Frame):
    
      def __init__(
        self,
        parent,
        controller
        ):
        tk.Frame.__init__(
            self,
            parent
            )
        self.controller = controller

        label = tk.Label(
            self,
            text="Venom Basic Description",
            font=mm.TITLE_FONT
            )
        label.pack(
            side="top",
            fill="x",
            )
        prevbtn = ttk.Button(
            self,
            text="<--",
            #command=lambda:
            #controller.show_frame("BitisAtropas")
            )
        homebtn = ttk.Button(
            self,
            text="HomePage",
            command=lambda:
            controller.show_frame("MainMenu")
            )
        nextbtn = ttk.Button(
            self,
            text="-->",
            command=lambda:
            controller.show_frame("HaemoToxic")
            )
        prevbtn.place(
            x=10,
            y=50
            )
        homebtn.place(
            x=85,
            y=50
            )
        nextbtn.place(
            x=160,
            y=50
            )
        lbl1 = ttk.Label(
            self,
            text=basicvenom,
            wraplength=2000,
            justify=tk.LEFT
            )
        lbl1.place(
            x=10,
            y=80
            )
