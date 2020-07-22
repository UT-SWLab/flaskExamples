import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    indep_day = now.month == 7 and now.day == 4
    indep_day = True
    return render_template("index.html", indep_day=indep_day)
