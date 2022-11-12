from tkinter import *

root=Tk()
Label(root,text="Firts name").grid(row=1,column=0,sticky=W)
e1=Entry(root).grid(row=1,column=1,sticky=E)

Label(root,text="Last name").grid(row=2,column=0,sticky=W)
e2=Entry(root).grid(row=2,column=1,sticky=E)
Text(root).grid(row=3,column=1,sticky=E)
root.mainloop()