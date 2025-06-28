from flask import Flask, jsonify

app = Flask(__name__)
moods = ["happy", "excited", "tired"]

@app.route('/moods')
def get_moods():
    return jsonify(moods)

if __name__ == '__main__':
    app.run(debug=True)
