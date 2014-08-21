#coding=utf-8
from flask import Flask
from flask import render_template
import random
import json

import os
dirname = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
pic_dir = 'pics'
interval_ms = 200
weight_px = 720.0

def load_pic_name(path):
    names = os.listdir(path)
    return names

@app.route("/")
def hello():
    return 'Hello, User'

@app.route('/show', methods = ['GET', 'POST'])
def show(path=None):
    # choose a pic
    return render_template('show.html', show=show, interval_ms=interval_ms, weight_px=weight_px)

@app.route('/allpics', methods = ['GET', 'POST'])
def allpics():
    pics = []
    paths = []
    pic_path = os.path.join(dirname, app._static_folder, pic_dir)
    for root,dirs,files in os.walk(pic_path):
        for fn in files:
            if fn[0] != '.':
                pics.append(fn)
                paths.append('/%s/%s/%s/%s'%(app._static_folder, pic_dir, root[len(pic_path)+1:], fn))
    res = [pics, paths]
    return json.dumps(res)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
