#!/bin/bash

mkdir pg
cd pg
sudo apt-get install build-essential libreadline-dev zlib1g-dev flex bison -y
sudo apt install postgresql-server-dev-all -y

wget https://ftp.postgresql.org/pub/source/v15.1/postgresql-15.1.tar.gz && tar -xvf postgresql-15.1.tar.gz && rm -f postgresql-15.1.tar.gz
cd postgresql-15.1

./configure --enable-debug --enable-cassert --prefix=$(pwd) CFLAGS="-ggdb -Og -fno-omit-frame-pointer"
make install

bin/initdb -D postgres

bin/pg_ctl -D postgres -l logfile start

sleep 5

bin/psql -d postgres -c "CREATE USER postgres WITH PASSWORD '12345';"

bin/psql -d postgres -c "ALTER USER postgres WITH SUPERUSER;"

bin/psql -d postgres -c "\du"