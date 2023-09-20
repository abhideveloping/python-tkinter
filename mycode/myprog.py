from tkinter import *
def getvals():
	print(f"The value of dancer name is {dancevalue.get()}")
	print(f"The value of address is {addressvalue.get()}")
	print(f"The value of height is {heightvalue.get()}")
	print(f"The value of weight is {weightvalue.get()}")
root = Tk()
root.geometry("655x333")
root.title("Dance class form")

dancer = Label(root, text="Dancer Name")
address = Label(root, text="Address")
height = Label(root, text="Height")
weight = Label(root, text="Weight")

dancer.grid()
address.grid(row=1)
height.grid(row=2)
weight.grid(row=3)
#variable classes in tkinter 
#boolean, var, doublevar, IntVar, StringVar

dancevalue = StringVar()
addressvalue = StringVar()
heightvalue = StringVar()
weightvalue = StringVar()

danceentry = Entry(root, textvariable=dancevalue)
addressentry = Entry(root, textvariable=addressvalue)
heightentry = Entry(root, textvariable=heightvalue)
weightentry = Entry(root, textvariable=weightvalue)

danceentry.grid(row=0, column=1)
addressentry.grid(row=1, column=1)
heightentry.grid(row=2, column=1)
weightentry.grid(row=3, column=1)

Button(text="Submit", command=getvals).grid()


root.mainloop()
