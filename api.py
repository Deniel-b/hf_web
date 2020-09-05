from flask import Flask
from flask import render_template

api = Flask(__name__)

@api.route("/", methods=['GET'])
def index():
    return render_template("index.html")