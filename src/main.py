import sqlite3, threading, time

from getinfo import *

#TIME SCRIPT START 
start = time.time()

# ------- INIT CONFIG -------

num_threads = 2
dbpahts=['/home/app/db/test/newACCS.db','/home/app/db/test/testACCS.db']
running_threads = list()
ts = list() #HOLDS TABLE INFO

# ---------------------------

for i in range(num_threads):
    name_th = "Thread_"+str(i)
    thread = threading.Thread(target=modtime, name=name_th, args=(dbpahts[i],ts))
    running_threads.append(thread)
    thread.start()


for thrd in running_threads:
    thrd.join()


#TIME SCRIPT ENDS
end = time.time() - start

print(ts)

print()
if ts[0] == ts[1]:
    print("SAME")
else:
    print("NOT SAME")

print(end)