from flask import render_template
from flask import Flask

@app.route(/students2)
students = ["khanh", "kien", "hung"]
def list_students2():
    name_len = [(i, len(i)) for i in students]
    return render_template("index.html", ss=name_len)