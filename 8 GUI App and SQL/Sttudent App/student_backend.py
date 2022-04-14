import sqlite3

def Connection():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name TEXT, sclass INTEGER, grade TEXT)")

    conn.commit()
    conn.close()


def insert(name, sclass, grade):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS student (name TEXT, sclass INTEGER, grade TEXT)")

    cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?)", (name, sclass, grade))

    conn.commit()
    conn.close()

# insert("Meenu", 10, "F")

def view():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row

print(view())

def update(id="", name="", sclass="", grade=""):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET name = ?, sclass = ?, grade = ? where id = ?", (name, sclass, grade, id,))
    conn.commit()
    conn.close()

# update(3, "Meenu", 10, "C+")

print(view())

def delete(name="", sclass="", grade=""):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("DELETE from student WHERE name = ? OR sclass = ? OR grade = ?", (name, sclass, grade))
    conn.commit()
    conn.close()

print(view())

Connection()