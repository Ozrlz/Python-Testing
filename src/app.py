from os import environ

from flask import Flask, jsonify

FLASK_PORT = environ.get('FLASK_PORT')

app = Flask(__name__)

@app.route('/')
def hello_wolrd():
    return jsonify({
            'message': 'Hello world c:'
        }
    )


if __name__ == '__main__':
    app.run(port=FLASK_PORT, host='0.0.0.0', debug=True)