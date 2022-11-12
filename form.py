from tkinter import *
root=Tk()

v=IntVar()
v.set(2)
v1=IntVar()
label=Label(root ,text="What is life",justify=LEFT).pack()

Radiobutton(root,text="balling",variable=v,value=1).pack()
Radiobutton(root,text="batting",variable=v,value=2).pack()
Radiobutton(root,text="feilding",variable=v,value=3).pack()

label=Label(root ,text="What is not life",justify=LEFT).pack()
Radiobutton(root,text="balling",variable=v1,value=1).pack()
Radiobutton(root,text="batting",variable=v1,value=2).pack()
Radiobutton(root,text="feilding",variable=v1,value=3).pack()

# label1=Label(root ,text="you chose"+v1 +"and"+v,justify=LEFT).pack()2
v2=IntVar()
languages=[("nepali",1),("english",2)]
def showChoice():
    print (v2.get())

for i,vr in languages:
    Radiobutton(root,text=i,variable=v2,value=vr,command=showChoice).pack()
    
root.mainloop()
