from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb+srv://Satyajit:Satyajit123@cluster0.8c20nzh.mongodb.net/")
db = client["Details"]      # Database name
collection = db["Emails_password"]          # Collection name

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Insert into MongoDB
        collection.insert_one({
            "email": email,
            "password": password
        })

        print("Data inserted successfully!")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)