from tkinter import ttk
import tkinter as tk   
from PIL import Image, ImageTk

import MainMenu as mm
import info as inf

class CaususRhombeatus(tk.Frame):
    
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
            text="Causus rhombeatus - Common Night Adder",
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
            controller.show_frame("BitisGabonica")
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
            #command=lambda:
            #controller.show_frame("BitisGabonica")
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
            text=inf.CaususRhombeatus,
            wraplength=2000,
            justify=tk.LEFT
            )
        lbl1.place(
            x=215,
            y=80
            )

      def showImg(self):
        load = Image.open("pictures/four.jpg")
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
