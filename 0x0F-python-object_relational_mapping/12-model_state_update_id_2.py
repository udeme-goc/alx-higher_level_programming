#!/usr/bin/python3
"""
Script that changes the nameof a State object from the database hbtn_0e_6_usa
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

    # Get the State object with id=2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Check if the state exists
    if state_to_update:
        # Update the name to "New Mexico"
        state_to_update.name = 'New Mexico'

        # Commit the changes to the database
        session.commit()

    # Close the session
    session.close()
