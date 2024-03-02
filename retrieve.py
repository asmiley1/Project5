import sqlite3

# Connect to the database
conn = sqlite3.connect('FridayProj5 (1).db')

# Get a list of all tables in the database
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the tables
if tables:
    print("Tables in the database:")
    for table in tables:
        print(table[0])
else:
    print("No tables found in the database.")

# Close the connection
conn.close()