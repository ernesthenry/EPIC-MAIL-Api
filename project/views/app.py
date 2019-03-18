from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route("/")
def home():
    """A welcoming route to my api"""
    return jsonify({
        'message': 'Welcome to Ernest\'s EPIC MAIL app.',
        'status': '200'
    }), 200