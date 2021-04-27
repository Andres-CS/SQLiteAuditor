import sqlite3

def tableinfo(conn):
    crs = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [
        v[0] for v in crs.fetchall()
        if v[0]  != 'sqlite_sequence'
    ]
    crs.close()
    return tables

conn1 = sqlite3.connect('/home/app/db/newACCS.db')
conn2 = sqlite3.connect('/home/app/db/oldACCS.db')

t1 = tableinfo(conn1)
t2 = tableinfo(conn2)

if t1 == t2:
    print("SAME")
else:
    print("NOT SAME")