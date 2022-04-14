import scriptBackend
from tkinter import *

window = Tk()
window.title("Bookstore Recods")

def get_selelected_row(event):
    try:
        global selected_tup
        index=list1.curselection()[0]
        selected_tup=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tup[1])
        e2.delete(0,END)
        e2.insert(END,selected_tup[2])
        e3.delete(0,END)
        e3.insert(END,selected_tup[3])
        e4.delete(0,END)
        e4.insert(END,selected_tup[4])
    except IndexError:
        pass
    


l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

l2 = Label(window, text="Year")
l2.grid(row=1, column=0)

year_text = StringVar()
e2 = Entry(window, textvariable=year_text)
e2.grid(row=1, column=1)

l3 = Label(window, text="Author")
l3.grid(row=0, column=2)

authur_text = StringVar()
e3 = Entry(window, textvariable=authur_text)
e3.grid(row=0, column=3)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


def view_command():
    list1.delete(0, END)
    for row in scriptBackend.view():
        list1.insert(END, row)

list1.bind('<<ListboxSelect>>', get_selelected_row)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

def search_command():
    list1.delete(0, END)
    for row in scriptBackend.search(title_text.get(), authur_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

def add_new():
    scriptBackend.insert(title_text.get(), authur_text.get(), year_text.get(), isbn_text.get())


b3 = Button(window, text="Add Entry", width=12, command=add_new)
b3.grid(row=4, column=3)

def update_command():
    scriptBackend.update(selected_tup[0], title_text.get(), authur_text.get(), year_text.get(), isbn_text.get())
    print(selected_tup[0], title_text.get(), authur_text.get(), year_text.get(), isbn_text.get())

b4 = Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

def delete_command():
    scriptBackend.delete(selected_tup[0])

b5 = Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
