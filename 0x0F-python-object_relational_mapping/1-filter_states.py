#!/usr/bin/python3
"""
script fileter
"""

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3],
                         port=3306)
    db_c = db.cursor()
    db_c.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
    row_select = db_c.fetchall()

    for row in row_select:
        print(row)
