from flask import Flask

app = Flask("Hello")

def hi():
    return "Hello Pymier"

@app.route("/bye", methods=["GET"])
def bye():
    return "bye bye"

import datetime
def now():
    return "Bay gio la: " + str(datetime.datetime.now())


app.add_url_rule("/", "hi", hi)
# app.add_url_rule("/bye", "bye", bye)
app.add_url_rule("/time", "now", now)


@app.route("/double/<int:x>")
def double(x):
    return str(x * 2)


@app.route("/hello/<string:name>")
def sayhello(name):
    return "Hello {}".format(name)


students = ["Khanh", "Kien", "Hung"]
# @app.route("/danhsach")

# def danhsach():
#     dict_ds = {}
#     for i in range(0,len(students)):
#         dict_ds.update({students[i]:len(students[i])})
#     return str(for i in dict_ds "Name: {}")
    
from  flask import jsonify

songs = [
         {"name": "muon roi ma sao con", "view": 1_000_000},
         {"name": "chung ta cua hien tai", "view": 10_000_000}
        ]
    

from flask import request
import json
@app.route("/api/songs", methods=["GET", "POST"])
def api_list():
    try:
        with open("data.json", "rt") as f:
            songs = json.load(f)
    except FileNotFoundError:
        songs = basesongs

    if request.method == "GET":
        return jsonify(songs)
    else:
        # POST
        s = json.loadsrequest.data.decode("utf-8")
        print("XXX", data)
        s = json.loads(data)
        songs.append(s)
        with open("data.json", "wt") as f:
            json.dump(songs, f)
            
        return {"success": True}

