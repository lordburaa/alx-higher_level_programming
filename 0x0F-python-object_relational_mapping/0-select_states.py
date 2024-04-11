#!/usr/bin/python3

import MySQLdb
import sys

db = MySQLdb.connect(password="997788", database="hbtn_0e_0_usa")
c = db.cursor()
c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
r = c.fetchall()

for i in r:
    print(i)
