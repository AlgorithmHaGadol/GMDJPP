from tkinter import *

root = Tk()

volume = LabelFrame(root, text="Volume", padx=5, pady=5)
volume.pack(padx=10, pady=10)

volCyl = Button(volume, text="vol_cyl()")
volCyl.pack()
volSph = Button(volume, text="vol_Sph()")
volSph.pack()

mainloop()
