import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from random import shuffle
from functools import partial

_translate = QtCore.QCoreApplication.translate


class Cards:
    def __init__(self, index=0):
        self.index = index


    def iter_stack(self):
        if self.index == len(stack):
            self.index = 0
        ui.pushButton_30.setText(_translate("MainWindow", stack[self.index]))
        if "♥" in ui.pushButton_30.text():
            ui.pushButton_30.setStyleSheet("color: red")
        elif "♦" in ui.pushButton_30.text():
            ui.pushButton_30.setStyleSheet("color: red")
        else:
            ui.pushButton_30.setStyleSheet("color: black")
        self.index += 1


class Desk:
    def value(self,pushButton):
        if "A" in pushButton.text():

            return 1
        if "K" in pushButton.text():

            return 13
        if "Q" in pushButton.text():

            return 12
        if "J" in pushButton.text():

            return 11
        if "10" in pushButton.text():

            return 10
        if "9" in pushButton.text():

            return 9
        if "8" in pushButton.text():

            return 8
        if "7" in pushButton.text():

            return 7
        if "6" in pushButton.text():

            return 6
        if "5" in pushButton.text():

            return 5
        if "4" in pushButton.text():

            return 4
        if "3" in pushButton.text():

            return 3
        if "2" in pushButton.text():

            return 2

    def score(self, pushButton):
        if Desk.value(Desk, pushButton) == 13:
            pass

def main():
    ui.pushButton_29.clicked.connect(c.iter_stack)
    ui.pushButton.clicked.connect(partial(Desk.value, Desk, ui.pushButton))
    ui.pushButton_2.clicked.connect(partial(Desk.value, Desk, ui.pushButton_2))
    ui.pushButton_3.clicked.connect(partial(Desk.value, Desk, ui.pushButton_3))
    ui.pushButton_4.clicked.connect(partial(Desk.value, Desk, ui.pushButton_4))
    ui.pushButton_5.clicked.connect(partial(Desk.value, Desk, ui.pushButton_5))
    ui.pushButton_6.clicked.connect(partial(Desk.value, Desk, ui.pushButton_6))
    ui.pushButton_7.clicked.connect(partial(Desk.value, Desk, ui.pushButton_7))
    ui.pushButton_8.clicked.connect(partial(Desk.value, Desk, ui.pushButton_8))
    ui.pushButton_9.clicked.connect(partial(Desk.value, Desk, ui.pushButton_9))
    ui.pushButton_10.clicked.connect(partial(Desk.value, Desk, ui.pushButton_10))
    ui.pushButton_11.clicked.connect(partial(Desk.value, Desk, ui.pushButton_11))
    ui.pushButton_12.clicked.connect(partial(Desk.value, Desk, ui.pushButton_12))
    ui.pushButton_13.clicked.connect(partial(Desk.value, Desk, ui.pushButton_13))
    ui.pushButton_14.clicked.connect(partial(Desk.value, Desk, ui.pushButton_14))
    ui.pushButton_15.clicked.connect(partial(Desk.value, Desk, ui.pushButton_15))
    ui.pushButton_16.clicked.connect(partial(Desk.value, Desk, ui.pushButton_16))
    ui.pushButton_17.clicked.connect(partial(Desk.value, Desk, ui.pushButton_17))
    ui.pushButton_18.clicked.connect(partial(Desk.value, Desk, ui.pushButton_18))
    ui.pushButton_19.clicked.connect(partial(Desk.value, Desk, ui.pushButton_19))
    ui.pushButton_20.clicked.connect(partial(Desk.value, Desk, ui.pushButton_20))
    ui.pushButton_21.clicked.connect(partial(Desk.value, Desk, ui.pushButton_21))
    ui.pushButton_22.clicked.connect(partial(Desk.value, Desk, ui.pushButton_22))
    ui.pushButton_23.clicked.connect(partial(Desk.value, Desk, ui.pushButton_23))
    ui.pushButton_24.clicked.connect(partial(Desk.value, Desk, ui.pushButton_24))
    ui.pushButton_25.clicked.connect(partial(Desk.value, Desk, ui.pushButton_25))
    ui.pushButton_26.clicked.connect(partial(Desk.value, Desk, ui.pushButton_26))
    ui.pushButton_27.clicked.connect(partial(Desk.value, Desk, ui.pushButton_27))
    ui.pushButton_28.clicked.connect(partial(Desk.value, Desk, ui.pushButton_28))
    ui.pushButton_30.clicked.connect(partial(Desk.value, Desk, ui.pushButton_30))


if __name__ == "__main__":
    c = Cards()
    app = QtWidgets.QApplication([])
    ui = uic.loadUi("window.ui")
    cards = ["A♥", "K♥", "Q♥", "J♥", "10♥", "9♥", "8♥", "7♥", "6♥", "5♥", "4♥", "3♥", "2♥",
             "A♠", "K♠", "Q♠", "J♠", "10♠", "9♠", "8♠", "7♠", "6♠", "5♠", "4♠", "3♠", "2♠",
             "A♣", "K♣", "Q♣", "J♣", "10♣", "9♣", "8♣", "7♣", "6♣", "5♣", "4♣", "3♣", "2♣",
             "A♦", "K♦", "Q♦", "J♦", "10♦", "9♦", "8♦", "7♦", "6♦", "5♦", "4♦", "3♦", "2♦"]
    shuffle(cards)
    piramyd = [ui.pushButton, ui.pushButton_2, ui.pushButton_3, ui.pushButton_4, ui.pushButton_5, ui.pushButton_6,
             ui.pushButton_7, ui.pushButton_8, ui.pushButton_9, ui.pushButton_10, ui.pushButton_11, ui.pushButton_12,
             ui.pushButton_13, ui.pushButton_14, ui.pushButton_15, ui.pushButton_16, ui.pushButton_17, ui.pushButton_18,
             ui.pushButton_19, ui.pushButton_20, ui.pushButton_21, ui.pushButton_22, ui.pushButton_23, ui.pushButton_24,
             ui.pushButton_25, ui.pushButton_26, ui.pushButton_27, ui.pushButton_28]
    stack = cards[28:]
    for i in range(28):
        piramyd[i].setText(_translate("MainWindow", cards[i]))
        if "♥" in piramyd[i].text():
            piramyd[i].setStyleSheet("color: red")
        elif "♦" in piramyd[i].text():
            piramyd[i].setStyleSheet("color: red")
        else:
            piramyd[i].setStyleSheet("color: black")
    c.iter_stack()
    main()
    ui.show()
    sys.exit(app.exec_())
