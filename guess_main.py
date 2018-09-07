#coding:utf-8

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import numpy as np
from guess import *
import sys


class mywindow(Ui_Form, QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.times = 0 # 6次猜中才可以
        self.num = np.random.randint(30)
        self.setWindowTitle("猜数字游戏")
        print(self.num)
    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, "确认", "确认退出？", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
    def guess(self):
        if self.check_time():
            number = int(self.lineEdit.text())
            if number > self.num:
                QMessageBox.about(self, "结果", "猜大了！")
                self.textEdit.append(self.lineEdit.text() + ": 猜大了")
                self.times = self.times + 1
                self.lineEdit.clear()
                self.lineEdit.setFocus()
            elif number < self.num:
                QMessageBox.about(self, "结果", "猜小了！")
                self.textEdit.append(self.lineEdit.text() + ": 猜小了")
                self.lineEdit.clear()
                self.times = self.times + 1
                self.lineEdit.setFocus()
            elif number == self.num:
                QMessageBox.about(self, "结果", "恭喜猜中了")
                self.textEdit.append(self.lineEdit.text())
                self.lineEdit.clear()
                self.game_again()
                self.lineEdit.setFocus()
            else:
                pass
        else:
            QMessageBox.about(self, "结果", "没猜到，重来")
            self.game_again()
    def game_again(self):
        self.textEdit.append("=========上一轮游戏结束，新一轮重新开始=========")
        self.num = np.random.randint(30)
        self.lineEdit.clear()
        print(self.num)
        self.times = 0
    def check_time(self):
        print(self.times)
        if self.times < 6:
            return True
        else:
            return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mywindow()
    w.pushButton.clicked.connect(w.guess)
    w.show()
    sys.exit(app.exec_())