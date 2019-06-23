import sys
import sqlite3 as sql
import numpy as np

database = 'mcqas.db'

def enter_tst(tablename, username, itemname, action, lot, price):   #{
    con = sql.connect(database)  # connect to database

    with con:
        cur = con.cursor()
        try:
            cmd = 'INSERT INTO {} (username, order_item, order_action, order_lot, order_price) VALUES (?, ?, ?, ?, ?)'.format(tablename)
            print('\t', cmd)    # for debugging purpose
            cur.execute(cmd, [username, itemname, action.upper(), lot, price])
        except:
            print('\nsomething is wrong in insertion .... with {} {} {} {} {} {}'.format(tablename, username, itemname, action, lot, price))
            con.rollback()
    con.close()
#}

def retrieve_tst(tablename, username, action):  #{
    con = sql.connect(database)  # connect to database

    with con:
        cur = con.cursor()
        cur.execute("""SELECT order_item, order_lot, order_price, create_time
                       FROM Transactions WHERE (username =? AND order_action =?)""", [username, action.upper()])
        found = cur.fetchall()
    con.close()                          
    return (found)
#}
