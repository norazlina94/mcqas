import sys
import sqlite3
import numpy as np

if len(sys.argv) < 2:
    print('Usage: dbsetup [dbname]')
    sys.exit()
database = sys.argv[1] + '.db'


#connect to db
db = sqlite3.connect(database)

#setup cursor
cursor = db.cursor()

#create a Transactions table
tablename = 'Transactions'
print('\n ... drop table <{tn}> if it exists'.format(tn=tablename))
cursor.execute("DROP TABLE IF EXISTS {tn}".format(tn=tablename))

print(' ... create a table {tn}'.format(tn=tablename))
sql = """CREATE TABLE {tn} (
            ticket_id       integer             not null    default 0 PRIMARY KEY AUTOINCREMENT,
            username        varchar(32)         not null    default '',
            status          varchar(1)          not null    default '-',
            order_item      varchar(32)         not null    default '',
            order_action    varchar(8)          not null    default 'BUY',
            order_lot       unsigned integer    not null    default 0,
            order_price     float               not null    default 0,
            create_time     datetime            null
      );""".format(tn=tablename)
print('\n', sql)
cursor.execute(sql)

#insert to table
print('\ntry to insert 2 records to table {tn}'.format(tn=tablename))
try:
    cmd = 'INSERT INTO {} (username, order_item, order_action, order_lot, order_price) VALUES (?, ?, ?, ?, ?)'.format(tablename)
    print('\t', cmd)
    cursor.execute(cmd, ['alan', 'mango', 'SELL', 3, 10.56])
    cursor.execute(cmd, ['lina', 'apple', 'BUY', 5, 11.23])
    db.commit()
except:     
    print('\nsomething is wrong in insertion ....')
    db.rollback()

#show table
print('\nselect all from {tn}'.format(tn=tablename))
cursor.execute('SELECT * FROM {tn}'.format(tn=tablename))
print(np.array(cursor.fetchall()))


#create a Users table
tablename = 'Users'
print('\n ... drop table <{tn}> if it exists'.format(tn=tablename))
cursor.execute("DROP TABLE IF EXISTS {tn}".format(tn=tablename))

print(' ... create a table {tn}'.format(tn=tablename))
sql = """CREATE TABLE {tn} (
            id		    integer		not null    default 0 PRIMARY KEY AUTOINCREMENT,
            username	varchar(32)	not null    default '',
            password    varchar(32) not null    default '',
            emailaddr   varchar(32) not null    default ''
      );""".format(tn=tablename)
print('\n', sql)
cursor.execute(sql)

#insert to table
print('\ntry to insert 2 records to table {tn}'.format(tn=tablename))
try:
    cmd = 'INSERT INTO {} (username, password) VALUES (?, ?)'.format(tablename)
    print('\t', cmd)
    print(cmd)
    cursor.execute(cmd, ('alan', '00000000'))
    cursor.execute(cmd, ('lina', '12345678'))
    db.commit()
except:     
    print('\nsomething is wrong in insertion ....')
    db.rollback()

#create a Users table
tablename = 'quotes'
print('\n ... drop table <{tn}> if it exists'.format(tn=tablename))
cursor.execute("DROP TABLE IF EXISTS {tn}".format(tn=tablename))

print(' ... create a table {tn}'.format(tn=tablename))
sql = """CREATE TABLE {tn} (
            id          integer     not null    default 0 PRIMARY KEY AUTOINCREMENT,
            name        varchar(32) not null    default '',
            company     varchar(32) not null    default '',
            phone_num   integer(32) not null    default '',
            details     integer(32) not null    default ''

      );""".format(tn=tablename)
print('\n', sql)
cursor.execute(sql)

#show table
print('\nselect all from {tn}'.format(tn=tablename))
cursor.execute('SELECT * FROM {tn}'.format(tn=tablename))
print(np.array(cursor.fetchall()))

db.close()
