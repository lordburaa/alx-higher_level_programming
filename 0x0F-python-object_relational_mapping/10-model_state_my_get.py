#!/usr/bin/python3
"""
Get a State
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    query = session.query(State).filter(State.name == argv[4]).first()
    if query is None:
        print("Not found")
    else:
        print("{0}".format(query.id))
