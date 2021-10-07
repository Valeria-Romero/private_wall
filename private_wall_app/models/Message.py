from flask import flash
from private_wall_app.config.MySQLConnection import connectToMySQL
from private_wall_app.models.User import User

class Message:
    def __init__(self, id, message_text, user_id):
        self.id = id
        self.message_text = message_text
        self.user_id = user_id

    @classmethod
    def add_new_message(cls, message_text, user_id):
        print(1)
        
        query = "INSERT INTO messages(message_text,user_id) VALUES (%(message_text)s, %(user_id)s);"
        data={
            "message_text": message_text,
            "user_id": user_id
        }
        print(data)
        result = connectToMySQL("private_wall_db").query_db(query, data)
        print(3)
        return result

    @classmethod
    def get_user_messages(cls,id):
        query = "SELECT users.first_name, messages.* FROM users LEFT JOIN messages ON users.id = messages.user_id WHERE messages.user_id = %(id)"

        data={
            "id": id
        }

        messages = connectToMySQL("private_wall_db").query_db(query, data)
        print(messages)
        return messages