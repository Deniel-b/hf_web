from flask import Flask, config
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)

@server.route("/", methods=['GET'])
def index():
    return render_template("index.html")


db = SQLAlchemy(app)
app.confg