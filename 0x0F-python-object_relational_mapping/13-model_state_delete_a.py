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

    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(uname, pas, db)
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    engine.connect()

    session = sessionmaker()
    local_session = session(bind=engine)

    del_all_a_states = local_session.query(State)\
        .filter(State.name.like("%a%")).all()

    for i in del_all_a_states:
        local_session.delete(i)
    local_session.commit()

# Coded by EnGentech
