from tkinter import *

window = Tk()
window.title("Exersice 1")

def kg_gram_pound():
    t1.delete("1.0", END)
    t1.insert(END, float(kgs.get())*1000)
    t2.delete("1.0", END)
    t2.insert(END, float(kgs.get())*2.20462)
    t3.delete("1.0", END)
    t3.insert(END, float(kgs.get())*35.274)

l1 = Label(window, text="Enter the value in Kgs")
l1.grid(row=0, column=0)

kgs = StringVar()
e1 = Entry(window, textvariable=kgs)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=kg_gram_pound)
b1.grid(row=0, column=2)

l2 = Label(window, text="In Grams")
l2.grid(row=1, column=0)

t1 = Text(window, width=20, height=0)
t1.grid(row=1, column=1)

l3 = Label(window, text="In Pounds")
l3.grid(row=1, column=2)

t2 = Text(window, width=20, height=0)
t2.grid(row=1, column=3)

l4 = Label(window, text="In Ounce")
l4.grid(row=1, column=4)

t3 = Text(window, width=20, height=0)
t3.grid(row=1, column=5)

window.mainloop()