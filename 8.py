from tkinter import *
def left(event):
    print("Left Click")
def middle(event):
    print("Middle Click")
def right(event):
    print("Right Click")
win = Tk()
button1 = Button(win, text="Click Me")
button1.pack()
button1.bind("<Button-1>", left)
button1.bind("<Button-2>", middle)
button1.bind("<Button-3>", right)
win.mainloop()
