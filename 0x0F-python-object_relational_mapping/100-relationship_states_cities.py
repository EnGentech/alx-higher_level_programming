#!/usr/bin/python3
"""In this advanced tasks, we deal more with relationship
on how a table should relate with each other
using the available resources on sqlalchemy"""

import sys
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City

if __name__ == "__main__":
    uname = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]

    url = "mysql+mysqldb://{}:{}@localhost:3306/{}" \
        .format(uname, pas, db)

    engine = create_engine(url)
    engine.connect()

    Base.metadata.create_all(engine)

    session = sessionmaker()(bind=engine)

    new_City = City(name="San Francisco")
    new = State(name="California", relate=new_City)

    session.commit()

# Coded be EnGentech
