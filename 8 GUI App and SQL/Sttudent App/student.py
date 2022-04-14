from tkinter import *
import student_backend

window = Tk()
window.title("Student Record Book")

l1 = Label(window, text="Name")
l1.grid(row=0, column=0)

name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

l2 = Label(window, text="Class")
l2.grid(row=0, column=2)

class_text = StringVar()
e2 = Entry(window, textvariable=class_text)
e2.grid(row=0, column=3)

l3 = Label(window, text="Grade")
l3.grid(row=0, column=4)

grade_text = StringVar()
e3 = Entry(window, textvariable=grade_text)
e3.grid(row=0, column=5)

list1 = Listbox(window, height=15, width=70)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)


def insert_rec():
    student_backend.insert(name_text.get(), class_text.get(), grade_text.get())

b1 = Button(window, text="ADD ENTRY", command=insert_rec)
b1.grid(row=2, column=2)


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
    except IndexError:
        pass

list1.bind('<<ListboxSelect>>', get_selelected_row)

def delete_command():
    student_backend.delete(selected_tup[0])

b2 = Button(window, text="DELETE ENTRY", command=delete_command)
b2.grid(row=2, column=3)

def show_db():
    list1.delete(0, END)
    for row in student_backend.view():
        list1.insert(END, row)

b3 = Button(window, text="SHOW ALL", command=show_db)
b3.grid(row=2, column=4)

b4 = Button(window, text="CLOSE", command=window.destroy)
b4.grid(row=2, column=5)

window.mainloop()
