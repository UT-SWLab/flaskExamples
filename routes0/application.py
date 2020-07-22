from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/mary")
def mary():
    return "Hello, Mary"

@app.route("/elvis") 
def elvis():
    return "Hello, Elvis"



