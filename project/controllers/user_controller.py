#project/server/controllers
from flask import jsonify, request,json, current_app
from project.models.user import user_data, User
from project.utilities.validation import user_validation
import jwt
from os import environ
from datetime import datetime, timedelta
from functools import wraps

secret_key = environ.get("SECRET_KEY", "epicmail-reloaded")

class UserController:
    def signup_user(self):
        """Api endpoint to Register"""
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