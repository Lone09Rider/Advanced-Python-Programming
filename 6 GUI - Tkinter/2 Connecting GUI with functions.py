from tkinter import *

window = Tk()

def km_miles():
    print(e1_value.get())
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

b1 = Button(window, text="Extecute",command=km_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, width=20, height=10)
t1.grid(row=1, column=1)


window.mainloop()