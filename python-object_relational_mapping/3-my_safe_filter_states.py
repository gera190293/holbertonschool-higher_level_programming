#!/usr/bin/python3
"""
Script that lists all values in the `states` table of `hbtn_0e_0_usa`
where `name` matches the argument `state name searched`
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    searched_name = sys.argv[4]

    db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                (searched_name, ))
    rows = cur.fetchall()

    for row in rows:
        print(row)
