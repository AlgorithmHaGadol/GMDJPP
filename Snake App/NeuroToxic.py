from tkinter import ttk
import tkinter as tk   
from PIL import Image, ImageTk

import MainMenu as mm
import info as inf

class NeuroToxic(tk.Frame):
    
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
            text="Neurotoxic",
            font=mm.TITLE_FONT
            )
        label.pack(
            side="top",
            fill="x",
            )
        prevbtn = ttk.Button(
            self,
            text="<--",
            command=lambda:
            controller.show_frame("CytoToxic")
            )
        homebtn = ttk.Button(
            self,
            text="VenomMenu",
            command=lambda:
            controller.show_frame("VenomBasics")
            )
        nextbtn = ttk.Button(
            self,
            text="-->",
            command=lambda:
            controller.show_frame("MyoToxic")
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
        ttk.Label(
            self,
            text=" ",
            command=self.showImg()
            )
        lbl1 = ttk.Label(
            self,
            text=inf.NeuroToxic,
            wraplength=2000,
            justify=tk.LEFT
            )
        lbl1.place(
            x=260,
            y=80
            )
      def showImg(self):
        load = Image.open("pictures/Neurotoxin.png")
        render = ImageTk.PhotoImage(load)
        img = ttk.Label(
            self,
            image=render
            )
        img.image = render

        img.place(
            x=5,
            y=80
            )
