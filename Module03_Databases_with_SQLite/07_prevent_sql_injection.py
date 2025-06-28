# 07_prevent_sql_injection.py
# 🛡️ Prevent SQL Injection with Parameterized Queries

import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Unsafe way: directly inserting user input (DON'T DO THIS)
user_input = "Robert'); DROP TABLE users;--"

# Unsafe example (commented out to avoid harm):
# cursor.execute(f"INSERT INTO users (name, age) VALUES ('{user_input}', 30)")

# Safe way: use parameterized queries with placeholders
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (user_input, 30))

conn.commit()

# Check if users table still exists and data was inserted safely
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Users in the database after safe insert:")
for row in rows:
    print(row)

conn.close()
