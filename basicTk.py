from tkinter import *
#creating root widget 
root=Tk()
# adding label to the root widget
w=Label(root,text='hello')
#pack method tells tk to fit size of the window to given text
w.pack()
#adding a button
b=Button(text="Goodbye",command=root.destroy)
b.pack()

root.mainloop()