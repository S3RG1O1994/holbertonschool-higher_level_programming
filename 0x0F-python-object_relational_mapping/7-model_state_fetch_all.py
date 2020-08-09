#!/usr/bin/python3
''' Lists all State objects from the database hbtn_0e_6_usa '''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    Uname = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(Uname, passwd, db))
    InstanceSession = sessionmaker(bind=engine)
    session = InstanceSession()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
