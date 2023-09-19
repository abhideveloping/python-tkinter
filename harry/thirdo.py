from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("455x244")
#photo = PhotoImage(file="1.png")

#for jpg images

image = Image.open("pic1.jpg")
photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)

varun_label.pack()

root.mainloop()