import psycopg2

def conn():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='123456' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mystore(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='123456' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mystore(item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO mystore VALUES(?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

insert("Milk", 10, 20)
insert("Curd", 1, 10)

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='123456' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("Select * from mystore")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


print(view())

# def delete(item):
#     conn = psycopg2.connect("dbname='database1' user='postgres' password='123456' host='localhost' port='5432'")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM mystore WHERE item = ?", (item,))
#     conn.commit()
#     conn.close()

# delete("Curd")

# print(view())

# def update(quantity, price, item):
#     conn = psycopg2.connect("dbname='database1' user='postgres' password='123456' host='localhost' port='5432'")
#     cur = conn.cursor()
#     cur.execute("UPDATE mystore SET quantity = ? , price = ? WHERE item = ?", (quantity, price, item))
#     conn.commit()
#     conn.close()

# update(1, 50, "Milk")

# print(view())

# update(100, 5, "Milk")

# print(view())