from flask import Flask, request, jsonify
from guesslang import Guess

app = Flask(__name__)

def programming_language_recognition(code: str) -> str:
    guess = Guess()

    language_name = guess.language_name(code)
    if language_name is not None:
        print('Language recognized -> ' + language_name)
        if language_name == 'Batchfile':
            return 'shell'
        return language_name.lower()

    return 'plaintext'


@app.route('/api/v1/recognize', methods=['POST'])
def create_resource():

    data = request.json

    response = {
        'status': 'success',
        'programming_language': programming_language_recognition(data['code'])
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
