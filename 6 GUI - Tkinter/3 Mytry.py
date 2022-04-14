from tkinter import *

window = Tk()
window.title("Calculator")

def check():
    if text_num.get().isnumeric():
        t1.insert(END, "It is a Numeric Value\n")
    else:
        t1.insert(END, "Not a Numeric Value\n")

b1 = Button(window, text="Execute", command=check)
b1.grid(row=0, column=0)

text_num = StringVar()
e1 = Entry(window, textvariable=text_num)
e1.grid(row=0, column=1)

t1 = Text(window)
t1.grid(row=1, column=1)



window.mainloop()
