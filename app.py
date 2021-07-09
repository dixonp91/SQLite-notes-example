import sqlite3 as sl
from watch_class import Watch


con = sl.connect('watch.db')
c = con.cursor()

with con:
    c.execute("""CREATE TABLE watches(
           
               brand TEXT,
                model TEXT,
                cost REAL
    );""")

def insert_watch(watch):
    with con:
        c.execute("INSERT INTO watches VALUES( :brand, :model, :cost)", {'brand' : watch.brand, 'model':watch.model, 'cost':watch.cost})


def watch_list():
    c.execute("SELECT * FROM watches;")
    return c.fetchall()


def get_watch_by_brand(brand):
    c.execute("SELECT * FROM watches WHERE brand = :brand", {'brand' : brand})
    return c.fetchall()

def update_cost(watch, cost):
    with con:
        c.execute("UPDATE watches SET cost = :cost WHERE model = :model", {'cost': cost, 'model': watch.model})

def delete_watch(watch):
    with con:
        c.execute("DELETE FROM watches WHERE model = :model", {'model':watch.model})

Timex_avi = Watch('timex', 'avi', 89)
Or_kam = Watch('orient', 'kammasu', 280)
tsot_prx = Watch ('tissot', 'prx', 470)

insert_watch(Timex_avi)
insert_watch(Or_kam)
insert_watch(tsot_prx)

fav_wtc = get_watch_by_brand('tissot')
print(fav_wtc)

delete_watch(Timex_avi)
watchList = watch_list()
print(watchList)

con.close()