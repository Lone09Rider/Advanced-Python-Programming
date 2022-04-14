import sqlite3

def create():
    conn = sqlite3.connect("StoreDB.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS canteen (products TEXT, quantity INTEGER, amount REAL)")
    conn.commit()
    conn.close()

def insert(products, quantity, amount):
    conn = sqlite3.connect("StoreDB.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS canteen (products VARCHAR(10), quantity INTEGER, amount FLOAT)")
    cur.execute("INSERT INTO canteen VALUES (?, ?, ?)", (products, quantity, amount))
    conn.commit()
    conn.close()

insert("Curd", 21, 10)

def view():
    conn = sqlite3.connect("StoreDB.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM canteen")
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row

print(view())
