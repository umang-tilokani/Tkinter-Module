from tkinter import *

def getvals():
    print(f"The value of username is:{uservalue.get()}")
    print(f"The value of password is:{passvalue.get()}")

root = Tk()
root.geometry("200x100")

user = Label(root, text="Username")
passwd = Label(root, text="Password")

user.grid()
passwd.grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue, show="*")

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()
root.mainloop()
