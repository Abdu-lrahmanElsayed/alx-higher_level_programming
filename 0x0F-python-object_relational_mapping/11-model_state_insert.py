#!/usr/bin/python3
"""a script that adds the State object “Louisiana” to the database"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    newstate = State(name='Louisiana')
    session.add(newstate)
    session.commit()
    print("{}".format(newstate.id))
