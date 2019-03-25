from datetime import datetime
user_messages = []
message_id = 1


class Message:
    """class to contain all message objects"""
    def __init__(self, **kwargs):
        global message_id
        self.message_id = message_id
        userid = len(user_messages)+1
        self.subject = kwargs["subject"]
        self.message = kwargs["message"]
        self.sender_status = kwargs["sender_status"]
        self.reciever_status = "unread"
        self.parent_message_id = kwargs["parent_message_id"]
        self.receiver = kwargs["receiver"]
        self.created_on = str(datetime.now)
        message_id += 1
