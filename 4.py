from tkinter import *
win = Tk()
win.geometry("200x200")
rLabel = Label(win, text="RED", bg="red", fg="white")
rLabel.pack(fill=X)
gLabel = Label(win, text="GREEN", bg="green", fg="white")
gLabel.pack(fill=X)
bLabel = Label(win, text="BLUE", bg="blue", fg="white")
bLabel.pack(side=LEFT, fill=Y)
win.mainloop()
