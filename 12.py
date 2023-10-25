from tkinter import *
from PIL import ImageTk,Image
win=Tk()
win.geometry("1000x1000")
win.title("Image Demo")
# for png images
photo1 = PhotoImage(file="Image2.png")
img1 = Label(image=photo1)
img1.pack()
win.mainloop()
