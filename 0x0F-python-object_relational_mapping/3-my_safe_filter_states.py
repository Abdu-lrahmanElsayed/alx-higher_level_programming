#!/usr/bin/python3
"""This module takes in an argument and displays all values in the states
    where name matches the argument.
    safe from MySQL injections!"""
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
    query = "SELECT * FROM states WHERE BINARY name = %s"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
