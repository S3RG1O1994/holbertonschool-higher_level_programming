#!/usr/bin/python3
'''
    script that lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa
'''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, db_name))
    init_session = sessionmaker(bind=engine)
    conection = init_session()
    query = conection.query(State).order_by(State.id)
    for state in query:
        if 'a' in state.name:
            print('{}: {}'.format(state.id, state.name))
    conection.close()
