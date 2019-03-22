#project/utilities
from flask import jsonify, request
import jwt
from os import environ
from functools import wraps
from project.controllers.user_controller import users


secret_key = environ.get("SECRET_KEY", "epicmail-reloaded")


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()
        try:
            token = auth_headers[1]
            if not token:
                error = jsonify({'message': 'Token is missing'}), 403
            data = jwt.decode(token, secret_key)
            return f(*args, **kwargs)
        except IndexError:
            error = jsonify({
                "message": "Token does not exist",
                "authenticated": False
            }), 401
        except jwt.DecodeError:
            error = jsonify({
                "message": "Token Decode Failed!",
                "authenticated": False
            }), 401
        except jwt.ExpiredSignatureError:
            error = jsonify({
                'message': 'Expired token. Please Log In again.',
                'authenticated': False
            }), 401
        except jwt.InvalidTokenError:
            error = jsonify({
                'message': 'Invalid token. Please Log In again',
                'authenticated': False
            }), 401
        return error

    return _verify

def current_user_id():
    auth_headers = request.headers.get('Authorization', '').split()
    token = auth_headers[1]
    data = jwt.decode(token, secret_key)
    return data["user_id"]