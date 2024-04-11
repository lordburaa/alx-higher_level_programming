#!/usr/bin/python3
"""
Takes an Argument and display all values in the\
states tables of hbtn_0e_0_usa where name matche
the argument
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3], port=3306)
    db_c = db.cursor()
    # avoid the sql injection
    db_c.execute("SELECT * FROM states WHERE states.name='{}'\
            ORDER BY states.id ASC".format(sys.argv[4]))
    row_select = db_c.fetchall()
    for row in row_select:
        print(row)
