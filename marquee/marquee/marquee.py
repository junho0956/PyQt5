import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# marquee 길이확인을 위한 변수
label_size = 320
resize_py = 0
# marquee class
class MarqueeLabel(QLabel):
    def __init__(self, parent=None):
        global cnt
        global label_size
        QLabel.__init__(self, parent)

        self.move = 1
        self.px = 15
        self.py = 15
        self._direction = Qt.RightToLeft
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(40)
        self._speed = 1
        self.lastx = self.fontMetrics().width(self.text())

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.lastx > label_size:
            self.px -= self.speed()
            self.lastx -= 0.3
        else:
            if self.px > 0:
                self.px -= self.speed()
            else:
                self.move = 0

        painter.drawText(self.px, self.py, self.text())

    def speed(self):
        return self._speed

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
       global resize_py
       #MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
       MainWindow.resize(786, 594)

       self.centralwidget = QtWidgets.QWidget(MainWindow)
       self.centralwidget.setObjectName("centralwidget")

       _label_ = QtWidgets.QLabel()
       _label_2 = QtWidgets.QLabel()
       _label_3 = QtWidgets.QLabel()
       _label_4 = QtWidgets.QLabel()
       _label_5 = QtWidgets.QLabel()

       self.label = QtWidgets.QLabel(self.centralwidget)
       self.label.setGeometry(QtCore.QRect(50,20,510,60))
       self.label.setObjectName("label")
       self.label_2 = QtWidgets.QLabel(self.centralwidget)
       self.label_2.setGeometry(QtCore.QRect(130,160,570,50))
       self.label_2.setObjectName("label_2")
       self.label_3 = QtWidgets.QLabel(self.centralwidget)
       self.label_3.setGeometry(QtCore.QRect(130,250,570,50))
       self.label_3.setObjectName("label_3")
       self.label_4 = QtWidgets.QLabel(self.centralwidget)
       self.label_4.setGeometry(QtCore.QRect(130,340,570,50))
       self.label_4.setObjectName("label_4")
       self.label_5 = QtWidgets.QLabel(self.centralwidget)
       self.label_5.setGeometry(QtCore.QRect(130,430,570,50))
       self.label_5.setObjectName("label_5")
       self.label_6 = QtWidgets.QLabel(self.centralwidget)
       self.label_6.setGeometry(QtCore.QRect(130,520,570,50))
       self.label_6.setObjectName("label_6")
       MainWindow.setCentralWidget(self.centralwidget)
       
       self.label.setText("    marquee")

       # marquee class 가져오기
       self.label_2 = MarqueeLabel(self.label_2)
       self.label_3 = MarqueeLabel(self.label_3) 
       self.label_4 = MarqueeLabel(self.label_4)
       self.label_5 = MarqueeLabel(self.label_5)
       self.label_6 = MarqueeLabel(self.label_6)
       
       #한글 -> 15
       #알파벳 소문자 -> 8
       #알파벳 대문자 -> 9
       #공백 -> 5
       #현재 공백칸 405
       self.label_2.setText("가나다라마바사가나다라마바사가나다라마바사")
       self.label_3.setText("아자차카타파하가나다라마바사가나다라마바사")
       self.label_4.setText("abcdefghijklmn가나다라마바사가나다라마바사")
       self.label_5.setText("ABCDEFGHIJKLMN가나다라마바사가나다라마바사")
       self.label_6.setText("MARQUEE TEST가나다라마바사가나다라마바사")


    def check_move(self):
           if self.label_2.move == 0 :
               if self.label_3.move == 0 :
                   if self.label_4.move == 0 :
                       if self.label_5.move == 0 :
                           if self.label_6.move == 0 :
                               self.change_text()

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec_())