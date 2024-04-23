#!/usr/bin/python3
"""
Deletes all STate object with name conaitng hte letter a
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    query = session.query(State).filter(State.name.contains('a')).all()
    for i in query:
        session.delete(i)
    session.commit()
    """
    session.delete(query)
    session.commit()
    session.close()
    """
