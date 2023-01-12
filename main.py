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