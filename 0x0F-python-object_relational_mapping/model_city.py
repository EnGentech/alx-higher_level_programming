#!/usr/bin/python3
"""This is the beginning part of create
a different class that will populate cities
on the database newly created"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    """Class definition of City"""
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True,\
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))

# Coded by EnGentech
