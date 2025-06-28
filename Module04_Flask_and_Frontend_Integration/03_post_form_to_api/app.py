from flask import Flask, request, jsonify

app = Flask(__name__)
moods = []

@app.route('/moods', methods=['POST'])
def add_mood():
    data = request.get_json()
    mood = data.get('mood')
    if not mood:
        return jsonify({'error': 'Mood is required'}), 400
    moods.append(mood)
    return jsonify({'message': f'Mood "{mood}" added!'})

if __name__ == '__main__':
    app.run(debug=True)
