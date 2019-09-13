from Tkinter import *
root=Tk()
root.geometry('1000x600')
root.configure(background='light blue')
a=PhotoImage(file='IMG_20180803_222052.gif')
def fun(e):
    root.destroy()
    import project
lb=Label(root,image=a)
lb.bind('<Motion>',fun)
lb.place(x=300,y=20)
Label(root,text='Name:       Rohit Lovewanshi',font='algerian 20').place(x=250,y=270)
Label(root,text='Enr :         171B101',font='algerian 20').place(x=250,y=320)
Label(root,text='Batch:     B3',font='algerian 20').place(x=250,y=370)
Label(root,text='Email:      rohitlovewanshi78@gmail.com',font='algerian 20').place(x=250,y=420)
Label(root,text='Mob:         7746861342',font='algerian 20').place(x=250,y=470)
root.mainloop()
