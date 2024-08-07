#!/usr/bin/python3
"""that prints all City objects from the database hbtn_0e_14_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from model_city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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
    query = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id)
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
