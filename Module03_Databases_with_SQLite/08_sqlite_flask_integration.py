# 08_sqlite_flask_integration.py
# 🔗 Integrate SQLite with Flask for persistent data

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'my_database.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # allows dict-like access
    return conn

@app.route('/users')
def users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()

    users_list = [dict(user) for user in users]
    return jsonify(users_list)

if __name__ == '__main__':
    app.run(debug=True)
