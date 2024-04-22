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
    name = argv[4]
    session = Session(bind=engine)
    query = session.query(State).filter(State.name == name).all()
    if len(query) == 0:
        print("Not found")
    else:
        print(query[1].id)
