from flask import Flask, render_template, url_for, request, flash, redirect, jsonify, Response
from forms import LoginForm
import json
from database.model import DB
from os import getenv

app = Flask(__name__)

# Default page
@app.route('/')
@app.route('/index')
def index():
    if "username" in request.args:
        user = {'username': request.args["username"]}
    else:
        user = {'username': "Semen"}
    return render_template('restaurants/restaurants.html', title='Home', user=user)


@app.route('/login')
def login_page():
    form = LoginForm()
    return render_template('restaurants/login.html', title='Sign In', form=form)

    
# Run server
def run_server(host = "0.0.0.0", port = 5000):
    from config import Config
    app.config.from_object(Config)

    app.debug = True
    app.run(host=host, port=port)
