# 09_module_review.py
# 📚 Module 3 Review: Test your knowledge of databases and SQL with Python

print("1. What SQL command is used to create a table?")
print("Answer: CREATE TABLE")

print("\n2. How do you insert data safely to prevent SQL injection?")
print("Answer: Use parameterized queries with placeholders like '?'")

print("\n3. What Python module do we use to work with SQLite?")
print("Answer: sqlite3")

print("\n4. How do you connect Flask to an SQLite database?")
print("Answer: Use sqlite3.connect() inside Flask route functions")

print("\n5. What HTTP methods did we use to create, read, update, and delete in Flask?")
print("Answer: POST (create), GET (read), PUT (update), DELETE (delete)")

print("\n6. What does the commit() method do in SQLite?")
print("Answer: It saves changes to the database.")

print("\n7. How can you fetch all rows from a SQLite query?")
print("Answer: Using cursor.fetchall()")

print("\nBonus Challenge:")
print("Write a simple Flask route that returns all rows from a 'users' table in JSON format.")

print("""
@app.route('/users')
def get_users():
    conn = sqlite3.connect('my_database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])
""")

print("\nGreat job reviewing! Ready for the mini project?")

