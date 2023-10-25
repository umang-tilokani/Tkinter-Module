from tkinter import *
win = Tk()
win.geometry("200x100")
name = Label(win, text="Name")
email = Label(win, text="Email-Id")
password = Label(win, text="Password")

entry_1 = Entry(win)
entry_2 = Entry(win)
entry_3 = Entry(win, show="*")

check = Checkbutton(win, text="Keep Me Logged In!")

name.grid(row=0)
email.grid(row=1)
password.grid(row=2)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)

check.grid(columnspan=2)
win.mainloop()
