from ast import Delete
from cgitb import text
from tkinter.ttk import *
from tkinter import *
from tkinter.font import BOLD, ITALIC
from turtle import bgcolor
from PIL import Image, ImageTk
from googletrans import Translator
a = Tk()
a.geometry('480x600')
a.title("Translator - Nhóm 11")
a.resizable(width=False,height=False)
b = Image.open("hinhnendep.jpg")
c=ImageTk.PhotoImage(b)
d=Label(a,image=c)
d.place(x=0,y=0)
logo = Label(a,text="Translator",font=("Century",26,ITALIC,BOLD),bg="#4C0190",fg="red")
logo.pack(pady=13)
l1=Label(a,text="Mời bạn chọn phương thức dịch:",font=('@Microsoft JhengHei Light',11,BOLD),bg="#9706C3",fg="#FFFFFF")
l1.place(x=40,y=100)
l2=Label(a,text="Mời nhập:",font=('@Microsoft JhengHei Light',10,BOLD),bg="#9706C3",fg="#FFFFFF")
l2.place(x=40,y=155)
kq=Label(a,text="Kết quả:",font=('@Microsoft JhengHei Light',10,BOLD),bg="#9706C3",fg="#FFFFFF")
kq.place(x=40,y=417)
m = Combobox(a, font = ("Ariel",10,BOLD),width=15)
m["value"]=["Anh -> Việt","Việt -> Anh"]
m.current(0)
m.place(x=340,y=100)
box1 = Text(a,width=43,height=7,bg="#1A0065",fg="white",font = ("Ariel"))
box1.place(x=55,y=200)
box2 = Text(a,width=43,height=7,bg="#1A0065",fg="white",font = ("Ariel"))
box2.place(x=55,y=455)
def dich():
    box2.delete(1.0,END)
    try:
        s = box1.get(1.0,END)
        i = Translator()
        j = "vi"
        k = "en"
        if m.get()=="Anh -> Việt":
            j,k="en","vi"
        a1=i.translate(s,src=j,dest=k)
        b1=a1.text
        box2.insert(END,b1)
    except IndexError:
        pass
def focus():
        box1.focus()
def xoa():
        box1.delete(1.0,END)
        box2.delete(1.0,END)
        focus()
n= Button(a,text="Chọn",font = ("@Microsoft JhengHei Light",9,BOLD),bg="#9E01CC",fg="#FFFFFF",command=focus)
n.place(x=424,y=128)
clear = Button(a,text="Làm mới",font = ("@Microsoft JhengHei Light",9,BOLD),command=xoa,bg="#5010A4",fg="#FFFFFF")
clear.place(x=330,y=333)
tran = Button(a,text="Dịch",font = ("@Microsoft JhengHei Light",9,BOLD),command=dich,bg="#AD27AA",fg="#FFFFFF")
tran.place(x=406,y=333)
a.mainloop()