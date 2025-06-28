# 06_update_and_delete.py
# 🔄 Update and delete records in SQLite

import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Update age for user named 'Alice'
cursor.execute('UPDATE users SET age = ? WHERE name = ?', (26, 'Alice'))
print(f"Updated {cursor.rowcount} record(s).")

# Delete user named 'Bob'
cursor.execute('DELETE FROM users WHERE name = ?', ('Bob',))
print(f"Deleted {cursor.rowcount} record(s).")

conn.commit()

# Verify changes
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
print("Current users:")
for row in rows:
    print(row)

conn.close()
