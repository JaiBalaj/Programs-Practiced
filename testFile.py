from tkinter import *
from tkinter import messagebox

def show_entry_fields():
    try:
        val=int(e1.get())
    except ValueError:
        messagebox.showwarning("Invalid Entry", "Please Entry Integer Values Only !")
        return
    if (int(e1.get())>100):
        messagebox.showwarning("Invalid Entry","Chunk size is too large !")
        return
    messagebox.showinfo("Chunk Size: ",e1.get())

master = Tk()
Label(master, text="Chunk Size:").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Ok', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop()

print("Now Conti..")