import sqlite3 as sl
#https://www.youtube.com/watch?v=pd-0G0MigUA

#https://www.youtube.com/watch?v=byHcYRpMgI4



con = sl.connect('first_db.db')

c = con.cursor()

#c.execute("""CREATE TABLE watches (
#                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#               brand TEXT,
#                model TEXT,
#                cost REAL
#                );""")

#c.execute("""INSERT INTO watches
#                VALUES (1, "Tissot", "PRX", 380.91);""")


#c.execute("SELECT * FROM watches;")

#c.fetchone()
#c.fetchmany(5)
#c.fetchall()

with con:
    data = c.execute("SELECT * FROM watches;")
    for row in data:
        print(row)


con.commit()
con.close()