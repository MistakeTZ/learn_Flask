from flask import Flask, render_template, url_for, request, flash, redirect, jsonify, Response
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
        user = {'username': "Oleg"}
    return render_template('restaurants.html', title='Home', user=user)


@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp

    
# Run server
def run_server(host = "0.0.0.0", port = 5000):
    app.secret_key = getenv("app_secret_key")
    app.debug = True
    app.run(host=host, port=port)
