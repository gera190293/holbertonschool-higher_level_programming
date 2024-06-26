#!/usr/bin/python3
"""
Script that lists all `State` objects that contain
the letter `a` from the database `hbtn_0e_6_usa`
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from model_state import Base, State


if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': mySQL_u, 'password': mySQL_p, 'database': db_name}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    q = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for instance in q:
        print("{}: {}".format(instance.id, instance.name))
