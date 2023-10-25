from tkinter import *
def fun1():
    print("Welcome to Tkinter Lessons!")
win = Tk()
win.geometry("100x100")
button = Button(win, text="Click Me", command=fun1)
button.pack()
win.mainloop()
