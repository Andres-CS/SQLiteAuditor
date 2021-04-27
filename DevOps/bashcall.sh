#!/bin/bash

COLOR='\033[0;33m'
NOCOLOR='\033[0m'

dbsource=/home/jarvis/Development/SQLiteAuditor/src
dbdestination=/home/app/db

echo "Welcome to SQLite Auditor"
echo -n "PLease input path of Database 1: "
read dbpath
echo -n -e "You inputed ${COLOR} $dbpath ${NOCOLOR}, is this correct [y/n]: "
read ans

if [ $ans == 'y' ]
then
    echo -e "docker run --mount type=bind,source=${COLOR}$dbpath${NOCOLOR},destination=${COLOR}$dbdestination${NOCOLOR} -it sq /bin/bash"
    docker run --mount type=bind,source=$dbpath,destination=$dbdestination -it sq /bin/bash
else
    echo "No Action"
fi 