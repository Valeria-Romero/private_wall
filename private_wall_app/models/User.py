from flask import flash, session
import private_wall_app
from private_wall_app.config.MySQLConnection import connectToMySQL
import re

class User:
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.messages = []
    
    @classmethod
    def add_new_user(cls, new_user):
        query = "INSERT INTO users(first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s, %(password)s);"
        data={
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "email": new_user.email,
            "password": new_user.password
        }

        result = connectToMySQL("private_wall_db").query_db(query,data)
        return result


    @classmethod
    def validate_login(cls, login_information):

        query = "SELECT * FROM users WHERE email = %(email)s;"

        email={
            "email": login_information
        }

        result = connectToMySQL('private_wall_db').query_db(query,email)
        return result

    @classmethod
    def load_users_info(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('private_wall_db').query_db(query)

        users_information=[]
        for user in results:
            users_information.append(User(user['id'],user['first_name'],user['last_name'],user['email'],user['password']))
        return users_information

    @classmethod
    def load_users_info_not_in_session(cls, id):
        query = "SELECT * FROM users WHERE id != %(id)s"

        id={
            "id": id
        }

        results = connectToMySQL('private_wall_db').query_db(query, id)

        users_information_not_in_session=[]
        for user in results:
            users_information_not_in_session.append(User(user['id'],user['first_name'],user['last_name'],user['email'],user['password']))
        return users_information_not_in_session

    @classmethod
    def get_one(cls,data):
        query = "SELECT first_name FROM users WHERE id = %(id)s;"
        data = {
            "id": session['user_id'],
        }
        results = connectToMySQL('private_wall_db').query_db(query,data)
        return results

    @staticmethod
    def validate_registry( first_name, last_name, email,encrypted_password, password, password_confirmation):
        isValid = True
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        query = "SELECT * FROM users WHERE email = %(email)s;"
        emaildata = {
                "email" : email,
            }
        results = connectToMySQL('private_wall_db').query_db(query,emaildata)

        if len(results)>=1:
            flash("Email already registered")
            isValid = False

        if len( first_name ) < 2:
            flash( "First name must be at least 2 characters long" )
            isValid = False 

        if len( last_name ) < 2:
            flash( "Last name must be at least 2 characters long")
            isValid = False

        if not EMAIL_REGEX.match(email):
            flash("Invalid email, please write email in valid format")
            isValid = False

        if len(password) < 8:
            flash("Password must be at least 8 characters long")
            isValid = False

        if password != password_confirmation:
            flash("Passwords must match, try again")
            isValid = False
        return isValid

    