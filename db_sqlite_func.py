import sqlite3 as sl


def insert():
    con = sl.connect('customers.db')
    c = con.cursor()
    many_customers = [('wes', 'brown', 'wes@email.com'), 
                  ('bob', 'smith', 'bob@email.com'), 
                  ('eric', 'hall', 'eric@email.com')]
    with con:
        c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


def show_all():
    con = sl.connect('customers.db')
    c = con.cursor()
    c.execute("SELECT * FROM customers")
    query = c.fetchall()
    for q in query:
      print(q)