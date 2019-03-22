from project.controllers.user_controller import UserController
from flask import Blueprint

user_blueprint = Blueprint("user_blueprint", __name__)

u_controller=UserController()

@user_blueprint.route("/auth/signup", methods=['POST'])
def register_user():
    return u_controller.signup_user()
