#!/usr/bin/python3
"""This module takes in an argument and displays all values in the states
    where name matches the argument."""
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
            "SELECT * FROM states WHERE BINARY name = '{}'".format(
                sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
