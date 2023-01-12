#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import urllib.parse


# 満腹度
hungry = 0
# 好感度
love = 0
# ほこり
dust = 0
# 成長度
grow = 0

# 何日目か
day = 1

#卵=0,ひな=1,大人=2
status = 1

# 遊ぶ(ひな)
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
    

# ごはん(ひな)
def food_child():
    global hungry, love, dust
    hungry = 100
    if love <= 100:
        love = love + 10
    elif love >= 100:
        love = 100

# そうじ(ひな)
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

# ねる(ひな)
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

# 遊ぶ(大人)
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

# ごはん（大人）
def food_adult():
    global hungry, love, dust
    hungry = 100
    if love <= 100:
        love = love + 10
    elif love >= 100:
        love = 100

# そうじ（大人）
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

# ねる（大人）
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

# 日にちの更新
def nextday():
    # リロードすると前回の行動のクエリパラメータが残っているので，勝手に行動される
    global status,day
    day = day + 1
    if day == 10 :
        status = 2 


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
def warm():
    return render_template('warm-egg.html')

#メインのゲーム画面(タスクの選択)
@app.route('/game', methods=["GET"])
def growing():
    # クエリを使ってGETメソッドで処理できる(都合悪そうならPOSTにも変更可)
    task=request.args.get('task')

    if task != None:
        if status == 1:
            if task == 'eat':
                food_child()
            elif task == 'play':
                play_child()
            elif task == 'sleep':
                sleep_child()
            elif task == 'clean':
                cleen_child()

        if status == 2:
            if task == 'eat':
                food_adult()
            elif task == 'play':
                play_adult()
            elif task == 'sleep':
                sleep_adult()
            elif task == 'clean':
                cleen_adult()

        nextday()

    return render_template('game.html',day=day,hungry=hungry,dust=dust,grow=grow,status=status)

#たまごをあたためる画面
@app.route('/finish', methods=["GET"])
def finish():
    return render_template('finish.html')

if __name__ == '__main__':
    app.run(debug=True)