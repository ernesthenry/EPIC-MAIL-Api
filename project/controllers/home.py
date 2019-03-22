from flask import jsonify
class Home:
    def __init__(self):
        pass
    def home_route(self):
        """A welcoming route to my api"""
        return jsonify({
            'data': 'Welcome to Ernest\'s EPIC MAIL app.',
                'status': 200
                }), 200