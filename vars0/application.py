from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    my_header = "Hello, World!"
    return render_template("index.html", my_header=my_header)

@app.route("/bye") 
def bye():
    my_header = "Goodbye"
    return render_template("index.html", my_header=my_header)
