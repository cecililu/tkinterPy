from tkinter import *
root=Tk()
#radiobox
# v=IntVar()
# v.set(2)
# v1=IntVar()
# label=Label(root ,text="What is life",justify=LEFT).pack()

# Radiobutton(root,text="balling",variable=v,value=1).pack()
# Radiobutton(root,text="batting",variable=v,value=2).pack()
# Radiobutton(root,text="feilding",variable=v,value=3).pack()

# label=Label(root ,text="What is not life",justify=LEFT).pack()
# Radiobutton(root,text="balling",variable=v1,value=1).pack()
# Radiobutton(root,text="batting",variable=v1,value=2).pack()
# Radiobutton(root,text="feilding",variable=v1,value=3).pack()

# # label1=Label(root ,text="you chose"+v1 +"and"+v,justify=LEFT).pack()2
# v2=IntVar()
# languages=[("nepali",1),("english",2)]
# def showChoice():
#     print (v2.get())

# for i,vr in languages:
#     Radiobutton(root,text=i,variable=v2,value=vr,command=showChoice).pack()
    

#checkbox
label1=Label(root ,text="What are your favoirite food",justify=LEFT).grid(row=0,sticky=W)
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
Checkbutton(root,text='momo' ,variable=var1).grid(row=1,sticky=W)
Checkbutton(root,text='pxxa' ,variable=var2).grid(row=2,sticky=W)
Checkbutton(root,text='dal' ,variable=var3).grid(row=1,sticky=E)
Checkbutton(root,text='bhat' ,variable=var4).grid(row=2,sticky=E)

root.mainloop()
