#!/usr/bin/python3
# Once again, write a script that takes in arguments and
# displays all values in the states table of hbtn_0e_0_usa
# where name matches the argument.
# But this time, write one that is safe from MySQL injections!
# -
# Your script should take 4 arguments: mysql username, mysql password,
# database name and state name searched (safe from MySQL injection)
# -
# You must use the module MySQLdb (import MySQLdb)
# Your script should connect to a MySQL server running on
# localhost at port 3306
# -
# Results must be sorted in ascending order by states.id
# Results must be displayed as they are in the example below
# Your code should not be executed when imported

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s;", (argv[4],))
    # passing the command as an immutable tuple
    # makes injection more difficult
    access = cursor.fetchall()
    for iteration in access:
        print(iteration)