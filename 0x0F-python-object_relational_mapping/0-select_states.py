#!/usr/bin/python3

import MySQLdb
import sys
if __name__ == '__main__':

    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    r = c.fetchall()

    for i in r:
        print(i)
