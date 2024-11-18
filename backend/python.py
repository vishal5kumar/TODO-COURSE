import sqlite3
from backend.python_functions import get_schema



one_conn = sqlite3.connect('app1.sqlite')
one_cursor = one_conn.cursor()

two_conn = sqlite3.connect('app2.sqlite')
two_cursor = two_conn.cursor()

x = get_schema("products", one_cursor)
print(x)

TABLE1_SQL_CREATE_QUERY = "create table products ( id integer primary key, name text not null, price integer default 0)"
# one_cursor.execute(TABLE1_SQL_CREATE_QUERY)



data = [
    ('a',2000),
    ('b',3000),
    ('c',4000),
    ('d',5000),
    ('e',6000),
    ('f',7000),
    ('g',8000),
    ('h',9000),
    ('i',1000)

]

insert_query = "INSERT  INTO products(name,price) VALUES(?,?)"
one_cursor.executemany(insert_query, data)
one_conn.commit()



one_cursor.execute("SELECT * FROM products")
data = one_cursor.fetchall()

try:
    two_cursor.execute(x)  # Execute the schema from app1 to create the table in app2
    two_conn.commit()
    print("Table created in app2.")
except sqlite3.OperationalError as e:
    print(f"Table creation failed (maybe it already exists): {e}")



insert_query = "INSERT INTO products(id, name, price) VALUES(?, ?, ?)"
two_cursor.executemany(insert_query, data)
two_conn.commit()



one_conn.close()
two_conn.close()
# two_cursor.execute(x)
    











