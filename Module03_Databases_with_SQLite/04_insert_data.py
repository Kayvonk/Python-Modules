# 04_insert_data.py
# ➕ Insert data into the SQLite table

import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Insert some users into the users table
users = [
    ('Alice', 25),
    ('Bob', 30),
    ('Charlie', 22)
]

cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', users)

print(f"Inserted {cursor.rowcount} users into the database.")

conn.commit()
conn.close()
