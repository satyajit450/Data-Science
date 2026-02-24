from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client.mydatabase        # database name
users = db.users              # collection name

@app.route("/")
def home():
    return "Flask + MongoDB connected"

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    users.insert_one({
        "name": data["name"],
        "age": data["age"]
    })
    return jsonify({"message": "User added successfully"})

@app.route("/users", methods=["GET"])
def get_users():
    result = []
    for user in users.find({}, {"_id": 0}):
        result.append(user)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
