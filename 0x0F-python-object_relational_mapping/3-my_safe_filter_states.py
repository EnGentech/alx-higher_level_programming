#!/usr/bin/python3
"""This program will list all states in the db"""

import MySQLdb
import sys

if __name__ == '__main__':
    name = sys.argv[1]
    pas = sys.argv[2]
    dbname = sys.argv[3]
    choice = sys.argv[4]

    mydb = MySQLdb.connect(host="localhost", port=3306,
                           user=name, passwd=pas, db=dbname)
    mycursor = mydb.cursor()

    command = "SELECT * FROM states WHERE BINARY name = %s\
    ORDER BY states.id ASC;"
    mycursor.execute(command, (choice, ))

    for state in mycursor:
        print(state)

    mycursor.close()
    mydb.close()

# Coded by EnGentech
