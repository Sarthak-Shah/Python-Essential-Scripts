__author__: "sarthak shah"

"""
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and
flexibility of SQL.
SQLAlchemy provides a full suite of well known enterprise-level persistence patterns, designed for efficient and 
high-performing database access, adapted into a simple and Pythonic domain language.

Features:

1)SQLAlchemy is a tool that helps developers work with databases. It has two main parts: the Core and the ORM.

2) The Core lets developers write SQL code in Python, making it easier to interact with databases.

3) The ORM is a way to map objects in code to tables in a database. It helps developers work with databases as if they
 were just working with objects in code.

4) SQLAlchemy's philosophy is to allow developers to have full control over the design, structure, and naming conventions 
of both the object model and the relational schema. The ORM provides patterns to help developers build a custom 
mediation layer between the two.

5) SQLAlchemy encourages developers to use transactions, which ensure that changes to the database are consistent and 
complete. It also encourages developers to use bound parameters instead of literal values in SQL statements, which helps 
prevent security vulnerabilities.

6) Overall, SQLAlchemy aims to accommodate both the principles of object-oriented programming and the functionality of 
relational databases, providing developers with the flexibility to design and structure their databases in a way that 
works best for their specific needs.
 
"""

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Create a connection string
connection_string = 'oracle+cx_oracle://sarthakshah1920@gmail.com:helAPE2@host:port/service_name'

# Create an engine
engine = create_engine(connection_string)

# Define the table schema
metadata = MetaData()
my_table = Table('my_table', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String),
                  Column('age', Integer))

# Query the database
with engine.connect() as connection:
    query = my_table.select().where(my_table.c.age > 30)
    result = connection.execute(query)
    for row in result:
        print(row)
