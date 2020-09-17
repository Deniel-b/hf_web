from flask import Flask, config, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")