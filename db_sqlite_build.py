import sqlite3 as sl



def build_db():
    con = sl.connect('customers.db')
    c = con.cursor()
    with con:
        c.execute(""" CREATE TABLE customers(
            first_name TEXT,
            last_name TEXT,
            email TEXT
        );

        """)

    con.commit()

