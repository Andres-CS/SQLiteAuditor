import sqlite3, threading, time, pathlib
from datetime import datetime


def tableinfo(dbname, results):
    print("TABLEINFO")
    msg = "GOING TO QUERY DB: "+dbname+", IN THREAD: "+threading.current_thread().name
    print(msg)

    #SQLite Connection
    conn = sqlite3.connect(dbname)
    crs = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [
        v[0] for v in crs.fetchall()
        if v[0]  != 'sqlite_sequence'
    ]
    crs.close()
    results.append(tables) #HOLDS TABLE INFO

def modtime(filepath, results):
    file = pathlib.Path(filepath)
    print( datetime.fromtimestamp(file.stat().st_mtime) )
    results.append(datetime.fromtimestamp(file.stat().st_mtime))