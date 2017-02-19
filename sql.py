# sql.py - Create a SQLite3 table and populate it with data

import sqlite3

# create a new database if a database does not already exist
with sqlite3.connect("blog.db") as connection:

    # get a cursor object used to execute the SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE posts(title TEXT, post TEXT)""")

    # seed the database with dummy data
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')