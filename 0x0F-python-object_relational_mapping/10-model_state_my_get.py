#!/usr/bin/python3
"""This code deals with sqlalchemy
basically written to connect with our mysqldb
get all the list of states present in there
and list them in ascending order to out python snippet"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    uname = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]
    choice = sys.argv[4]

    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(uname, pas, db)
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    engine.connect()

    session = sessionmaker()
    local_session = session(bind=engine)

    f_n = local_session.query(State)\
        .filter(State.name == choice).first()

    if f_n:
        print(f_n.id)
    else:
        print("Not found")

# Coded by EnGentech
