import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import shuffle
from functools import partial


_translate = QtCore.QCoreApplication.translate

class Desk:
    def value(self, pushButton, num):
        if pushButton.isEnabled():
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
            Desk.summ(Desk, num, names, pushButton, stock)

    def summ(self, num, names, pushButton, stock):

        if len(names) == 2 and sum(num) != 13:
            num.clear()
            names.clear()
        elif sum(num) == 13:
            if len(names) == 1:
                if names[0] == ui.pushButton_30:
                    temp = stock.index(names[0].text())
                    del stock[stock.index(names[0].text())]
                    ui.pushButton_30.setText(stock[temp])
                else:
                    names[0].hide()
                    num.clear()
                    names.clear()
                    Desk.all_cards_access(Desk, pyramid)
            elif len(names) == 2:
                if names[0] == ui.pushButton_30:
                    temp1 = stock.index(names[0].text())
                    del stock[stock.index(names[0].text())]
                    ui.pushButton_30.setText(stock[temp1])
                    names[1].hide()
                    num.clear()
                    names.clear()
                    Desk.all_cards_access(Desk, pyramid)
                elif names[1] == ui.pushButton_30:
                    temp2 = stock.index(names[1].text())
                    del stock[stock.index(names[1].text())]
                    ui.pushButton_30.setText(stock[temp2])
                    names[0].hide()
                    num.clear()
                    names.clear()
                    Desk.all_cards_access(Desk, pyramid)
                else:
                    names[0].hide()
                    names[1].hide()
                    num.clear()
                    names.clear()
                    Desk.all_cards_access(Desk, pyramid)

    def all_cards_access(self, pyramid):
        row = 1
        for i in range(len(pyramid[:21])):
            if not pyramid[i].isEnabled():
                if i == 1:
                    row += 1
                if i == 3:
                    row += 1
                if i == 6:
                    row += 1
                if i == 10:
                    row += 1
                if i == 15:
                    row += 1
                if i == 21:
                    row += 1
                if pyramid[i + row].isHidden() and pyramid[i + row + 1].isHidden():
                    pyramid[i].setEnabled(True)
                    pyramid[i].setIcon(QIcon(None))
                    pyramid[i].setText(_translate("MainWindow", cards[i]))

    # def score(self, pushButton):
    #     if Desk.value(Desk, pushButton) == 13:
    #         pass


class Cards(Desk):
    def __init__(self, index=0):
        self.index = index

    def iter_stock(self):
        if self.index == len(stock):
            self.index = 0
        stock_style()
        ui.pushButton_30.setText(_translate("MainWindow", stock[self.index]))
        self.index += 1

def not_enabled_pyramid():
    # icon = QIcon()
    # icon.addPixmap(QPixmap("red_back.png"), QIcon.Active, QIcon.Off)
    for i in range(21):
        pyramid[i].setText(_translate("MainWindow", None))
        pyramid[i].setEnabled(False)
        pyramid[i].setIconSize(QSize(125, 125))
        pyramid[i].setIcon(QIcon("PNG/red_back.png"))
        # pyramid[i].setIcon(icon)

        # icon.addPixmap(QPixmap(graphics_dir+name+".png"), QIcon.Normal, QIcon.Off)


def stock_style():
    ui.pushButton_29.setText(_translate("MainWindow", None))
    ui.pushButton_29.setIcon(QIcon("PNG/red_back.png"))
    # ui.pushButton_30.setText(_translate("MainWindow", None))
    ui.pushButton_29.setIconSize(QSize(125, 125))
    ui.pushButton_30.setIconSize(QSize(125, 125))


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
    ui.setWindowIcon(QtGui.QIcon(os.path.join(base_dir, 'PNG/green_felt.jpg')))  # must be in ico format
    n = QtCore.QPoint(120, 40)
    cards = ["AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
             "AD", "KD", "QD", "JD", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D",
             "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C",
             "AS", "KS", "QS", "JS", "10S", "9S", "8S", "7S", "6S", "5S", "4S", "3S", "2S"]
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
    not_enabled_pyramid()
    c.iter_stock()
    main()
    ui.show()
    sys.exit(app.exec_())
