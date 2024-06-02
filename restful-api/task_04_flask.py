#!/usr/bin/python3

"""Module for RESTful API exercises"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route('/')
def home():
    """Root URL returns a welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Return status"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Return the user object"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user"""
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    user_data = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run(debug=True)
