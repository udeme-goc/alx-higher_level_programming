#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
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
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to get all cities of the specified state, sorted by id
    query = """SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC"""

    cursor.execute(query, (state_name,))
    result = cursor.fetchall()

    # Extract city names from the result
    cities = [row[0] for row in result]

    # Print the list of cities separated by commas
    print(", ".join(cities))

    # Close cursor and database connection
    cursor.close()
    db.close()
