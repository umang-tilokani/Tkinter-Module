# My Store Project
from tkinter import *

def getvals():
    print("Submitting Form!")

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentvalue.get(), foodservicevalue.get()}")

    with open("record.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentvalue.get(), foodservicevalue.get()}\n")

win = Tk()
win.geometry("400x300")

# Heading
Label(win, text="Welcome to My Store", font="Comicsansms 13 bold", pady=15).grid(row=0, column=3)

# Text for our form
name = Label(win, text="Name")
phone = Label(win, text="Phone")
gender = Label(win, text="Gender")
emergency = Label(win, text="Emergency Contact")
payment = Label(win, text="Payment Mode")

# Pack text from our forms
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment.grid(row=5, column=2)

# Tkinter variables for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

# Entries for our form
nameentry = Entry(win, textvariable=namevalue)
phonentry = Entry(win, textvariable=phonevalue)
genderentry = Entry(win, textvariable=gendervalue)
emergencyentry = Entry(win, textvariable=emergencyvalue)
paymentmodeentry = Entry(win, textvariable=paymentvalue)

# Packing the entries
nameentry.grid(row=1, column=3)
phonentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# Checkbox
foodservice = Checkbutton(text="Want to prebook your meals?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# Button
Button(text="Submit to MyStore", command=getvals).grid(row=7, column=3)
win.mainloop()
