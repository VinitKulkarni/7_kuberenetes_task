from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
client = pymongo.MongoClient(mongo_uri)
db = client.testDB
collection = db['users-collection']

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid data"}), 400

    collection.insert_one({
        "username": data["username"],
        "password": data["password"]
    })

    return jsonify({"message": "User data stored successfully"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
