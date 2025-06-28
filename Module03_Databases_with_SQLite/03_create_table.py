# 03_create_table.py
# 📋 Create a table in SQLite with Python

import sqlite3

# Connect to the database (creates file if needed)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create a table called 'users' with id, name, and age
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')

print("Table 'users' created (if it didn't exist).")

# Commit changes and close connection
conn.commit()
conn.close()
