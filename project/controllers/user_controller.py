#project/server/controllers
from flask import jsonify, request
from project.models.user import user_data, User
class UserController:
    def __init__(self):
        pass
    def signup_user(self):
        data = request.get_json()

        user_email = data.get(email)
        Firstname = data.get(firstname)
        Lastname = data.get(lastname)
        Password = data.get(password)

        if not user_email or not Firstname or not Lastname \
        or not Password:
            return jsonify({
                "Error": "Required field is missing"
            }), 400
        new_user = User(
    		email = user_email,  firstname= Firstname, lastname = Lastname, password = Password
            )

        user_data.append(
            new_user.format_user_record()
            )
            
        if len(user_data) == 0:
            return jsonify({
        "status": 200, 
         "Error": "No user yet"
         }), 200
        return jsonify({
        "data": new_user.format_user_record,  
        "status": 201,            
        "Message": "User created successfully" 
        }), 201