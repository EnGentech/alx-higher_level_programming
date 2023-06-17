#!/usr/bin/python3
"""This program will list all states in the db"""

import MySQLdb
import sys

if __name__ == '__main__':
    name = sys.argv[1]
    pas = sys.argv[2]
    dbname = sys.argv[3]

    mydb = MySQLdb.connect(host="localhost", port=3306,
                           user=name, passwd=pas, db=dbname)
    mycursor = mydb.cursor()

    command = "SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id ASC;"
    mycursor.execute(command)

    for cities in mycursor:
        print(cities)

    mycursor.close()
    mydb.close()

# Coded by EnGentech
