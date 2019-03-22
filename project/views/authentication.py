from project.views.app import app
from project.controllers.user_controller import UserController

u_controller=UserController()

@app.route("api/v1/auth/signup", methods=['POST'])
def new_user():
    return u_controller.signup_user()