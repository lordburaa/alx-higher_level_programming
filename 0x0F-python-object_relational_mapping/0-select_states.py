#!/usr/bin/python3
"""
This script liss all states from the databsee
"""


import MySQLdb
import sys


if __name__ == '__main__':
    """ doc checked """
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    r = c.fetchall()

    for row in r:
        print(row)
