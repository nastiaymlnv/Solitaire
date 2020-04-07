import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import shuffle
from functools import partial
import PNG

_translate = QtCore.QCoreApplication.translate


class Cards:
    def __init__(self, index=0):
        self.index = index


    def iter_stock(self):
        if self.index == len(stock):
            self.index = 0
        ui.pushButton_30.setText(_translate("MainWindow", stock[self.index]))
        if "♥" in ui.pushButton_30.text():
            ui.pushButton_30.setStyleSheet("color: red")
        elif "♦" in ui.pushButton_30.text():
            ui.pushButton_30.setStyleSheet("color: red")
        else:
            ui.pushButton_30.setStyleSheet("color: black")
        self.index += 1


class Desk:
    def value(self, pushButton, num):
        if "A" in pushButton.text():
            num.append(1)
            names.append(pushButton)
        if "K" in pushButton.text():
            num.append(13)
            names.append(pushButton)
        if "Q" in pushButton.text():
            num.append(12)
            names.append(pushButton)
        if "J" in pushButton.text():
            num.append(11)
            names.append(pushButton)
        if "10" in pushButton.text():
            num.append(10)
            names.append(pushButton)
        if "9" in pushButton.text():
            num.append(9)
            names.append(pushButton)
        if "8" in pushButton.text():
            num.append(8)
            names.append(pushButton)
        if "7" in pushButton.text():
            num.append(7)
            names.append(pushButton)
        if "6" in pushButton.text():
            num.append(6)
            names.append(pushButton)
        if "5" in pushButton.text():
            num.append(5)
            names.append(pushButton)
        if "4" in pushButton.text():
            num.append(4)
            names.append(pushButton)
        if "3" in pushButton.text():
            num.append(3)
            names.append(pushButton)
        if "2" in pushButton.text():
            num.append(2)
            names.append(pushButton)
        Desk.summ(Desk, num, names, pushButton)

    def summ(self, num, names, pushButton):
        if len(names) == 2 and sum(num) != 13:
            num.clear()
            names.clear()
        elif sum(num) == 13:
            if len(names) == 1:
                names[0].hide()
                num.clear()
                names.clear()
            elif len(names) == 2:
                names[0].hide()
                names[1].hide()
                num.clear()
                names.clear()


    # def score(self, pushButton):
    #     if Desk.value(Desk, pushButton) == 13:
    #         pass


def main():
    ui.pushButton_29.clicked.connect(c.iter_stock)
    ui.pushButton_1.clicked.connect(partial(Desk.value, Desk, ui.pushButton_1, num))
    ui.pushButton_2.clicked.connect(partial(Desk.value, Desk, ui.pushButton_2, num))
    ui.pushButton_3.clicked.connect(partial(Desk.value, Desk, ui.pushButton_3, num))
    ui.pushButton_4.clicked.connect(partial(Desk.value, Desk, ui.pushButton_4, num))
    ui.pushButton_5.clicked.connect(partial(Desk.value, Desk, ui.pushButton_5, num))
    ui.pushButton_6.clicked.connect(partial(Desk.value, Desk, ui.pushButton_6, num))
    ui.pushButton_7.clicked.connect(partial(Desk.value, Desk, ui.pushButton_7, num))
    ui.pushButton_8.clicked.connect(partial(Desk.value, Desk, ui.pushButton_8, num))
    ui.pushButton_9.clicked.connect(partial(Desk.value, Desk, ui.pushButton_9, num))
    ui.pushButton_10.clicked.connect(partial(Desk.value, Desk, ui.pushButton_10, num))
    ui.pushButton_11.clicked.connect(partial(Desk.value, Desk, ui.pushButton_11, num))
    ui.pushButton_12.clicked.connect(partial(Desk.value, Desk, ui.pushButton_12, num))
    ui.pushButton_13.clicked.connect(partial(Desk.value, Desk, ui.pushButton_13, num))
    ui.pushButton_14.clicked.connect(partial(Desk.value, Desk, ui.pushButton_14, num))
    ui.pushButton_15.clicked.connect(partial(Desk.value, Desk, ui.pushButton_15, num))
    ui.pushButton_16.clicked.connect(partial(Desk.value, Desk, ui.pushButton_16, num))
    ui.pushButton_17.clicked.connect(partial(Desk.value, Desk, ui.pushButton_17, num))
    ui.pushButton_18.clicked.connect(partial(Desk.value, Desk, ui.pushButton_18, num))
    ui.pushButton_19.clicked.connect(partial(Desk.value, Desk, ui.pushButton_19, num))
    ui.pushButton_20.clicked.connect(partial(Desk.value, Desk, ui.pushButton_20, num))
    ui.pushButton_21.clicked.connect(partial(Desk.value, Desk, ui.pushButton_21, num))
    ui.pushButton_22.clicked.connect(partial(Desk.value, Desk, ui.pushButton_22, num))
    ui.pushButton_23.clicked.connect(partial(Desk.value, Desk, ui.pushButton_23, num))
    ui.pushButton_24.clicked.connect(partial(Desk.value, Desk, ui.pushButton_24, num))
    ui.pushButton_25.clicked.connect(partial(Desk.value, Desk, ui.pushButton_25, num))
    ui.pushButton_26.clicked.connect(partial(Desk.value, Desk, ui.pushButton_26, num))
    ui.pushButton_27.clicked.connect(partial(Desk.value, Desk, ui.pushButton_27, num))
    ui.pushButton_28.clicked.connect(partial(Desk.value, Desk, ui.pushButton_28, num))
    ui.pushButton_30.clicked.connect(partial(Desk.value, Desk, ui.pushButton_30, num))


