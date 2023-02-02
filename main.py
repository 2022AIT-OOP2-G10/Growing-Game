#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webbrowser
from flask import Flask, request, render_template, url_for, redirect

class character :
    hungry = 100# 満腹度
    love = 0# 好感度
    dust = 0# ほこり
    status = 0
    day = 1# 何日目か
    food_count = 0 #ごはんを選択した数
    evo = 0 #分岐フラグ
    grow_end = False #育成終了
    death = False #餓死
    runaway = False #逃走
    runaway_count = 0 #逃走までの日数カウント

c = character()

def reset_para(cha):
    cha.hungry = 100
    cha.love = 0
    cha.dust = 0
    cha.status = 0
    cha.day = 1
    cha.food_count = 0 
    cha.evo = 0 
    cha.grow_end = False 
    cha.death = False 
    cha.runaway = False 
    cha.runaway_count = 0 

def play_child(cha):
    if cha.hungry <= 40:
        cha.hungry = 0
    elif cha.hungry > 40:
        cha.hungry = cha.hungry - 40

    if cha.love >= 80:
        cha.love = 100
    elif cha.love < 80:
        cha.love = cha.love + 20

    if cha.dust >= 50:
        cha.dust = 100
    elif cha.dust < 50:
        cha.dust = cha.dust + 50

    
def food_child(cha):
    cha.food_count=cha.food_count+1
    cha.hungry = 100
    if cha.love <= 90:
        cha.love = cha.love + 10
    elif cha.love > 90:
        cha.love = 100
  
def cleen_child(cha):
    if cha.hungry <= 40:
        cha.hungry = 0
    elif cha.hungry > 40:
        cha.hungry = cha.hungry - 40
    
    if cha.love >= 90:
        cha.love = 100
    elif cha.love < 90:
        cha.love = cha.love + 10
    cha.dust = 0

def sleep_child(cha):
    if cha.hungry <= 30:
        cha.hungry = 0
    elif cha.hungry > 30:
        cha.hungry = cha.hungry - 30

    if cha.love >= 20:
        cha.love = cha.love - 20
    elif cha.love < 20:
        cha.love = 0

def play_adult(cha):
    if cha.hungry <= 30:
        cha.hungry = 0
    elif cha.hungry > 30:
        cha.hungry = cha.hungry - 30

    if cha.love >= 85:
        cha.love = 100
    elif cha.love < 85:
        cha.love = cha.love + 15

    if cha.dust >= 60:
        cha.dust = 100
    elif cha.dust < 60:
        cha.dust = cha.dust + 40
        
def food_adult(cha):
    cha.food_count=cha.food_count+1
    cha.hungry = 100
    if cha.love <= 90:
        cha.love = cha.love + 10
    elif cha.love > 90:
        cha.love = 100

def cleen_adult(cha):
    if cha.hungry <= 30:
        cha.hungry = 0
    elif cha.hungry > 30:
        cha.hungry = cha.hungry - 30
    
    if cha.love >= 80:
        cha.love = 100
    elif cha.love < 80:
        cha.love = cha.love + 20
    cha.dust = 0

def sleep_adult(cha):
    
    if cha.hungry <= 30:
        cha.hungry = 0
    elif cha.hungry > 30:
        cha.hungry = cha.hungry - 30

    if cha.love >= 20:
        cha.love = cha.love - 20
    elif cha.love < 20:
        cha.love = 0

def day_end(cha):
    #成長分岐
    if cha.status==1 or cha.status ==3:
        if cha.love >= 60:
            cha.evo = 1
        else:
            cha.evo = 2
    elif cha.status==2:
        if cha.love >= 60:
            cha.evo = 2
        else:
            cha.evo = 3
    elif cha.status==6:
        if cha.food_count >= 9:
            cha.evo = 2
        else:
            cha.evo = 1
    elif cha.status==7:
        if cha.food_count >= 9:
            cha.evo = 3
        else:
            cha.evo = 2
    elif cha.status==8:
        if cha.food_count >= 6:
            cha.evo = 2
        else:
            cha.evo = 1
    #死亡フラグ
    if cha.hungry == 0 :
            cha.death = True
    
    #逃走フラグ
    if cha.love < 30 : #好感度30未満でカウント増加
            cha.runaway_count = cha.runaway_count + 1
    elif cha.love >= 30 : #好感度30以上でカウントリセット
            cha.runaway_count = 0
    if cha.runaway_count == 3 : #カウント3で逃走フラグがたつ
            cha.runaway = True

    cha.day = cha.day + 1
    if cha.day == 10 :

        cha.status = cha.status+cha.evo 
        cha.food_count=0

    if cha.day == 25 : #終了フラグを立てる
        cha.status = cha.status+cha.evo 
        cha.grow_end = True

    #1日の開始時のパラメータ変動

    if cha.dust>=70:
        if cha.love >= 20:
            cha.love = cha.love - 20
        else:
            cha.love = 0
        
    if cha.dust <= 90:
        cha.dust = cha.dust + 10
    else:
        cha.dust = 100


app = Flask(__name__)

#ホーム画面
@app.route('/', methods=["GET"])
def title():
    return render_template('title.html')

#たまごの選択画面
@app.route('/select', methods=["GET"])
def select():

    egg = request.args.get('egg')
    if egg == '1':
        # 何かしらの処理
        c.status=6    
        return redirect(url_for('growing'))
    if egg == '2':
        c.status=1
        return redirect(url_for('growing'))

    return render_template('select-egg.html')

#メインのゲーム画面(タスクの選択)
@app.route('/game', methods=["GET"])
def growing():
    # クエリを使ってGETメソッドで処理できる(都合悪そうならPOSTにも変更可)

    task=request.args.get('task')
    message = ''

    if c.status == 1 or c.status == 6:
        if task == 'eat':
            food_child(c)
            message = 'ごはんを食べました'
        elif task == 'play':
            play_child(c)
            message = '遊びました'
        elif task == 'sleep':
            sleep_child(c)
            message = '寝ました'
        elif task == 'clean':
            cleen_child(c)
            message = '掃除しました'
        else:
            return render_template('game.html',day=c.day,bird=c,status=c.status)
        day_end(c)
        if c.death or c.runaway:
            return redirect(url_for('finish'))

        return render_template('game.html',day=c.day,bird=c,status=c.status,message=message)


    else:
        if task == 'eat':
            food_adult(c)
            message = 'ごはんを食べました'
        elif task == 'play':
            play_adult(c)
            message = '遊びました'
        elif task == 'sleep':
            sleep_adult(c)
            message = '寝ました'
        elif task == 'clean':
            cleen_adult(c)
            message = '掃除しました'

        else:
            return render_template('game.html',day=c.day,bird=c,status=c.status)

        day_end(c)
        
        if c.grow_end or c.death or c.runaway:
            return redirect(url_for('finish'))
            
        return render_template('game.html',day=c.day,bird=c,status=c.status,message=message)
        

#リザルト画面
@app.route('/finish', methods=["GET"])
def finish():
    task=request.args.get('task')
    if task=='onemore':
        reset_para(c)
        return redirect(url_for('select'))

    return render_template('finish.html',death=c.death, runaway=c.runaway, status=c.status)

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000", new=1, autoraise=True)
    app.run()