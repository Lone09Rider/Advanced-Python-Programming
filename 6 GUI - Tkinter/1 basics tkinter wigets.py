from tkinter import *

window = Tk()

b1 = Button(window, text="Execute")
# b1.pack()
b1.grid(row=2, column=3)

e1 = Entry(window)
e1.grid(row=2, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=2, column=2)

window.mainloop()
