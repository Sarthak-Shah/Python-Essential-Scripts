"""
__author__ : "sarthak shah"
"""
"""
python can connect to DBMS to retrieve and manipulate data.

1) sqlite (locally stored database): best substitute for serialisation. Email/send data over network easily.
light application or mobile application
---> SQLite is a C library that provides lightweighted db that does not require a separate server process
and also allows accessing the db using non-standard variant of the SQL.

procedure:
    1) you need to import the package
    2) you need to make the connection. It connectes with RAM based file *database file* locally stored.
    3) cursor ---> execute SQL statements.

2) serverbase ----> mysql

XAMPP apache + mariadb + php ..
"""

import sqlite3


# sqlite3 is dynamic


def sqliteMemory():
    """
    in RAM
    """
    # Opens a connection to the SQLite database file database. You can use ":memory:" to open a database connection to a
    # database that resides in RAM instead of on disk.
    try:
        # con = sqlite3.connect("demo.db")
        con = sqlite3.connect(":memory:")
        cur = con.cursor()  # function within connecten.
        cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")  # Run the whole thing in RAM
        # q mark notation]
        # define list of tuple pairs containing row data for executemany
        alist_of_movies = [('Terminator', 1998, 9), ('Matrix 2', 2002, 8.5), ('John wick', 2018, 6.7),
                           ("the rock", 2000, 7.8)]
        cur.executemany('''insert into movie values (?, ?, ?)''', alist_of_movies)
        cur.execute("insert into movie values ('RRR', 2022, 8.7)")

        print("This is in memory (RAM) sqlite db file creation and usage example ! ")
        res = cur.execute("select * from movie")
        print(res.fetchall())
    except Exception as e:
        print(e)


def sqliteDisk():
    """
    in disk
    """
    # Opens a connection to the SQLite database file database. You can use ":memory:" to open a database connection to a
    # database that resides in RAM instead of on disk.
    try:
        # con = sqlite3.connect("demo.db")
        con = sqlite3.connect("movies.db")
        cur = con.cursor()  # function within connecten.
        cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")  # Run the whole thing in RAM
        # q mark notation
        # define list of tuple pairs containing row data for executemany
        alist_of_movies = [('Terminator', 1998, 9), ('Matrix 2', 2002, 8.5), ('John wick', 2018, 6.7),
                           ("the rock", 2000, 7.8)]
        cur.executemany('''insert into movie values (?, ?, ?)''', alist_of_movies)
        cur.execute("insert into movie values ('RRR', 2022, 8.7)")
        # res = cur.execute("select * from movie")
        # print(res.fetchall())

        con.commit()
        con.close()
    except Exception as e:
        print(e)


def read_SQLite_from_pandas():
    import pandas as pd
    # create a connection to the database
    conn = sqlite3.connect('movies.db')
    # read data from the table using pandas
    df = pd.read_sql_query('SELECT * FROM movie', conn)
    # close the database connection
    conn.close()
    # view the data using pandas
    print("\nThis is sqlite db file loaded from disk named movies.db and showing data with pandas\n")
    print(df.head())


sqliteDisk()
sqliteMemory()
read_SQLite_from_pandas()
