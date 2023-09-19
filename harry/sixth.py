from tkinter import *
root = Tk()
root.geometry("655x240")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, borderwidth=9, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")


l = Label(f1, text="Project Tkinter - Pycharm")
l.pack(pady=42)

l = Label(f2, text="welcome to sublime text", font="Helvetica 16 bold", fg="red", pady=22)
l.pack()
root.mainloop()