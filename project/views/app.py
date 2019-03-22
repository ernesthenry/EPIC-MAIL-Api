from flask import Flask, jsonify, request
from project.controllers.home import Home

app=Flask(__name__)

home_page = Home()
@app.route("/")
def home():
    return home_page.home_route()