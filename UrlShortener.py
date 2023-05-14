import pyshorteners
from tkinter import *

win  = Tk()
win.geometry("500x300")

win.config(background="purple")

def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)


Label(win,text="Enter Your URL Link Below",font="Arial 15 bold",bg="skyblue",foreground="Black",).pack(fill="x")

entry1 = Entry(win,font="12",border="4",width="45")
entry1.pack(pady=25,padx=20)

Button(win,text="Submit URL",font="impack 12 bold",background="yellow",foreground="Black",width="15",command=short).pack()

entry2 = Entry(win,font="Arial 12 bold",background="pink",width=40,bd=0)
entry2.pack(pady=45,padx=30)

mainloop()





