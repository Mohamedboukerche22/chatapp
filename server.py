from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
app = Flask(__name__)
CORS(app)
DB_FILE = "messages.json"
def load_messages():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []
def save_messages(messages):
    with open(DB_FILE, "w") as f:
        json.dump(messages, f)

@app.route("/get", methods=["GET"])
def get_messages():
    return jsonify(load_messages())
@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    message = data.get("message")
    messages = load_messages()
    messages.append({"message": message})
    save_messages(messages)
    return jsonify({"status": "ok"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
