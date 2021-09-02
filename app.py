# save this as app.py
from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('base.html', title='home')