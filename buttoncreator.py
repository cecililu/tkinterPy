from tkinter import *
root=Tk()
def addlabel(a):
    w=Label(root,text=a)
    #pack method tells tk to fit size of the window to given text
    w.pack()
def buttoncreator():
    b=Button(text="Nice Job",command=addlabel)
    b.pack()
    
b=Button(text="Create Another button",command=buttoncreator)
b.pack()
root.mainloop()

