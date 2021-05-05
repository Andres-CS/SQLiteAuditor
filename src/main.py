import sqlite3

import threading, time

start = time.time()

def tableinfo(dbname, results):
    
    tmp_start = time.time()
    #print(tmp_start)

    name = threading.current_thread().name
    msg = "GOING TO QUERY DB: "+dbname
    print(msg)

    conn = sqlite3.connect(dbname)
    crs = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [
        v[0] for v in crs.fetchall()
        if v[0]  != 'sqlite_sequence'
    ]
    crs.close()
    results.append(tables) #HOLDS TABLE INFO
    
    tmp_end = time.time()
    #print(tmp_end)
    diff_temp = tmp_end - tmp_start
    tmp_msg = "Elapsed Time: "+str(diff_temp)
    print(tmp_msg)
    #return tables

n_threads = 2
dbpahts=['/home/app/db/newACCS.db','/home/app/db/oldACCS.db']
running_threads = list()
ts = list() #HOLDS TABLE INFO

for i in range(n_threads):
    name_th = "Thread_"+str(i)
    thread = threading.Thread(target=tableinfo, name=name_th, args=(dbpahts[i],ts))
    running_threads.append(thread)
    thread.start()


for thrd in running_threads:
    thrd.join()

#conn1 = sqlite3.connect('/home/app/db/newACCS.db')
#conn2 = sqlite3.connect('/home/app/db/oldACCS.db')

#t1 = tableinfo(conn1)
#t2 = tableinfo(conn2)

end = time.time() - start

print(ts)

if ts[0] == ts[1]:
    print("SAME")
else:
    print("NOT SAME")

print(end)