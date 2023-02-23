import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='username', password='password',
                              host='host', database='database')

# Create a cursor
cursor = cnx.cursor()

# Execute the SELECT statement
query = "SELECT * FROM table"
cursor.execute(query)

# Fetch all rows in the active set
rows = cursor.fetchall()

# Iterate through the active set
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()
