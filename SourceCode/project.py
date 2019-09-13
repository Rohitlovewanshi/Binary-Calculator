from Tkinter import *
from tkMessageBox import *
root=Tk()
root.resizable(width=False,height=False)
root.geometry('1000x600')
a=PhotoImage(file='image.gif')
Label(root,image=a).place(x=0,y=0)
Label(root,text='BINARY CONVERSION CALCULATOR',font='times 20 bold',height=2,relief='sunken',bg='#F08080').place(x=260,y=40)

def cal():
    root1=Tk()
    root1.resizable(width=False,height=False)
    root1.configure(background='#ADD8E6')
    
    def add():
        if len(e1.get())==0 or len(e2.get())==0:
            showerror('Error','Invalid input')
            return
        e3.delete(0,END)
        try:
            sum=bin(int(e1.get(),2)+int(e2.get(),2))
            sum=int(str(sum)[2:])
            e3.insert(16,sum)
        except:
            showerror('Error','Invalid literals')
        return
    def subs():
        if len(e1.get())==0 or len(e2.get())==0:
            showerror('Error','Invalid input')
            return
        e3.delete(0,END)
        try:
            sum=bin(int(e1.get(),2)-int(e2.get(),2))
            sum=int(str(sum)[2:])
            e3.insert(16,sum)
        except:
            showerror('Error','Invalid literals')
        return
    def multi():
        if len(e1.get())==0 or len(e2.get())==0:
            showerror('Error','Invalid input')
            return
        e3.delete(0,END)
        try:
            sum=bin(int(e1.get(),2)*int(e2.get(),2))
            sum=int(str(sum)[2:])
            e3.insert(16,sum)
        except:
            showerror('Error','Invalid literals')
        return
    def div():
        if len(e1.get())==0 or len(e2.get())==0:
            showerror('Error','Invalid input')
            return
        e3.delete(0,END)
        try:
            sum=bin(int(e1.get(),2)/int(e2.get(),2))
            sum=int(str(sum)[2:])
            e3.insert(16,sum)
        except:
            showerror('Error','Invalid literals')
        return
    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
    def exit1():
        root1.destroy()
    def insert1(x):
        e1.insert(16,x)     
    
    Label(root1,text='Binary Calculator',font='algerian 20 bold',bg='#ADD8E6').grid(row=0,column=0,columnspan=4)
    Label(root1,text='1.Number:',font='times 17',bg='#ADD8E6',width=15,height=3,anchor=W).grid(row=1,column=0,columnspan=2)
    Label(root1,text='2.Number:',font='times 17',bg='#ADD8E6',width=15,height=3,anchor=W).grid(row=2,column=0,columnspan=2)
    Label(root1,text='Result:',font='times 17',bg='#ADD8E6',width=15,height=3,anchor=W).grid(row=3,column=0,columnspan=2)
    e1=Entry(root1,font='arial 15 bold',width=40,bd=5)
    e1.grid(row=1,column=2,columnspan=2)
    e2=Entry(root1,font='arial 15 bold',width=40,bd=5)
    e2.grid(row=2,column=2,columnspan=2)
    e3=Entry(root1,font='arial 15 bold',width=40,bd=5)
    e3.grid(row=3,column=2,columnspan=2)
    Button(root1,text='1',height=2,font='times 14',activebackground='#FAEBD7',command=lambda:insert1(1)).grid(row=4,column=0,sticky=N+S+E+W)
    Button(root1,text='0',height=2,font='times 14',activebackground='#FAEBD7',command=lambda:insert1(0)).grid(row=4,column=1,sticky=N+S+E+W)
    Button(root1,text='+',height=2,font='times 14',activebackground='#FAEBD7',command=add).grid(row=4,column=2,sticky=N+S+E+W)
    Button(root1,text='-',height=2,font='times 14',activebackground='#FAEBD7',command=subs).grid(row=4,column=3,sticky=N+S+E+W)
    Button(root1,text='delete',height=2,font='times 14',activebackground='#FAEBD7').grid(row=5,column=0,columnspan=2,sticky=N+S+E+W)
    Button(root1,text='x',height=2,font='times 14',activebackground='#FAEBD7',command=multi).grid(row=5,column=2,sticky=N+S+E+W)
    Button(root1,text='/',height=2,font='times 14',activebackground='#FAEBD7',command=div).grid(row=5,column=3,sticky=N+S+E+W)
    Button(root1,text='exit',height=2,font='times 14',activebackground='#FAEBD7',command=exit1).grid(row=6,column=0,columnspan=2,sticky=N+S+E+W)
    Button(root1,text='clear all',height=2,font='times 14',activebackground='#FAEBD7',command=clear).grid(row=6,column=2,columnspan=2,sticky=N+S+E+W)
    root1.mainloop()

