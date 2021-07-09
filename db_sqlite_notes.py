import sqlite3 as sl

con = sl.connect('customers.db')
c = con.cursor()

#c.execute("INSERT INTO customers VALUES ('pat', 'dixon', 'pat.dixon@email.com');")

many_customers = [('wes', 'brown', 'wes@email.com'), 
                  ('bob', 'smith', 'bob@email.com'), 
                  ('eric', 'hall', 'eric@email.com')]

#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#c.execute("SELECT * FROM customers;")

#three types of fetch
#c.fetchone()
#c.fetchmany(3)
#c.fetchal()

#query = c.fetchall()

#for i in query:
 #   print(i[0] + "\t" + i[1] + "\t" + i[2])

#print("\n")

#c.execute(" SELECT rowid, * FROM customers;")
#row_id = c.fetchall()
#for id in row_id:
 #   print(id)
  #  print("\n")

def first_name(row_id, new_name):
    c.execute(""" UPDATE customers SET first_name = :name WHERE rowid = :row

    """, {'name': new_name, 'row': row_id})

first_name(2, 'ansley')
first_name(3, 'jack')

c.execute("SELECT * FROM customers WHERE email LIKE '%email.com' ")
q = c.fetchall()
print(q)

print('process complete')
con.commit()
#con.close()

def show_all(db):
    c.execute("SELECT * FROM :db", {'db': db})
    query = c.fetchall()
    for q in query:
      print(q)

# How to drop table from database

c.execute("DROP TABLE customers")
con.commit()
con.close()