#!/usr/bin/python3
"""
Script that lists all State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    engine = create_engine(
       'mysql+mysqldb://{}:{}@localhost/{}'.format(
           sys.argv[1], sys.argv[2], sys.argv[3]
       ),
       pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the given state name
    state = session.query(State).filter_by(name=state_name).first()

    # Display the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
