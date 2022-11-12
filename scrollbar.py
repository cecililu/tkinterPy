from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

root=Tk()

menu=Menu(root)    
root.config(menu=menu)
filemenu=Menu(menu)
filemenu1=Menu(menu)

menu.add_cascade(label='file',menu=filemenu)
menu.add_cascade(label='toolbox',menu=filemenu1)

filemenu.add_command(label='new')
filemenu.add_separator()
filemenu.add_command(label='open')

filemenu1.add_command(label='Buffer')
filemenu1.add_command(label='Euclideian distance')



text=""""
Wikipedia is an encyclopedia that anyone can edit, and tens of millions already have!

Wikipedia's purpose is to benefit readers by acting as a widely accessible and free encyclopedia that contains information on all branches of knowledge. Hosted by the Wikimedia Foundation, Wikipedia consists of freely editable content whose articles also provide numerous links to guide readers to related pages with more information.

Written collaboratively by largely anonymous volunteers, anyone with Internet access and in good standing can write and make changes to Wikipedia articles (except in limited cases where editing is restricted to prevent disruption or vandalism).

Since its creation on January 15, 2001, Wikipedia has grown into the world's largest reference website, attracting over a billion visitors monthly. It currently has more than fifty-nine million articles in more than 300 languages, including 6,573,564 articles in English with 124,119 active contributors in the past month.

The fundamental principles of Wikipedia are summarized in its five pillars. The Wikipedia community has developed many policies and guidelines, with which familiarity is not a requirement for contributing.

Anyone is allowed to add or edit text, references, images, and other media here. What is contributed is more important than who contributes it. To remain, the content must be free of copyright restrictions and libelous material about living people. It must conform with Wikipedia's policies, including being verifiable against a published reliable source. Editors' opinions, beliefs, and unreviewed research will not remain. Contributions cannot damage Wikipedia, as its software allows easy reversal of errors, and many experienced editors watch to ensure that edits are improvements. Begin by simply clicking the Edit button at the top of any editable page!

Wikipedia differs from printed references in important ways. It is continually created and updated, and articles on new events appear within minutes rather than months or years. Because anyone can improve Wikipedia it has become more comprehensive than any other encyclopedia. Its contributors improve the quality and quantity of the articles as well as remove misinformation, errors, and vandalism. Any reader who recognizes a mistake or finds places in articles which need more information (see Wikipedia:Researching with Wikipedia) can add to or fix articles.

Over time, Wikipedia's pages tend to become more comprehensive and balanced. Wikipedia has tested the wisdom of the crowd since 2001, and found that it succeeds. As Linus's law asserts, "Given enough eyeballs, all bugs are shallow!"
"""
S=Scrollbar(root)
S.pack(side=RIGHT,fill=Y)


S1=Scrollbar(root,orient=HORIZONTAL)
S1.pack(side=TOP,fill=X)

image=PhotoImage(file='./cecil.jpg')
w1 = Label(root, image=image)
w1.pack(side=LEFT)
t=Text(root,yscrollcommand=S.set,xscrollcommand=S1.set)
t.insert(END,text*5)

S.config(command=t.yview)
S1.config(command=t.xview)

t.pack(fill=Y)

def callback():
    name=askopenfilename()
    print(name)
    if messagebox.askyesno('quit for real','quit for real'):
       messagebox.showwarning('yes','ok yes')
    else:
        messagebox.showinfo('no','ok no')
    

    
Button(text='quit',command=callback).pack()
root.mainloop()