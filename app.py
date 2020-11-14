from flask import Flask, config, request, url_for
from flask import render_template, g
import sqlite3
import os
from database.database import User
from database.exotics_db import Exotics
import json

# import request

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


@app.route('/exotics', methods=["GET"])
def exotics():
    data = dict()
    meta = dict()
    for weapon in Exotics.select():
        meta.update({"Name": weapon.Name})
        meta.update({"Type": weapon.Type})
        meta.update({"Energy": weapon.Energy})
        meta.update({"Unlock": weapon.Unlock})
        meta.update({"Description": weapon.Description})
        meta.update({"PicLink": weapon.PicLink})
        data[weapon.ID] = meta
        # print(data)
        # meta.clear()
    jsonDB = json.dumps(data, ensure_ascii=False)
    print(jsonDB)
    return render_template('exotics.html', jsonfile=jsonDB)
