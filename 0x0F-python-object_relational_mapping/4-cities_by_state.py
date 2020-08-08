#!/usr/bin/python3
''' Script for query all states in database.
'''

import MySQLdb
import sys

if __name__ == '__main__':
    Uname = sys.argv[1]
    Upasswd = sys.argv[2]
    DB = sys.argv[3]
    db = MySQLdb.connect(user=Uname, passwd=Upasswd, db=DB)
    pointer = db.cursor()
    pointer.execute('SELECT cities FROM states ORDER BY cities.id;')
    row = pointer.fetchall()
    for items in row:
        print(items)
    pointer.close()
    db.close()
