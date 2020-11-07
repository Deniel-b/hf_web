from flask import Flask, config, request, url_for
from flask import render_template, g
import sqlite3
import os
from database.database import User
from database.exotics_db import Exotics
import request

app = Flask(__name__, static_folder='static', static_url_path='')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/", methods=['GET'])
def index():
    return app.send_static_file("index_copy.html")

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/news", methods=["GET"])
def news():
    for usr in User.select():
        a = usr.Name
    return render_template('news.html', name=a)

@app.route('/exotics', methods=["GET"])
def exotics():
    data = list()
    meta = list()
    for weapon in Exotics.select():
        meta.append(weapon.ID)
        meta.append(weapon.Name)
        meta.append(weapon.Type)
        meta.append(weapon.Energy)
        meta.append(weapon.Unlock)
        meta.append(weapon.Description)
        meta.append(weapon.PicLink)
        data.append(tuple(meta))
        meta.clear()