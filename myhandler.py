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

def enter_tst1(tablename, username, count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,
unit1,unit2,unit3,unit4,unit5,unit6,unit7,unit8,unit9,unit10,unit11,unit12):   #{
    con = sql.connect(database)  # connect to database

    with con:
        cur = con.cursor()
        try:
            cmd = 'INSERT INTO {} (username, count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,unit1,unit2,unit3,unit4,unit5,unit6,unit7,unit8,unit9,unit10,unit11,unit12) VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'.format(tablename)
            print('\t', cmd)    # for debugging purpose
            cur.execute(cmd, [username, count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,unit1,unit2,unit3,unit4,unit5,unit6,unit7,unit8,unit9,unit10,unit11,unit12])
        except:
            print('\nsomething is wrong in insertion .... with {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(tablename, username, count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,unit1,unit2,unit3,unit4,unit5,unit6,unit7,unit8,unit9,unit10,unit11,unit12))
            con.rollback()
    con.close()
#}
def retrieve_tst1(tablename, username, count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,
unit1,unit2,unit3,unit4,unit5,unit6,unit7,unit8,unit9,unit10,unit11,unit12):  #{
    con = sql.connect(database)  # connect to database

    with con:
        cur = con.cursor()
        cur.execute("""SELECT count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,
                    unit1,unit2,unit3,unit4,unit5,unit6,unit7,unit8,unit9,unit10,unit11,unit12
                       FROM eblooffilm WHERE (username =?)""", [username,])
        found = cur.fetchall()
    con.close()                          
    return (found)
#}