#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

#満腹度
hungry=0
#好感度
love=0
#ほこり
dust=0
#成長度
grow=0

#何日目か
day=1


def play_child():
    global hungry, love, dust
    if hungry <= 40:
        hungry = 0
    elif hungry > 40:
        hungry = hungry - 40

    if love >= 80:
        love = 100
    elif love < 80:
        love = love + 20

    if dust >= 50:
        dust = 100
    elif dust < 50:
        dust = dust + 50
    
def food_child():
    global hungry, love, dust
    hungry = 100
    if love <= 100:
        love = love + 10
    elif love >= 100:
        love = 100
  
def cleen_child():
    global hungry, love, dust
    if hungry <= 40:
        hungry = 0
    elif hungry > 40:
        hungry = hungry - 40
    
    if love >= 90:
        love = 100
    elif love < 90:
        love = love + 90
    dust = 0

def sleep_child():
    global hungry, love, dust
    if hungry <= 30:
        hungry = 0
    elif hungry > 30:
        hungry = hungry - 30

    if love >= 80:
        love = 100
    elif love < 80:
        love = love + 20


def play_adult():
    global hungry, love, dust
    if hungry <= 30:
        hungry = 0
    elif hungry < 30:
        hungry = hungry - 30

    if love >= 85:
        love = 100
    elif love < 85:
        love = love + 15

    if dust >= 60:
        dust = 100
    elif dust < 60:
        dust = dust + 40


def food_adult():
    global hungry, love, dust
    hungry = 100
    if love <= 100:
        love = love + 10
    elif love >= 100:
        love = 100


def cleen_adult():
    global hungry, love, dust
    if hungry <= 30:
        hungry = 0
    elif hungry > 30:
        hungry = hungry - 30
    
    if love >= 80:
        love = 100
    elif love < 80:
        love = love + 80
    dust = 0

def sleep_adult():
    global hungry, love, dust
    if hungry <= 30:
        hungry = 0
    elif hungry > 30:
        hungry = hungry - 30

    if love >= 80:
        love = 100
    elif love < 80:
        love = love + 20


app = Flask(__name__)


#ホーム画面
@app.route('/', methods=["GET"])
def title():
    #タイトル画面表示時に表示
    play_child()
    print(hungry)
    print(love)
    print(dust)
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
    # クエリを使ってGETメソッドで処理できる(都合悪そうならPOSTにも変更可)
    task=request.args.get('task')
    if task == 'eat':
        # ご飯を食べる関数　とかをここに書く
        print("ご飯を食べました")
    elif task == 'play':
        # 遊ぶ
        print("遊びました")
    elif task == 'sleep':
        # 寝る
        print("寝ました")
    return render_template('game.html',day=day,hungry=hungry,dust=dust,grow=grow)

#たまごをあたためる画面
@app.route('/finish', methods=["GET"])
def home_get3():
    return render_template('finish.html')
if __name__ == '__main__':
    app.run(debug=True)