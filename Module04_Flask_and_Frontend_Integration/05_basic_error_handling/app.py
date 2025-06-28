from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def get_data():
    # Simulate an error by returning 500 status sometimes
    from random import randint
    if randint(1, 3) == 1:
        return jsonify({'error': 'Random server error occurred'}), 500
    return jsonify({'message': 'Success!'})

if __name__ == '__main__':
    app.run(debug=True)
