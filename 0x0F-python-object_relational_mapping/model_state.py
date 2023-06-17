#!/usr/bin/python3
"""This page begins the use of sqlalchemy"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
"""this file begins the usage of sqlalchemy"""

url = "mysql+mysqldb://root:admin8634@localhost/hbtn_0e_6_usa"
engine = create_engine(url)
connection = engine.connect()

Base = declarative_base()


class State(Base):
    """A class definition inherited from Base in sqlalchemy"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)

# Coded by EnGentech
