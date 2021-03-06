#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
-
Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!)
-
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost
at port 3306
-
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT
                    # cities.id
                    cities.name
                    # states.name
                    FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    WHERE states.name LIKE BINARY %s""", (argv[4],))
    access = cursor.fetchall()
    x = []
    for iteration in access:
        x.append(iteration[0])
    print(", ".join(x))
