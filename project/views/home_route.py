from flask import Blueprint
from project import create_app
from project.controllers.home_controller import Home

app = create_app()

home_page = Home()
@app.route("/")
def first_page():
    return home_page.home()