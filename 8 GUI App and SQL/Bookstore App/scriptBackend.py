import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT, authur TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title, authur, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT, authur TEXT, year INTEGER, isbn INTEGER)")
    cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, authur, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", authur="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book where title = ? OR authur = ? OR year = ? OR isbn = ?", (title, authur, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(title="", authur="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE title = ? OR authur = ? OR year = ? OR isbn = ?", (title, authur, year, isbn))
    conn.commit()
    conn.close()

def update(id="", title="", authur="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, authur = ?, year = ?, isbn = ? where id = ?", (title, authur, year, isbn, id))
    conn.commit()
    conn.close()

connect()

# insert('The Fire', 'Jhon Fire', 1908, 987608741231)
# # delete(year=1908)
# print(view())

# print(search(year=2000))

# update(2,"The Moon", "Jhon Smooth", 1917, 99991919)
print(view())