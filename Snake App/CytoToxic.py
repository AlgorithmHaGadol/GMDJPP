from tkinter import ttk
import tkinter as tk   

import MainMenu as mm
import info as inf

class CytoToxic(tk.Frame):
    
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
            text="Cytotoxic",
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
            controller.show_frame("HaemoToxic")
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
            controller.show_frame("NeuroToxic")
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
            text=inf.CytoToxic,
            wraplength=2000,
            justify=tk.LEFT
            )
        lbl1.place(
            x=10,
            y=80
            )
