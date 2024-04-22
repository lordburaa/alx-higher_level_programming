#!/usr/bin/python3
"""
list all State object that contain the letter a from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    query = session.query(State).filter(State.name.like('%a%'))
    for row in query:
        print("{}: {}".format(row.id, row.name))
