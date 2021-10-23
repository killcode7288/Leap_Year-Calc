from tkinter import *
from tkinter import messagebox
import time

def check():
    year_entered = entry_1.get()
    Output.delete(0.0, END)
    
    length = str(year_entered)
    if len(length) == 0:
        Output.insert(END, " Please enter a year")
    elif len(length) > 4:
        Output.insert(END, f"{year_entered} is not a valid year try again")
    elif len(length) < 4: 
        Output.insert(END, f"{year_entered} is not a valid year try again")
    elif int(year_entered) % 4 == 0:
        Output.insert(END, f"{year_entered} is a leap year")
    else:
        Output.insert(END, f"{year_entered} is not a leap year")



#main code
win =Tk()
win.title("Leap Year Calculator")
win.maxsize(width=300, height=270)
win.configure(background="yellow")


lbl_1 = Label(win, text="Determine which year is a leap year",bg="yellow", font="Hevetica 12 bold")
lbl_1.pack()

lbl_2 = Label(win, text="Enter year you want to check",bg="yellow", font="Hevetica 8 bold")
lbl_2.pack()

entry_1 = Entry(win, width=20)
entry_1.pack()

btn_1 = Button(win, text="Check", fg="yellow",bg="black", command=check)
btn_1.pack()

Output = Text(win, height=10,width=20, wrap=WORD)
Output.pack()

lbl_3 = Label(win, text="Copyright©2021|DarlingCorpTech",bg="yellow", font="Hevetica 8 bold")
lbl_3.pack()

win.mainloop()