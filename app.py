from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat_handler():
    data = request.json
    response_payload = {
        "reply": "System online: Frequenz 44.2 Hz stabil.",
        "status": "CONNECTION_SUCCESSFUL"
    }
    return jsonify(response_payload)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

