from flask import Flask, render_template, url_for
from database.model import DB

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
    app.debug = True
    app.run(host=host, port=port)
