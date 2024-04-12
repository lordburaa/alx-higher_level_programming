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
    db_c = db.cursor()
    db_c.execute("SELECT c.name FROM states s JOIN
                  cities c ON s.id=c.state_id
                  WHERE s.name= %(name)s", {"name": sys.argv[4]})
    row = db_c.fetchone()
    while True:
        if row is None:
            break
        else:
            for i in row:
                print(i, end="")
        row = db_c.fetchone()
        if row is not None:
            print(", ", end="")
    print()
