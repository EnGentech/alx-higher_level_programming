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

    command = "SELECT c.name FROM cities AS c" \
              " inner join states AS s on " \
              "c.state_id = s.id where s.name = %s ORDER BY c.id ASC;"
    mycursor.execute(command, (choice, ))

    cities = mycursor.fetchall()

    lst = []
    for city in cities:
        lst.append(city[0])

    print(", ".join(lst))
    mycursor.close()
    mydb.close()

# Coded by EnGentech
