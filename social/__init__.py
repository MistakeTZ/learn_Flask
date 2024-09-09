from flask import Flask
from flask_login import LoginManager
from os import path


app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'
open_session_users = {}

import social.routes


# Run server
def run_server(host = "0.0.0.0", port = 5000):
    from config import Config
    app.config.from_object(Config)
    app.template_folder = path.join("templates")

    app.debug = True
    app.run(host=host, port=port)

