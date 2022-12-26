#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

#満腹度
hungry=0
#好感度
love=0
#ほこり
dust=0


def food_child():
    hungry = 100
    if love <= 100:
        love = love + 10
    elif love >= 100:
        love = 100
    

def play_child():
    pass

def cleen_child():
    pass

def sleep_child():
    pass

def food_adult():
    pass

def play_adult():
    pass

def cleen_adult():
    pass

def sleep_adult():
    pass




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
@app.route('/warm', methods=["GET"])
def home_get():
    return render_template('warm-egg.html')

#メインのゲーム画面(タスクの選択)
@app.route('/game', methods=["GET"])
def home_get2():
    return render_template('game.html')

#たまごをあたためる画面
@app.route('/finish', methods=["GET"])
def home_get3():
    return render_template('finish.html')
if __name__ == '__main__':
    app.run(debug=True)