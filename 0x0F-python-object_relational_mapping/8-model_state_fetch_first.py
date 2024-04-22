#!/usr/bin/python3
"""prints the first State object form the database"""

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import State, Base
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    query = session.query(State).first()
    if query is None:
        pass
    else:

        print("{}: {}".format(query.id, query.name))
