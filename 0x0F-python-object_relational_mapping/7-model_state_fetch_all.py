#!/usr/bin/python3
""" write script that liss all stae object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    session = Session(bind=engine)
    query = session.query(State).order_by(State.id)
    for _row in query:
        print("{}: {}".format(_row.id, _row.name))
