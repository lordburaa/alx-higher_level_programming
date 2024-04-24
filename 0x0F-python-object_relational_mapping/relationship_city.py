#!/usr/bin/python3
"""
create new tbales;
if there is error in the requirement
you can hange it column to mapped_collumn=> sqlalchemy.orm
"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import State
Base = declarative_base()


class City(Base):
    """ City class """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))
    state = relationship(State, backref="cities")
