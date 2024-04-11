#!/usr/bin/python3

import sys
from sqlalchemy import MetaData, Table, create_engine, select


engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
conn = engine.connect()
metadata = MetaData()
metadata.reflect(bind=engine)

table_name = 'states'

table = Table(table_name, metadata)
# grap query from the table
q = table.select()
r = conn.execute(table.select())

print(r)
