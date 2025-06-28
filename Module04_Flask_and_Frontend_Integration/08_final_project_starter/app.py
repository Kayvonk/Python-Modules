from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'final_project.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    # Example: create table for moods (or change to any project concept)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS moods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mood TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/moods', methods=['GET', 'POST'])
def moods():
    if request.method == 'POST':
        data = request.get_json()
        mood = data.get('mood')
        if not mood:
            return jsonify({'error': 'Mood is required'}), 400
        conn = get_db_connection()
        conn.execute('INSERT INTO moods (mood) VALUES (?)', (mood,))
        conn.commit()
        conn.close()
        return jsonify({'message': f'Mood "{mood}" saved!'})
    else:
        conn = get_db_connection()
        moods = conn.execute('SELECT * FROM moods').fetchall()
        conn.close()
        return jsonify([dict(m) for m in moods])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
