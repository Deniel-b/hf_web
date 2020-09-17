from flask import Flask, config, request
from flask import render_template,g
# from flask_sqlalchemy import SQLAlchemy
import sqlite3  

app = Flask(__name__, static_folder='static', static_url_path='')
# DATABASE = '/path/to/database.db'

@app.route("/", methods=['GET'])
def index():
    return app.send_static_file("index.html")


'''def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is None:
        db.close()'''

