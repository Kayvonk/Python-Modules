# 02_install_and_setup_sqlite.py
# 🛠️ Setting up SQLite with Python

import sqlite3

# Connect to a SQLite database file (it creates one if it doesn't exist)
conn = sqlite3.connect('my_database.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Print confirmation
print("Connected to SQLite database 'my_database.db'")

# Close the connection
conn.close()
