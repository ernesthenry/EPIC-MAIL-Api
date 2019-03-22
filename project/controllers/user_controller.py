#project/server/controllers
from flask import jsonify, request,json
from project.models.user import user_data, User, valid_credentials
from project.utilities.validation import user_validation
from project.utilities.helpers import generate_token

secret_key = environ.get("SECRET_KEY", "epicmail-reloaded")

class UserController:
    def signup_user(self):
        data = json.loads(request.data)
        if not data:
            return jsonify(
                {
                    "status": 400,
                    "error": "Empty Registration request. Please provide Registration data"
                    }), 400
        new_user ={
            "email": data.get("email"),
            "firstname": data.get("firstname"),
            "lastname": data.get("lastname"),
            "password": data.get("password")
            }
        email = data.get("email")
        firstname = data.get("firstname")
        already_user = [user for user in user_data if user.email ==
        email or user.firstname == firstname
        ]
        if already_user:
            return jsonify({"status": 409, "error": "User already exists"}), 409
        not_valid_user = user_validation(**new_user)
        if not_valid_user:
            return jsonify({"status": 400, "error": not_valid_user}), 400
        user = User(**new_user)
        user_data.append(user)
        return jsonify({
            "status": 201,
            "data": [
                {
                    "user": user.format_user_record(),
                    "success": " User registered Successfully"}
                    ],
                }
                ),201


    def login_user(self):
        login_credentials = json.loads(request.data)
        response = None
        if not login_credentials:
            return jsonify(
                {
                    "status": 400,
                    "error": "Empty Login request.Please provide login credentials"
            }), 400
        email = login_credentials.get("email")
        password = login_credentials.get("password")

        logged_in = is_valid_credentials(email,password)
        if logged_in:
            response = (
                    jsonify(
                        {
                            "status": 200,
                            "data": [
                                {
                                    "Token": generate_token(str(user._id)),
                                    "Success": "User logged in successfully"
                                }
                                ],
                                }
                                ),200,
                                )
        else:
            response = (
                jsonify({"error": "Wrong login credentials.", "status": 401}),
                401,
                )