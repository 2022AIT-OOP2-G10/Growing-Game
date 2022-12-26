#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

#満腹度
hungry=0
#好感度
love=0
#ほこり
dust=0

# 綴りが違ってたので一応書き換えた
def food_child(self):
    pass

def play_child():
    # グローバル変数を書き換える場合は明示的に宣言する必要があるらしい．
    global hungry, love, dust
    hungry = hungry - 40
    love = love + 20
    dust = dust + 50

def cleen_child(self):
    pass

def sleep_child(self):
    pass

def food_adult(self):
    pass

def play_adult(self):
    pass

def cleen_adult(self):
    pass

def sleep_adult(self):
    pass





app = Flask(__name__)

#ホーム画面
@app.route('/', methods=["GET"])
def title():
    # テスト用にタイトル画面表示するときにplay_childを実行する
    play_child()
    print(hungry) # -40
    print(love) # 20
    print(dust) # 50
    
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