if __name__ == "__main__":
    c = Cards()
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    # palette = QPalette()
    # palette.setColor(QPalette.Window, QColor(53, 53, 53))
    # palette.setColor(QPalette.WindowText, Qt.white)
    # palette.setColor(QPalette.Base, QColor(25, 25, 25))
    # palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    # palette.setColor(QPalette.ToolTipBase, Qt.white)
    # palette.setColor(QPalette.ToolTipText, Qt.white)
    # palette.setColor(QPalette.Text, Qt.white)
    # palette.setColor(QPalette.Button, QColor(53, 53, 53))
    # palette.setColor(QPalette.ButtonText, Qt.white)
    # palette.setColor(QPalette.BrightText, Qt.red)
    # palette.setColor(QPalette.Link, QColor(42, 130, 218))
    # palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    # palette.setColor(QPalette.HighlightedText, Qt.black)
    # app.setPalette(palette)
    # ui = uic.loadUi(app.theme["ui_path"] + "window.ui")
    ui = uic.loadUi("window.ui")
    ui.setWindowTitle("Pyramid Solitaire")
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ui.setWindowIcon(QtGui.QIcon(os.path.join(base_dir, 'green_felt.jpg')))  # must be in ico format

    cards = ["A♥", "K♥", "Q♥", "J♥", "10♥", "9♥", "8♥", "7♥", "6♥", "5♥", "4♥", "3♥", "2♥",
             "A♠", "K♠", "Q♠", "J♠", "10♠", "9♠", "8♠", "7♠", "6♠", "5♠", "4♠", "3♠", "2♠",
             "A♣", "K♣", "Q♣", "J♣", "10♣", "9♣", "8♣", "7♣", "6♣", "5♣", "4♣", "3♣", "2♣",
             "A♦", "K♦", "Q♦", "J♦", "10♦", "9♦", "8♦", "7♦", "6♦", "5♦", "4♦", "3♦", "2♦"]
    shuffle(cards)
    pyramid = [ui.pushButton_1, ui.pushButton_2, ui.pushButton_3, ui.pushButton_4, ui.pushButton_5, ui.pushButton_6,
               ui.pushButton_7, ui.pushButton_8, ui.pushButton_9, ui.pushButton_10, ui.pushButton_11, ui.pushButton_12,
               ui.pushButton_13, ui.pushButton_14, ui.pushButton_15, ui.pushButton_16, ui.pushButton_17, ui.pushButton_18,
               ui.pushButton_19, ui.pushButton_20, ui.pushButton_21, ui.pushButton_22, ui.pushButton_23, ui.pushButton_24,
               ui.pushButton_25, ui.pushButton_26, ui.pushButton_27, ui.pushButton_28]
    stock = cards[28:]
    num = []
    names = []

    for i in range(28):
        pyramid[i].setText(_translate("MainWindow", cards[i]))
        #pyramid[i].setIcon(QtGui.QIcon(':/PNG/{}/.png'.format('icon_theme')))
        if "♥" in pyramid[i].text():
            #pyramid[i].setIcon(_translate("MainWindow", 'D:/PNG/{}.png'.format(cards[i])))
            #pyramid[i].setIcon(QtGui.QIcon('D:/PNG/{}.png'.format(cards[i])))
            pyramid[i].setStyleSheet("color: red")
        elif "♦" in pyramid[i].text():
            #pyramid[i].setIcon(QtGui.QIcon('D:/PNG/{}.png'.format(cards[i])))
            pyramid[i].setStyleSheet("color: red")
        else:
            #pyramid[i].setIcon(QtGui.QIcon('D:/PNG/{}.png'.format(cards[i])))
            pyramid[i].setStyleSheet("color: black")
    c.iter_stock()
    main()

    ui.show()
    sys.exit(app.exec_())
