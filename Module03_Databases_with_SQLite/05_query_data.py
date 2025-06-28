# 05_query_data.py
# 🔍 Query data from the SQLite database

import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Select all users from the table
cursor.execute('SELECT * FROM users')

rows = cursor.fetchall()

print("All users in the database:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

conn.close()
