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
    query = 'SELECT * FROM states WHERE name LIKE"N%"ORDER BY states.id;'
    pointer.execute(query)
    row = pointer.fetchall()
    for items in row:
        print(items)
    pointer.close()
    db.close()
