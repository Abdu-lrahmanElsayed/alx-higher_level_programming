#!/usr/bin/python3
"""This module lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cur = db.cursor()
    cur.execute(
            "SELECT cities.id, cities.name, states.name FROM cities, states "
            + "WHERE cities.state_id = states.id"
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
