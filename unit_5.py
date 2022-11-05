'''from tkinter import*
win=Tk()
l1=Label(win,text="yellow color",bg='yellow',fg='black').pack()
l2=Label(win,text='blue color',bg='blue',fg='black').pack()
l3=Label(win,text='green color',bg='green',fg='black').pack()
mainloop()'''

from tkinter import*
master = Tk()
l1 = Label(master, text = "First:")
l2 = Label(master, text = "Second:")
l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)
#l1.grid(row = 0, column = 0, sticky = W, pady = 2)
#l2.grid(row = 1, column = 0, sticky = W, pady = 2)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#e1.grid(row=0, column=1, pady=2)
#e2.grid(row=1, column=1, pady=2)
mainloop()


'''from tkinter import*
colours=['blue','orange','green','yellow']
r=0
for c in colours:
    Label(text=c,relief=RIDGE,width=20).grid(row=r,column=0)
    Entry(bg=c,relief=SUNKEN,width=10).grid(row=r,column=1)
    r=r+1
mainloop()'''


'''from tkinter import*
win=Tk()
l1=Label(win,text='subject 1')
l1.place(x=10,y=10)
e1=Entry(win,bd=5)
e1.place(x=60,y=10)


l2=Label(win,text='subject 2')
l2.place(x=10,y=15)
e2=Entry(win,bd=5)
e2.place(x=40,y=30)

l3=Label(win,text='total')
l3.place(x=20,y=20)
e3=Entry(win,bd=5)
e3.place(x=60,y=100)

b=Button(win,text='addition')
b.place(x=100,y=100)
win.geometry("250 * 250 + 10 + 10")
win.mainloop()'''