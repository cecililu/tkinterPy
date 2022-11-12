from tkinter import *
root = Tk()
image=PhotoImage(file='./cecil.jpg')
w1 = Label(root, image=image).pack(side="right")
explanation = """<h1>At present, only GIF and PPM/PGM formats
are supported, but an interface exists to allow
additional image file formats to be added easily.</h1>"""
a=Label(root, text=explanation,justify='left').pack(side="left")
root.mainloop()