from tkinter import *
def quit():
    print('hello, getting out of here')
    import sys; sys.exit()
    
widget = Button(None, text="Press me to quit", command=quit)
widget.pack()
widget.mainloop()