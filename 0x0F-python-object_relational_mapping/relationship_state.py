#!/usr/bin/python3
"""This page begins the use of sqlalchemy"""

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String
from relationship_city import City

Base = declarative_base()


class State(Base):
    """A class definition inherited from Base in sqlalchemy"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade='all, delete')

# Coded by EnGentech
