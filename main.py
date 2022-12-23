#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)

#ホーム画面
@app.route('/', methods=["GET"])
def title():
    return render_template('title.html')

#たまごの選択画面
@app.route('/select', methods=["GET"])
def select():
    return render_template('select-egg.html')

#たまごをあたためる画面
#@app.route('/warm', methods=["GET"])
#def home_get():
#    return render_template('warm-egg.html')

#メインのゲーム画面(タスクの選択)
#@app.route('/game', methods=["GET"])
#def home_get():
#    return render_template('game.html')

#たまごをあたためる画面
#@app.route('/finish', methods=["GET"])
#def home_get():
#    return render_template('finish.html')
if __name__ == '__main__':
    app.run(debug=True)