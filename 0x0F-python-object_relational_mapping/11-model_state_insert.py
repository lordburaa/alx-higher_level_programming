#!/usr/bin/python3
"""
add State object ot the dtabase
"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys. argv[3]))
    session = Session(bind=engine)
    query = State(name="Louisiana")
    # adding name object
    session.add(query)
    # object permanently added
    session.commit()
    print(query.id)
