# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 12:47:50 2023

@author: SWAMINATHAN
"""

from sqlite3 import*
from tkinter import*
from admissionclass import *
from addmissiondbaccess import *
from tkinter import messagebox
from tkinter import ttk as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import ttk
import random



def validation():  
    eeid=eid.get()
    if len(eeid)!=4:
        errormsg.set("Enter a valid Enrollment Number...")
        return False
    ename=name.get()
    if len(ename)==0:
        errormsg.set("Student name should not be blank...")
        return False
    edob=dob.get()
    if len(edob)==0:
        errormsg.set("Date Of Birth should not be blank...")
        return False
    enum=num.get()
    if len(enum)==0:
        errormsg.set("Mobile Number should not be blank...")
        return False
    cc1=cal1.get()
    cc2=cal2.get()
    cc3=cal3.get()
    cc4=cal4.get()
    if (cc1==0 and cc2==0 and cc3==0 and cc4==0):
        errormsg.set("Course should not be blank")
        return False
    
    errormsg.set("")
    return True
          


def valueassign():
    gvalue=""
    ec1=""
    ec2=""
    ec3=""
    ec4=""
    etid=eid.get()
    ename=name.get()
    edob=dob.get()
    enum=num.get()
    eemail=email.get()
    eadd=address.get()
    ecaf=box.get()
    
    if gender.get()==1:
        gvalue="M"
    elif gender.get()==2:
        gvalue="F"
        
    if cal1.get()==1:
        ec1="Physics"
    else:
        ec1=""
    
    if cal2.get()==1:
        ec2="Mathematics"
    else:
        ec2=""
        
    if cal3.get()==1:
        ec3="Chemistry"
    else:
        ec3=""
        
    if cal4.get()==1:
        ec4="Computer Science"
    else:
        ec4=""
        
    cal='-'.join([ec1+ec2+ec3+ec4])
    
    aobj=Adminfo()
    aobj.eid=etid
    aobj.name=ename
    aobj.gender=gvalue
    aobj.dob=edob
    aobj.num=enum
    aobj.email=eemail
    aobj.address=eadd
    aobj.caf=ecaf
    aobj.cal=cal
    return aobj


def control(s):
    e_name.config(state=s)
    r_male.config(state=s)
    r_female.config(state=s)
    e_dob.config(state=s)
    e_num.config(state=s)
    e_email.config(state=s)
    e_address.config(state=s)
    box.config(state=s)
    c1.config(state=s)
    c2.config(state=s)
    c3.config(state=s)
    c4.config(state=s)
    abtn.config(state=s)
    dbtn.config(state=s)
    edbtn.config(state=s)


def clearcontrol():
    eid.set("")
    name.set("")
    gender.set(None)
    caf.set("")
    dob.set("")
    num.set("")
    email.set("")
    address.set("")
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    
def clearcontrol1():
    #eid.set(ndb)
    e_eid.config(state=DISABLED)
    name.set("")
    gender.set(None)
    caf.set("")
    dob.set("")
    num.set("")
    email.set("")
    address.set("")
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    
    
def newrecord():
    global exitflag
    control(NORMAL)
    abtn.config(state=NORMAL)
    nbtn.config(state=DISABLED)
    dbtn.config(state=DISABLED)
    edbtn.config(state=DISABLED)
    ebtn.config(state=NORMAL)
    ebtn.config(text="Cancel")
    exitflag=False


def newb():
    global saveflag
    saveflag=1
    newdb=AdmissionDB()
    ndb=newdb.appNum()
    eid.set(ndb)
    newrecord()
    clearcontrol1()
    
        
def editb():
    global saveflag
    saveflag=2
    abtn.config(text="Save")
    newrecord()
    e_eid.config(state=DISABLED)


def saverecord():
    global exitflag
    global saveflag
        
    if saveflag==1:
        if validation():           
            e=valueassign()
            adb=AdmissionDB()
            adb.addrecord(e)
            errormsg.set("Applied successfully...")
        return
        
    if saveflag==2:
        if validation():            
            e=valueassign()
            adb=AdmissionDB()
            adb.updaterecord(e)
            errormsg.set("Record updated successfully...")
        return        
    
    clearcontrol()
    eid.set("")
    control(DISABLED)
    e_eid.config(state=NORMAL)
    nbtn.config(state=NORMAL)
    ebtn.config(text="Exit")
    exitflag=True
    return
    

def searchrecord(event): 
    global exitflag
    ebtn.config(text="Cancel")
    exitflag=False
    abtn.config(state=DISABLED)
    control(DISABLED)
    name.set("")
    dob.set("")
    num.set("")
    email.set("")
    address.set("")
    caf.set("")
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    if len(eid.get())!=4:
        errormsg.set("Enter a valid Enrollment number ...")
        return
    errormsg.set("")
    adb=AdmissionDB()
    found,e=adb.search(eid.get())
    if found:
        eid.set(e.eid)
        name.set(e.name)
        dob.set(e.dob)
        num.set(e.num)
        email.set(e.email)
        address.set(e.address)
        box.set(e.caf)
        
        if e.gender=="M":
            r_male.select()
        elif e.gender=="F":
            r_female.select()
        
        if str(e.cal).find("Physics")>=0:
            c1.select()
        
        if str(e.cal).find("Mathematics")>=0:
            c2.select()
            
        if str(e.cal).find("Chemistry")>=0:
            c3.select()
            
        if str(e.cal).find("Computer Science")>=0:
            c4.select()
        
        errormsg.set("Record was shown...")
        edbtn.config(state=NORMAL)
        dbtn.config(state=NORMAL)
        return
        
    else:
        errormsg.set("Record Not Found...")
        edbtn.config(state=DISABLED)
        dbtn.config(state=DISABLED)
        return  
    errormsg.set("")
    return


def delrecord():
    errormsg.set("")
    yes=messagebox.askyesno("Remove Records","Do you want delete this record")
    if yes:
        e=AdmissionDB()
        e.delrecord(eid.get())
        clearcontrol()
        messagebox.showinfo("Delete","Record deleted successfully")
        errormsg.set("Record deleted successfully...")
    return


def appquit():
    global exitflag
    if exitflag:
        win.destroy()
    else:
        clearcontrol()
        ebtn.config(text="Exit")
        exitflag=True
        control(DISABLED)
        e_eid.config(state=NORMAL)
        abtn.config(state=DISABLED)
        edbtn.config(state=DISABLED)
        dbtn.config(state=DISABLED)
        nbtn.config(state=NORMAL)



#Main Window
win=Tk(className="Application Window")
win.geometry("600x750")
exitflag=True
saveflag=1


#Tab Widget
tabs = ttk.Notebook(win)
tabs.pack(fill=BOTH, expand=TRUE)
frame1 = ttk.Frame(tabs)
frame2 = ttk.Frame(tabs)
tabs.add(frame1, text="Tab One")
tabs.add(frame2, text="Tab Two")

#adding widget to Tab
label = Label(frame1)
label.pack(side=TOP, padx=10)

label2 = Label(frame2)
label2.pack(side=TOP, padx=10)


#Label and Entry
lbl1=Label(win,text="ALAGAPPA UNIVERSITY",font="Times 16 bold")
lbl1.place(x=170,y=10)


lbl2=Label(win,text="Online Application Form",font="Arial 15 bold",fg="blue")
lbl2.place(x=190,y=50)


lbl3=Label(win,text="Application Number",font="calibry 15 bold")
lbl3.place(x=30,y=100)
eid=StringVar()
e_eid=Entry(win,textvariable=eid,bd=2,font="helvetica 10")
e_eid.place(x=240,y=100,width=150,height=30)



lbl4=Label(win,text="Name",font="calibry 15 bold")
lbl4.place(x=30,y=150)
name=StringVar()
e_name=Entry(win,textvariable=name,bd=2,font="helvetica 10")
e_name.place(x=240,y=150,width=250,height=30)



lbl5=Label(win,text="Gender",font="calibry 15 bold")
lbl5.place(x=30,y=200)
gender=IntVar()
r_male=Radiobutton(win,text="Male",variable=gender,value=1)
r_male.place(x=240,y=200)
r_female=Radiobutton(win,text="Female",variable=gender,value=2)
r_female.place(x=300,y=200)



lbl6=Label(win,text="Date of Birth",font="calibry 15 bold")
lbl6.place(x=30,y=250)
dob=StringVar()
e_dob=Entry(win,textvariable=dob,bd=2,font="helvetica 10")
e_dob.place(x=240,y=250,width=150,height=30)



lbl7=Label(win,text="Mobile Number",font="calibry 15 bold")
lbl7.place(x=30,y=300)
num=StringVar()
e_num=Entry(win,textvariable=num,bd=2,font="helvetica 10")
e_num.place(x=240,y=300,width=150,height=30)



lbl8=Label(win,text="Email",font="calibry 15 bold")
lbl8.place(x=30,y=350)
email=StringVar()
e_email=Entry(win,textvariable=email,bd=2,font="helvetica 10")
e_email.place(x=240,y=350,width=250,height=30)



lbl9=Label(win,text="Address",font="calibry 15 bold")
lbl9.place(x=30,y=400)
address=StringVar()
e_address=Entry(win,textvariable=address,bd=2,font="helvetica 10")
e_address.place(x=240,y=400,width=250,height=30)



lbl9=Label(win,text="Course Applied For",font="calibry 15 bold")
lbl9.place(x=30,y=450)
caf=StringVar()
entries=("UG","PG","MPhil","Research")
box=tk.Combobox(win,value=entries,textvariable=caf)
box.current([0])
box.place(x=240,y=450)



lblh10=Label(win,text="Select Course",font="calibry 15 bold")
lblh10.place(x=30,y=535)
cal1=IntVar()
cal2=IntVar()
cal3=IntVar()
cal4=IntVar()
c1=Checkbutton(win,text="Physics",variable=cal1,onvalue=1,offvalue=0,height=3,width=15)
c2=Checkbutton(win,text="Mathematics",variable=cal2,onvalue=1,offvalue=0,height=3,width=15)
c3=Checkbutton(win,text="Chemistry",variable=cal3,onvalue=1,offvalue=0,height=3,width=15)
c4=Checkbutton(win,text="Computer Science",variable=cal4,onvalue=1,offvalue=0,height=3,width=15)
c1.place(x=215,y=520)
c2.place(x=365,y=520)
c3.place(x=218,y=570)
c4.place(x=370,y=570)


errormsg=StringVar()
lblerror=Label(win,textvariable=errormsg,font="arial 14 bold",fg="red")
lblerror.place(x=150,y=670)


#Button
abtn=Button(win,text="Apply",command=saverecord,bg="blue",fg="white")
abtn.place(x=50,y=630,width=100,height=30)

nbtn=Button(win,text="New",command=newb,bg="pink3",fg="black")
nbtn.place(x=150,y=630,width=100,height=30)

edbtn=Button(win,text="Edit",command=editb,bg="cyan4",fg="white")
edbtn.place(x=250,y=630,width=100,height=30)

dbtn=Button(win,text="Delete",command=delrecord,bg="magenta4",fg="white")
dbtn.place(x=350,y=630,width=100,height=30)

ebtn=Button(win,text="Exit",command=appquit,bg="red",fg="white")
ebtn.place(x=450,y=630,width=100,height=30)


#function definition for opening file dialog
def openf():
    file = filedialog.askopenfilename(initialdir='/', title="select file")

def donothing():
   filewin = Toplevel(win)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
   
#Menu
menubar = Menu(win)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newb)
filemenu.add_command(label="Open", command=openf)
filemenu.add_command(label="Save", command=saverecord)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=delrecord)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

win.config(menu=menubar)


#Image icon 
image = Image.open("save.jpg")
image = image.resize((35, 35))
image = ImageTk.PhotoImage(image) 
 
button = Button(width = 20, height = 20, image = image,command=searchrecord)
button.place(x = 380, y = 100)
win.bind('<Return>',searchrecord)


cln=Label(win,text=":",font="Arial 14 bold")
cln.place(x=220,y=100)
cln1=Label(win,text=":",font="Arial 14 bold")
cln1.place(x=220,y=150)
cln2=Label(win,text=":",font="Arial 14 bold")
cln2.place(x=220,y=200)
cln3=Label(win,text=":",font="Arial 14 bold")
cln3.place(x=220,y=250)
cln4=Label(win,text=":",font="Arial 14 bold")
cln4.place(x=220,y=300)
cln5=Label(win,text=":",font="Arial 14 bold")
cln5.place(x=220,y=350)
cln6=Label(win,text=":",font="Arial 14 bold")
cln6.place(x=220,y=400)
cln7=Label(win,text=":",font="Arial 14 bold")
cln7.place(x=220,y=450)
cln8=Label(win,text=":",font="Arial 14 bold")
cln8.place(x=220,y=535)

control(DISABLED)

win.mainloop()
