#gui
'''import tkinter as tk
win=tk.Tk()
win.title("my first gui ")
win.resizable(10,0)
win.mainloop()'''

#practical 19.2
from tkinter import*
top=Tk()
b1=Button(top,text="Relief Style:Flat",relief=FLAT).pack()
b2=Button(top,text="relief style raised",relief=RAISED).pack()
b3=Button(top,text="relief style:sunken",relief=SUNKEN).pack()
b4=Button(top,text="relief style: groove",relief=GROOVE).pack()
b5=Button(top,text="relief style:ridge",relief=RIDGE).pack()
top.mainloop()


