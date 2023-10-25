from tkinter import *
from PIL import ImageTk,Image
win=Tk()
win.geometry("1000x1000")
win.title("Image Demo")
# for jpg and other formats
photo2 = Image.open("Image1.jpg")
img2 = ImageTk.PhotoImage(photo2)
photolabel = Label(image=img2)
photolabel.pack()
win.mainloop()
