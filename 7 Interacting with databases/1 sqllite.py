import sqlite3

def create_table():
    # 1. Connect to a Database
    conn = sqlite3.connect("lite.db")
    # 2. Create a Cursour Object (Pointer)
    cur = conn.cursor()
    # 3. Write SQL Query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # 4. Commit Changes to Database
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    # 1. Connect to a Database
    conn = sqlite3.connect("lite.db")
    # 2. Create a Cursour Object (Pointer)
    cur = conn.cursor()
    # 3. Write SQL Query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    # 4. Commit Changes to Database
    conn.commit()
    conn.close()

insert("Glass", 10, 4)
insert("Coffee", 8, 2)

def view():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    cur.close()
    return rows


print(view())