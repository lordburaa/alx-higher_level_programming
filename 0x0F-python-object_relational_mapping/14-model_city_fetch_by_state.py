#!/usr/bin/python3
"""
prints all city object from the databse
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
from model_state import State, Base
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    query = session.query(State, City).join(City)
    for i in query:
        print("{}: ({}) {}".format(i[0].name, i[0].id, i[1].name))
