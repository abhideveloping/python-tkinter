from tkinter import *
root = Tk()
root.geometry("444x233")
root.title('Abhinandan')

#Important Label Options
#text - adds the Text
#bd - background
#fg - foreground
#font - sets the font
#padx - x paddin
#pady - y padding
#relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE
title_label = Label(text='''Hey this is abhinandan tiwari and wi Just don't knwo what I am doing.. this ese so many thigns in the
                    world which you shoudl be ocnsidering on the occasion for thw way we are and for the way how things jut workout is something
                    is amazing and for the way how things just immersed is something amazing. and for the way how things just work out. is something you
                    just convey how things just workout and the way how things just wrokout is osmething amazing. and for thw way you are and for thw way how
                    you thought that the thigns should be working is something amazing. and you just don't settle for somethign which is just not as per your standard
                    and you are the one who is working like hell just to make sure that you are the one who is a beast but it's not quite true.
                    you are hurting your mother and things aren't way you wanted them to be working.and now this is your fault.
                    ''', bg="red", fg="white", padx=23, pady=44, font="comicasansms 19 bold", borderwidth=3, relief=SUNKEN)
title_label.pack()
#Imoprtant pack options
#anchor = nw
#side = top, bottom, left, right
#fill 
#padx
#pady


title_label.pack(side=LEFT)
root.mainloop()