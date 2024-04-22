#!/usr/bin/python3
# create new tbales;


# if there is error in the requirement
# you can hange it column to mapped_collumn=> sqlalchemy.orm
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy import declarative_base
Base = declarative_base()


class State(Base):
    """ state class """

    __tablename__ = "states"
    id = Column(Integer, auto_generated, nullable=False)
    name = Column(String(128), nullabel=False)
