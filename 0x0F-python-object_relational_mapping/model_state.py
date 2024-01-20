#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base():
"""

# Import necessary modules
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()

# Define the State class representing the 'states' table
class State(Base):
    """State class inherits from Base"""

    # Specify the table name
    __tablename__ = 'states'

    # Define columns with their data types and constraints
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
