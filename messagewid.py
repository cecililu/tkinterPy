from tkinter import *
master = Tk()

mage=PhotoImage(file='./cecil.jpg')
w1 = Label(master, image=mage).pack(side="right")

msg = """hello my name is cecil"""
msg = Message(master, text = msg)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack(side='left')
mainloop( )