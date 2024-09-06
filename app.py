from flask import Flask, render_template, url_for, request, flash, redirect
from database.model import DB
from os import getenv

app = Flask(__name__)

@app.route('/')
def index():
    return "index"


@app.route('/hello')
def hello_world():
    return "Hello, world!"


@app.route('/users')
def get_users():
    all_users = DB.get("select * from users")
    users = [{"name": user[1], "user_id": user[0], "value": user[2]} for user in all_users]
    return render_template('users.html', users=users)


@app.route('/new_user')
def new_user():
    return render_template('new_user.html')


@app.route('/add_user', methods=["POST"])
def add_user():
    form = request.form
    if "name" in form:
        if form["name"]:
            name = form["name"]
        else:
            return "Name cant be empty", 400
    else:
        return "No user name", 400
    value = request.form["value"] if "value" in request.form else False

    DB.commit("insert into users (name, value) values (%s, %s)", [name, value])
    flash(f"Пользователь {name} добавлен")

    return redirect(url_for("get_users"))


@app.route('/delete_user/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    user = DB.select(user_id)
    if not user:
        flash(f"Пользователь не найден")
        return redirect(url_for("get_users"))
    
    DB.commit("delete from users where id=%s", [user_id])

    flash(f"Пользователь {user[1]} добавлен")

    return redirect(url_for("get_users"))


@app.route('/user/<int:user_id>/')
def get_user(user_id):
    user = DB.select(user_id)
    if user:
        return render_template('user.html', name=user[1], user_id=user[0], value=user[2])
    return f"User {user_id} not found"


@app.route('/user/change_name/<int:user_id>/<name>')
def change_user_name(user_id, name):
    user = DB.select(user_id)
    if user:
        DB.commit("update users set name=%s where id=%s", [name, user_id])
        return f"Name of user {user_id} changed to {name}"
    return f"User {user_id} not found"
    
    
def run_server(host = "0.0.0.0", port = 5000):
    app.secret_key = getenv("app_secret_key")
    app.debug = True
    app.run(host=host, port=port)
