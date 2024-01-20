#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Get command line arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # Create a cursor object to interact with database
    cursor = db.cursor()

    # Execute the query to get all cities with state name, sorted by id
    query = """SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC"""
    cursor.execute(query)

    # Fetch all rows
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close cursor and database connection
    cursor.close()
    db.close
