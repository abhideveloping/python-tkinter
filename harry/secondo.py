from tkinter import *

imaginary_tech_root = Tk()

#Width X Height
imaginary_tech_root.geometry("444x234")


#width, height
#defines the minimum size of the window.
imaginary_tech_root.minsize(200, 100)

#width, height
#define the max size of the window.. can't make the size bigger than this
imaginary_tech_root.maxsize(500, 400)

shakib = Label(text="Shakib is a good boy and this is his GUI")
shakib.pack()

#need to pack the shakib thing in order to see this in window.

imaginary_tech_root.mainloop()