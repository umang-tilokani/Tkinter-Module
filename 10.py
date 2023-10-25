from tkinter import *
def fun1():
    print("It's Working!!")
def resize():
    win.geometry("200x200")
def default():
    win.geometry("500x400")
win = Tk()
win.geometry("500x400")
menu = Menu(win)
win.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project..", command=fun1)
subMenu.add_command(label="New File..", command=fun1)
subMenu.add_command(label="Resize..", command=resize)
subMenu.add_command(label="Default..", command=default)
subMenu.add_command(label="Exit", command=quit)
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=fun1)
editMenu.add_command(label="Copy", command=fun1)
editMenu.add_command(label="Paste", command=fun1)
win.mainloop()
