import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel  
from PySide6.QtGui import QPixmap

class GameButton(QLabel):
    def __init__(self):
        super().__init__()
        # 画像のパス
        image = "./Images/character_egg.png"
        # 画像を配置する
        self.setPixmap(QPixmap(image).scaledToHeight(150))

    # QLabelでマウスイベントを受け取るために必要
    def mousePressEvent(self,event):
        self.clickedmethod()
        return QLabel.mousePressEvent(self,event)
    
    # クリックされた時の処理
    def clickedmethod(self):
        #処理したい内容。
        print("clicked")

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 3つのたまご
        eggLeft = GameButton()
        eggCenter = GameButton()
        eggRight = GameButton()
        
        # 水平なボックスを作成
        hbox = QHBoxLayout()
        hbox.addWidget(eggLeft)
        hbox.addWidget(eggCenter)
        hbox.addWidget(eggRight)
        
        # 垂直なボックスを作成
        vbox = QVBoxLayout()
        # 右下にボタンが移る
        vbox.addLayout(hbox)
        
        # 画面に上で設定したレイアウトを加える
        self.setLayout(vbox)    
        # 画面サイズ(x,y,縦,横)
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('育成ゲーム')    
        self.show()

app = QApplication(sys.argv)
mw = MainWidget()
mw.show()
app.exec()