def con():
    root2=Toplevel()
    root2.resizable(width=False,height=False)
    root2.configure(background='#ADD8E6')
    Label(root2,text='Binary Conversion',font='algerian 20 bold',bg='#ADD8E6').grid(row=0,column=0,columnspan=4)
    Label(root2,text='Enter Number:',bg='#ADD8E6',height=1,width=10,font='times 14').grid(row=1,column=0,pady=20,padx=10)
    e4=Entry(root2,font='arial 15 bold',width=40,bd=5)
    e4.grid(row=1,column=1,columnspan=3)
    Label(root2,text='Result:',bg='#ADD8E6',height=1,width=10,font='times 14').grid(row=2,column=0,pady=20,padx=10)
    e5=Entry(root2,font='arial 15 bold',width=40,bd=5)
    e5.grid(row=2,column=1,columnspan=3)
    v1=IntVar()
    v2=IntVar()
    Label(root2,text='From:',bg='#ADD8E6',height=1,width=10,font='times 14').grid(row=3,column=0,pady=20,padx=10)
    Radiobutton(root2,text='decimal',bg='#ADD8E6',variable=v1,value=1,font='times 13').grid(row=4,column=0)
    Radiobutton(root2,text='Binary',bg='#ADD8E6',variable=v1,value=2,font='times 13').grid(row=4,column=1)
    Radiobutton(root2,text='Octal',bg='#ADD8E6',variable=v1,value=3,font='times 13').grid(row=4,column=2)
    Radiobutton(root2,text='Hexadecimal',bg='#ADD8E6',variable=v1,value=4,font='times 13').grid(row=4,column=3)
    Label(root2,text='To:',height=1,bg='#ADD8E6',width=10,font='times 14').grid(row=5,column=0,pady=20,padx=10)
    Radiobutton(root2,text='decimal',bg='#ADD8E6',variable=v2,value=1,font='times 13').grid(row=6,column=0)
    Radiobutton(root2,text='Binary',bg='#ADD8E6',variable=v2,value=2,font='times 13').grid(row=6,column=1)
    Radiobutton(root2,text='Octal',bg='#ADD8E6',variable=v2,value=3,font='times 13').grid(row=6,column=2)
    Radiobutton(root2,text='Hexadecimal',bg='#ADD8E6',variable=v2,value=4,font='times 13').grid(row=6,column=3)
    
    def convert():
        e5.delete(0,END)
        if len(e4.get())==0:
            showerror('Error','Invalid input')
            return
        if v1.get()==1 and v2.get()==1:
            showerror('Error','Wrong selection')
            return
        if  v1.get()==1 and v2.get()==2:
            try:
                e5.insert(16,int(str(bin(int(e4.get())))[2:]))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==1 and v2.get()==3:
            try:
                e5.insert(16,int(str(oct(int(e4.get())))[1:]))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==1 and v2.get()==4:
            try:
                e5.insert(16,int(str(hex(int(e4.get())))[2:]))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==2 and v2.get()==1:
            try:
                e5.insert(16,int(e4.get(),2))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==2 and v2.get()==2:
            showerror('Error','Wrong selection')
            return
        if v1.get()==2 and v2.get()==3:
            try:
                e5.insert(16,int(str(oct(int(e4.get(),2)))[1:]))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==2 and v2.get()==4:
            try:
                e5.insert(16,int(str(hex(int(e4.get(),2)))[2:]))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==3 and v2.get()==1:
            try:
                e5.insert(16,int(e4.get(),8))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==3 and v2.get()==2:
            try:
                e5.insert(16,int(str(bin(int(e4.get(),8)))[2:]))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==3 and v2.get()==3:
            showerror('Error','Wrong selection')
            return
        if v1.get()==3 and v2.get()==4:
            try:
                e5.insert(16,int(str(hex(int(e4.get(),8)))[2:]))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==4 and v2.get()==1:
            try:
                e5.insert(16,int(e4.get(),16))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==4 and v2.get()==2:
            try:
                e5.insert(16,int(str(bin(int(e4.get(),16)))[2:]))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==4 and v2.get()==3:
            try:
                e5.insert(16,int(str(oct(int(e4.get(),16)))[1:]))
            except:
                showerror('Error','Invalid literals')
                return
            return
        if v1.get()==4 and v2.get()==4:
            showerror('Error','Wrong selection')
            return
    
    Button(root2,text='Convert',height=1,width=10,font='times 14',bg='green',command=convert).grid(row=7,column=0,columnspan=4,pady=20,padx=10)
    root2.mainloop()

Button(root,text='Calculator',font='times 20 bold',width=16,height=2,bg='#F08080',activebackground='green',command=cal).place(x=150,y=300)
Button(root,text='Conversion',font='times 20 bold',width=16,height=2,bg='#F08080',activebackground='green',command=con).place(x=550,y=300)
root.mainloop()
