#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Adde the new state to the session
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Display the new states.id after creation
    print(new_state.id)

    # Close the session
    session.close()
