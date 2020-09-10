from flask import Flask
from flask import render_template

server = Flask(__name__)

@server.route("/", methods=['GET'])
def index():
    return render_template("index.html")