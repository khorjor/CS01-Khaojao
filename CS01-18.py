from tkinter import *
root = Tk()
root.title("First GUI")
myText = Label(text="My name is",fg="blue",font=20).grid(row=0,column=1)
myText = Label(text="Pornpawee",fg="green",font=20).grid(row=1,column=2)
myText = Label(text="Khummee",fg="red",font=20).grid(row=3,column=3)
root.geometry("300x300")
root.mainloop()