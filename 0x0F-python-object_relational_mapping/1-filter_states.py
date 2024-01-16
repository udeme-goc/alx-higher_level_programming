#!/usr/bin/python3
"""Script that lists all states with a name starting with 'N' from the database
hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Get command line arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
            passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to get states starting with 'N', sorted by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
