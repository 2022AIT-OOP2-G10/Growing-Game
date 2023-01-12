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

#各種フラグ
grow_child = False #卵から子
grow_adult = False #子から大人
grow_end = False #育成終了
death = False #餓死
runaway = False #逃走
runaway_count = 0 #逃走までの日数カウント
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

    if chi.love >= 20:
        chi.love = chi.love - 20
    elif chi.love < 20:
        chi.love = 0

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

    if adu.love >= 20:
        adu.love = adu.love - 20
    elif adu.love < 20:
        adu.love = 0

a = adult()

def day_start(chi, adu):
    day = day + 1 #日数経過
    
    #1日の開始時のパラメータ変動
    if grow_child == True :
        chi.dust = chi.dust + 10
        chi.love = chi.love - 10
    elif grow_adult == True :
        adu.dust = adu.dust + 10
        adu.love = adu.love - 10

def day_end(chi, adu):
    if day == 1 : #2子に成長フラグを立てる
        grow_child = True
    if day == 9 : #大人に成長フラグを立てる
        grow_adult = True
        grow_child = False
    if day == 25 : #終了フラグを立てる
        grow_end = True

    #死亡フラグ
    if grow_child == True :
        if chi.hungry == 0 :
            death = True
    elif grow_adult == True :
        if adu.hungry == 0 :
            death = True

    #逃走フラグ
    if grow_child == True :
        if chi.love < 30 : #好感度30未満でカウント増加
            runaway_count = runaway_count + 1
        elif chi.love >= 30 : #好感度30以上でカウントリセット
            runaway_count = 0
        if runaway_count == 3 : #カウント3で逃走フラグがたつ
            runaway = True
    elif grow_adult == True :
        if adu.love < 30 :
            runaway_count = runaway_count + 1
        elif adu.love >= 30 :
            runaway_count = 0
        if runaway_count == 3 :
            runaway = True



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