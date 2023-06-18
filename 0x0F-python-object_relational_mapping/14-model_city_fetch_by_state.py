#!/usr/bin/python3
"""This code deals with creating a relationship
with states and cities using the join operator
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City

uname = sys.argv[1]
pas = sys.argv[2]
db = sys.argv[3]

url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
    .format(uname, pas, db)

if __name__ == "__main__":

    engine = create_engine(url)
    engine.connect()

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    city_session = session()

    all_table = city_session.query(State, City).join(State)\
        .order_by(City.id).all()

    for x, y in all_table:
        print("{}: ({}) {}".format(x.name, y.id, y.name))

# Coded by EnGentech
