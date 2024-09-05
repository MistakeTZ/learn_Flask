from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"
    
    
def run_server(host = "0.0.0.0", port = 5000):
    app.debug = True
    app.run(host=host, port=port)
