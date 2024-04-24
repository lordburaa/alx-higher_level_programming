#!/usr/bin/python3
"""
creaet relationship
"""
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine =create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    metadata = MetaData(bind=engine)
    
    # create tables
    State.metadata.create_all(engine)
    City.metadata.create_all(engine)
    # create State table
    # city = City(1,"San Francisco")

    State.metadata.create_all(engine)
    City.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # instancee
    state = State(name="california")
    city = City(name="San Fransico", state_id=1)
    session.add(state)
    session.add(city)

    session.commit()
    
