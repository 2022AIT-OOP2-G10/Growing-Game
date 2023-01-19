#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, url_for, redirect

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

status = 1

food_count = 0 #ごはんを選択した数
evo = 0 #分岐フラグ
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
        chi.love = chi.love + 20

    if chi.dust >= 50:
        chi.dust = 100
    elif chi.dust < 50:
        chi.dust = chi.dust + 50

    
def food_child(chi):
    global food_count
    food_count=food_count+1
    chi.hungry = 100
    if chi.love <= 90:
        chi.love = chi.love + 10
    elif chi.love > 90:
        chi.love = 100
  
def cleen_child(chi):
    if chi.hungry <= 40:
        chi.hungry = 0
    elif chi.hungry > 40:
        chi.hungry = chi.hungry - 40
    
    if chi.love >= 90:
        chi.love = 100
    elif chi.love < 90:
        chi.love = chi.love + 10
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
    global food_count
    food_count=food_count+1
    adu.hungry = 100
    if adu.love <= 90:
        adu.love = adu.love + 10
    elif adu.love > 90:
        adu.love = 100


def cleen_adult(adu):
    if adu.hungry <= 30:
        adu.hungry = 0
    elif adu.hungry > 30:
        adu.hungry = adu.hungry - 30
    
    if adu.love >= 80:
        adu.love = 100
    elif adu.love < 80:
        adu.love = adu.love + 20
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

def day_end(chi, adu):
    global status, day, food_count, evo, grow_end, death, runaway, runaway_count
    #成長分岐
    if status==1 or status==6 or status ==3 or status ==8:
        if food_count >= 6:
            evo = 1
        elif food_count < 6:
            evo = 2
    elif status==2 or status==7:
        if food_count >= 6:
            evo = 2
        elif food_count < 6:
            evo = 3
    #死亡フラグ
    if status == 1 or status == 6:
        if chi.hungry == 0 :
            death = True
    else:
        if adu.hungry == 0 :
            death = True
    
    #逃走フラグ
    if status == 1 or status == 6:
        if chi.love < 30 : #好感度30未満でカウント増加
            runaway_count = runaway_count + 1
        elif chi.love >= 30 : #好感度30以上でカウントリセット
            runaway_count = 0
        if runaway_count == 3 : #カウント3で逃走フラグがたつ
            runaway = True
    else:
        if adu.love < 30 :
            runaway_count = runaway_count + 1
        elif adu.love >= 30 :
            runaway_count = 0
        if runaway_count == 3 :
            runaway = True

    day = day + 1
    if day == 10 :

        status = status+evo 
        food_count=0

    if day == 25 : #終了フラグを立てる
        status = status+evo 
        adu.hungry = chi.hungry
        adu.dust = chi.dust
        adu.love = chi.love
        grow_end = True

    #1日の開始時のパラメータ変動

    if status == 1 or 6 :

        if chi.dust <= 90:
            chi.dust = chi.dust + 10
        else:
            chi.dust = 100
        if chi.love >= 10:
            chi.love = chi.love - 10
        else:
            chi.love = 0
    elif status == 2 or status == 6:
        if adu.dust <= 90:
            adu.dust = adu.dust + 10
        else:
            adu.dust = 100
        if adu.love >= 10:
            adu.love = adu.love - 10
        else:
            adu.love = 0

app = Flask(__name__)

#ホーム画面
@app.route('/', methods=["GET"])
def title():
    #タイトル画面表示時に表示
    play_child(c)
    return render_template('title.html')

#たまごの選択画面
@app.route('/select', methods=["GET"])
def select():
    global status
    egg = request.args.get('egg')
    if egg == '1':
        # 何かしらの処理
        status=6    
        return redirect(url_for('growing'))
    if egg == '2':
        status=1
        return redirect(url_for('growing'))

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
    message = ''

    if status == 1 or 6:


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
            return render_template('game.html',day=day,bird=c,status=status)

        day_end(c,a)
        if death or runaway:
            return redirect(url_for('finish'))

        return render_template('game.html',day=day,bird=c,status=status,message=message)


    else:
        if task == 'eat':
            food_adult(a)
            message = 'ごはんを食べました'
        elif task == 'play':
            play_adult(a)
            message = '遊びました'
        elif task == 'sleep':
            sleep_adult(a)
            message = '寝ました'
        elif task == 'clean':
            cleen_adult(a)
            message = '掃除しました'

        else:
            return render_template('game.html',day=day,bird=a,status=status)

        day_end(c,a)
        
        if day > 25 or death or runaway:
            return redirect(url_for('finish'))
            
        return render_template('game.html',day=day,bird=a,status=status)
    
    return render_template('game.html',day=day,status=status,message=message)

    return render_template('game.html',day=day,status=status,message=message)
        

#たまごをあたためる画面
@app.route('/finish', methods=["GET"])
def finish():
    return render_template('finish.html',death=death, runaway=runaway, status=status)

if __name__ == '__main__':
    app.run(debug=True)