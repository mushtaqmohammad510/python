from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        'message': 'Hello from the backend!',
        'data': [1, 2, 3, 4, 5]
    })

@app.route('/')
def serve_frontend():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
