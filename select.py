# Import module
from tkinter import *
from tkinter.ttk import *

# Create object
root = Tk()
  
root.geometry( "500x500" )
  
options = [
    "Select Province",
    "Province 1",
    "Province 2",
    
]
province1=[ "Select District",
           'district1_province1',
           'distric2_province1'
            ]
province2=["Select District",
           'district1_province2',
           'districe2_province2'
            ]
district1_province1=[
           "Select Municipality",
           'municipalty1_district1_province1',
           'municpality2_district1_province1'  
            ]
district2_province1=[
           "Select Municipality",
           'municipalty1_district1_province1',
           'municpality2_district2_province1'  
            ]

district1_province2=[
              "Select Municipality",
           'municipalty1_district1_province2',
           'municpality2_district1_province2'  
            ]
district2_province2=[
    "Select Municipality",
           'municipalty1',
           'municpality2'  
            ]
# def makeMunicipalityDD():
#      drop= OptionMenu( root  ,values=district1)
value_province = StringVar(root)
value_district = StringVar(root)
value_muni = StringVar(root)

def makedistrictDD(province):
     if (province=="Province 1"):
         drop= OptionMenu( root ,value_district,*province1,command=makedistrictMuni)
         drop.pack()
     if (province=="Province 2"):
         drop= OptionMenu( root ,value_district,*province2,command=makedistrictMuni)
         drop.pack()

def mkLabel(a):
    adddress=value_province.get()+ "   "+value_district.get() + "   "+value_muni.get()  
    Label(root,text=adddress).pack()
    
def makedistrictMuni(district):
    print(district)
    if (district=="district1_province1"):
         drop= OptionMenu( root ,value_muni,*district1_province1,command=mkLabel)
         drop.pack()
    if (district=="district2_province1"):
         drop= OptionMenu( root ,value_muni,*district2_province1,command=mkLabel)
         drop.pack()
     
    if (district=="district1_province2"):
         drop= OptionMenu( root ,value_muni,*district1_province2,command=mkLabel)
         drop.pack()
    if (district=="district2_province1"):
         drop= OptionMenu( root ,value_muni,*district2_province2,command=mkLabel)
         drop.pack()


drop = OptionMenu(root,value_province,*options,command=makedistrictDD)
drop.pack()
  

# Execute tkinter
root.mainloop()