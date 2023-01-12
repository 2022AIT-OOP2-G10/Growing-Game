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

class child :
    hungry = 0
    love = 0
    dust = 0

def play_child(chi):
    if chi.hungry <= 40:
        chi.hungry = 0
    elif chi.hungry > 40:
        chi.hungry = chi.hungry - 40

    if chi.love >= 80:
        chi.love = 100
    elif chi.love < 80:
        chi.love = love + 20

    if chi.dust >= 50:
        chi.dust = 100
    elif chi.dust < 50:
        chi.dust = chi.dust + 50

    
def food_child(chi):
    chi.hungry = 100
    if chi.love <= 100:
        chi.love = chi.love + 10
    elif chi.love >= 100:
        chi.love = 100
  
def cleen_child(chi):
    if chi.hungry <= 40:
        chi.hungry = 0
    elif chi.hungry > 40:
        chi.hungry = chi.hungry - 40
    
    if chi.love >= 90:
        chi.love = 100
    elif chi.love < 90:
        chi.love = chi.love + 90
    chi.dust = 0

def sleep_child(chi):
    if chi.hungry <= 30:
        chi.hungry = 0
    elif chi.hungry > 30:
        chi.hungry = chi.hungry - 30

    if chi.love >= 80:
        chi.love = 100
    elif chi.love < 80:
        chi.love = chi.love + 20

c = child()

class adult :
    hungry = 0
    love = 0
    dust = 0


def play_adult(adu):
    if adu.hungry <= 30:
        adu.hungry = 0
    elif adu.hungry > 30:
        adu.hungry = adu.hungry - 30

    if adu.love >= 85:
        adu.love = 100
    elif adu.love < 85:
        adu.love = adu.love + 15

    if adu.dust >= 60:
        adu.dust = 100
    elif adu.dust < 60:
        adu.dust = adu.dust + 40
        


def food_adult(adu):
    adu.hungry = 100
    if adu.love <= 100:
        adu.love = adu.love + 10
    elif adu.love >= 100:
        adu.love = 100


def cleen_adult(adu):
    if adu.hungry <= 30:
        adu.hungry = 0
    elif adu.hungry > 30:
        adu.hungry = adu.hungry - 30
    
    if adu.love >= 80:
        adu.love = 100
    elif adu.love < 80:
        adu.love = adu.love + 80
    adu.dust = 0

def sleep_adult(adu):
    
    if adu.hungry <= 30:
        adu.hungry = 0
    elif adu.hungry > 30:
        adu.hungry = adu.hungry - 30

    if adu.love >= 80:
        adu.love = 100
    elif adu.ove < 80:
        adu.love = adu.love + 20

a = adult()

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
    play_child(c)
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
                food_child(c)
            elif task == 'play':
                play_child(c)
            elif task == 'sleep':
                sleep_child(c)
            elif task == 'clean':
                cleen_child(c)

        if status == 2:
            if task == 'eat':
                food_adult(a)
            elif task == 'play':
                play_adult(a)
            elif task == 'sleep':
                sleep_adult(a)
            elif task == 'clean':
                cleen_adult(a)

        nextday()

    return render_template('game.html',day=day,hungry=hungry,dust=dust,grow=grow,status=status)

#たまごをあたためる画面
@app.route('/finish', methods=["GET"])
def finish():
    return render_template('finish.html')

if __name__ == '__main__':
    app.run(debug=True)