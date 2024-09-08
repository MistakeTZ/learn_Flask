from flask import Flask, render_template, url_for, request, flash, redirect, jsonify, Response
from social.forms import LoginForm
import json
from database.model import DB
from os import getenv, path

app = Flask(__name__)

# Default page
@app.route('/')
@app.route('/index')
def index():
    if "username" in request.args:
        user = {'username': request.args["username"]}
    else:
        user = {'username': "unregistered user"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('home_page.html', title='Home', user=user, posts=posts)


@app.route('/login', methods = ["GET", "POST"])
def login_page():
    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            flash('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect('/index')
        else:
            pass
            # flash('Data not valid')
        
    return render_template('login.html', title='Sign In', form=form)


# Run server
def run_server(host = "0.0.0.0", port = 5000):
    from config import Config
    app.config.from_object(Config)
    app.template_folder = path.join("templates")

    app.debug = True
    app.run(host=host, port=port)
