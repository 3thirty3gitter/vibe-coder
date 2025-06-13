from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/run', methods=['POST'])
def run_code():
    data = request.json
    prompt = data.get('prompt')
    return jsonify({"result": f"You sent: {prompt}"})

if __name__ == '__main__':
    app.run(debug=True)
