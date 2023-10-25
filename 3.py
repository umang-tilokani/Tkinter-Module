from tkinter import *
win = Tk()
topFrame = Frame(win)
topFrame.pack()
bottomFrame = Frame(win)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topFrame, text = "Button 1", fg="red")
button2 = Button(topFrame, text = "Button 2", fg="yellow")
button3 = Button(topFrame, text = "Button 3", fg="green")
button4 = Button(bottomFrame, text = "Button 4", fg="blue")
# packing the components
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
win.mainloop()
