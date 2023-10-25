from tkinter import *
def fun1(event):
    print("It's Working!")
win = Tk()
win.geometry("100x100")
button = Button(win, text="Click Me")
button.bind("<Button-1>", fun1)
button.pack()
win.mainloop()
