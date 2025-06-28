from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'todo.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    description = data.get('description')
    if not description:
        return jsonify({'error': 'Description is required'}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (description, completed) VALUES (?, 0)', (description,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task added'}), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
