from flask import render_template, request, redirect, session
from private_wall_app import app
from private_wall_app.models.Message import Message
from private_wall_app.models.User import User
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

@app.route("/", methods=['GET'])
def load_main_page():
    return render_template("home.html")

@app.route("/user/add", methods=['POST'])
def add_new_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    encrypted_password = bcrypt.generate_password_hash(password)
    password_confirmation = request.form['confirm_password']


    if User.validate_registry(first_name, last_name, email, encrypted_password, password, password_confirmation):
        new_user = User(id,first_name, last_name, email, encrypted_password)
        result = User.add_new_user(new_user)
        return redirect("/")
    else:
        print("something went wrong")
        return redirect("/")

@app.route("/login", methods=['POST'])
def login_validation():
    email = request.form['login_email']
    password = request.form['login_password']

    result = User.validate_login(email)
    Message.get_user_messages(result[0]['id'])
    database_password = result[0]['password']
    if result[0]['email'] == email:
        if bcrypt.check_password_hash(database_password, password):
            session.clear()
            data={
                'user_id':result[0]['id'],
                'user_first_name': result[0]['first_name']
            }
            session['user_id'] = result[0]['id']
            users_data = User.load_users_info_not_in_session(result[0]['id'])
            return render_template("wall.html", data=data, users_data=users_data)
        else:
            print("Not working")
            flash("Wrong password, try again")

    return redirect("/")

@app.route("/logout", methods=['GET'])
def logout_session():
    session.clear()
    return redirect("/")


@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user_info = User.get_one(session['user_id'])
    print(user_info)
    data = {
        "id": session['user_id'],
        "user_first_name": user_info[0]['first_name']
    }
    
    users_data = User.load_users_info_not_in_session(session['user_id'])
    return render_template("wall.html", data=data, users_data=users_data, user_info=user_info)

@app.route("/send/message", methods=['POST','GET'])
def add_new_message():
    print(2)
    message_text = request.form['message_text']
    user_id = request.form['user_id']

    result = Message.add_new_message(message_text, user_id)
    print(result)
    return redirect("/dashboard")

