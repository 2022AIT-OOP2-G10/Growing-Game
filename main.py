#!/usr/bin/env python
# -*- coding: utf-8 -*-
from operator import truediv
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

#各種フラグ管理
#死亡フラグ
death=False
#成長１（雛）
child = False
#成長２（大人）
adult = False
#ゲーム終了
finish = False
#逃げる日数カウント
run_away = 0



def egg_warm():
    child = True

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

    if love > 20:
        love = love - 20
    elif love >= 0:
        love = 0


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

    if love > 20:
        love = love - 20
    elif love >= 0:
        love = 0

def day_start():
    global hungry, love, dust
    #日数をカウント
    day = day + 1

    #ホコリ10上昇
    dust = dust + 10

    #好感度10減少
    love = love - 10

    if dust >= 60:
        love = love - 20
    
    if love < 30:#好感度が30未満だったら脱走までの日数カウント
        run_away = run_away + 1

        if run_away >= 3:#3日連続30以下だったら脱走
            run_away#脱走させる

    elif love >=30:#好感度が30以上だったらカウントリセット
        run_away = 0

    

    if hungry == 0:
        death = True

    if child == True:
        child = True #エラー防止用の１行です
        #画像を変化する(雛)

    if day == 11:
        adult = True
        #画像変化（大人）
    
    if day == 26:
        finish = True
        #終了





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