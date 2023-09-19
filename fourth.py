from tkinter import *
def hello(event):
    print('double click to exit')
    
    def quit(event):
        print('Caught a double click, leaving')
        import sys;
        sys.exit()
        
        widget = Button(None, text='Hello Event World')
        widget.pack()
        widget.bind('<Button-1', hello)
        widget.bind('<Double-1', quit)
        widget.mainloop()