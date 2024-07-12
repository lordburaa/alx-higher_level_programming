#!/usr/bin/python3
"""
script that takes in the name of state as an
argument and lists cities of that ste usgin
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3], port=3306)

    cu = db.cursor()
    try:
        cu.execute('SELECT c.name FROM cities c JOIN states s on s.id=c.state_id s.name="{}"'.format(sys.argv[4]))

        print(cu.fetchall())
    except:
        print("Error found ")
