#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table at hbtn_0e_0_usa where name matched the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Get command line arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
            passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query with the user input sorted by id
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;" \
            .format(state_name)
    cursor.execute(query, (state_name,))

    # Fetch all rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
