
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    dogs=["Otis", "Bubbles", "Charlie", "Milo"]
    return render_template("index.html", dogs=dogs)
