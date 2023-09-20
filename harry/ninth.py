from tkinter import *


root = Tk()

def getvals():
    print("it works!")

root.geometry("644x344")
root.title('Harry Travels')

Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold").grid(row=0, column=3)
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

#tkinter variable for storing entrrrrrr
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
payementmodeentry = Entry(root, textvariable=paymentmodevalue)

# packing the entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
payementmodeentry.grid(row=5, column=3)

#checkbox
foodservice = Checkbutton(text="Want to prebook your meals", variable = foodservicevalue)
foodservice.grid(row=6, column=3)

#button & packing it and assigingin it a command
Button(text="Submit to harry travels", command=getvals).grid(row=7, column=3)
root.mainloop()