import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import shuffle
from functools import partial

_translate = QtCore.QCoreApplication.translate


class Cards:

    def value(self, pushButton, num):
        if pushButton.isEnabled():
            if "A" in pushButton.value:
                num.append(1)
                names.append(pushButton)
            if "K" in pushButton.value:
                num.append(13)
                names.append(pushButton)
            if "Q" in pushButton.value:
                num.append(12)
                names.append(pushButton)
            if "J" in pushButton.value:
                num.append(11)
                names.append(pushButton)
            if "10" in pushButton.value:
                num.append(10)
                names.append(pushButton)
            if "9" in pushButton.value:
                num.append(9)
                names.append(pushButton)
            if "8" in pushButton.value:
                num.append(8)
                names.append(pushButton)
            if "7" in pushButton.value:
                num.append(7)
                names.append(pushButton)
            if "6" in pushButton.value:
                num.append(6)
                names.append(pushButton)
            if "5" in pushButton.value:
                num.append(5)
                names.append(pushButton)
            if "4" in pushButton.value:
                num.append(4)
                names.append(pushButton)
            if "3" in pushButton.value:
                num.append(3)
                names.append(pushButton)
            if "2" in pushButton.value:
                num.append(2)
                names.append(pushButton)
            Desk.summ(Desk, num, names, stock)

    def summ(self, num, names, stock):
        if len(names) == 2 and sum(num) != 13:
            num.clear()
            names.clear()
        elif sum(num) == 13:
            if len(names) == 1:
                if names[0] == ui.pushButton_30:
                    temp = stock.index(names[0].text())
                    del stock[stock.index(names[0].text())]
                    if temp >= len(stock):
                        temp = 0
                    ui.pushButton_30.setText(_translate("MainWindow", stock[temp]))
                    ui.pushButton_30.value = stock[temp]
                    ui.pushButton_30.setIcon(QIcon(QPixmap(f"PNG/{stock[temp]}.png")))
                    num.clear()
                    names.clear()
                    score()
                else:
                    names[0].hide()
                    num.clear()
                    names.clear()
                    score()
                    if ui.pushButton_1.isHidden():
                        winner()
                    Desk.all_cards_access(Desk, pyramid)
            elif len(names) == 2:
                # if names[0] == ui.pushButton_30 and names[1] == ui.pushButton_30:
                #     num.clear()
                #     names.clear()
                if names[0] == ui.pushButton_30:
                    temp1 = stock.index(names[0].text())
                    del stock[stock.index(names[0].text())]
                    if temp1 >= len(stock):
                        temp1 = 0
                    ui.pushButton_30.setText(_translate("MainWindow", stock[temp1]))
                    ui.pushButton_30.value = stock[temp1]
                    ui.pushButton_30.setIcon(QIcon(QPixmap(f"PNG/{stock[temp1]}.png")))
                    names[1].hide()
                    num.clear()
                    names.clear()
                    score()
                    if ui.pushButton_1.isHidden():
                        winner()
                    Desk.all_cards_access(Desk, pyramid)
                elif names[1] == ui.pushButton_30:
                    temp2 = stock.index(names[1].text())
                    del stock[stock.index(names[1].text())]
                    if temp2 >= len(stock):
                        temp2 = 0
                    ui.pushButton_30.setText(_translate("MainWindow", stock[temp2]))
                    ui.pushButton_30.value = stock[temp2]
                    ui.pushButton_30.setIcon(QIcon(QPixmap(f"PNG/{stock[temp2]}.png")))
                    names[0].hide()
                    num.clear()
                    names.clear()
                    score()
                    if ui.pushButton_1.isHidden():
                        winner()
                    Desk.all_cards_access(Desk, pyramid)
                else:
                    names[0].hide()
                    names[1].hide()
                    num.clear()
                    names.clear()
                    score()
                    if ui.pushButton_1.isHidden():
                        winner()
                    Desk.all_cards_access(Desk, pyramid)

    def all_cards_access(self, pyramid):
        row = 1
        for i in range(len(pyramid[:21])):
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
                pyramid[i].setIcon(QIcon(QPixmap(f"PNG/{cards[i]}.png")))


class Desk(Cards):

    def __init__(self, index=0):
        self.index = index

    def iter_stock(self):
        d.stock_style()
        if self.index >= len(stock):
            self.index = 0
        ui.pushButton_30.setText(_translate("MainWindow", stock[self.index]))
        ui.pushButton_30.value = stock[self.index]
        ui.pushButton_30.setStyleSheet("QPushButton{border-radius:10px;"
                                       "font: 1px;"
                                       "padding: 10px}")
        ui.pushButton_30.setIcon(QIcon(QPixmap(f"PNG/{stock[self.index]}.png")))
        self.index += 1
        score()

    def stock_style(self):
        ui.pushButton_29.setText(_translate("MainWindow", None))
        ui.pushButton_29.setIcon(QIcon(QPixmap("PNG/red_back.png")))
        ui.pushButton_30.setText(_translate("MainWindow", None))
        ui.pushButton_30.setIcon(QIcon(QPixmap(f"PNG/{stock[0]}.png")))
        ui.pushButton_29.setIconSize(QSize(125, 125))
        ui.pushButton_30.setIconSize(QSize(125, 125))

    def not_enabled_pyramid(self):
        for i in range(21):
            pyramid[i].setText(_translate("MainWindow", None))
            pyramid[i].setEnabled(False)
            pyramid[i].setIconSize(QSize(125, 125))
            pyramid[i].setIcon(QIcon(QPixmap("PNG/red_back.png")))


def score():
    ui.lcdNumber.display(ui.lcdNumber.value()+1)
    ui.lcdNumber.update()


def window_style():
    ui.setWindowTitle("Pyramid Solitaire")
    img = QImage("PNG/green-felt.png")
    palette = QPalette()
    scaled = img.scaled(ui.size(), Qt.KeepAspectRatioByExpanding)
    palette.setBrush(QPalette.Window, QBrush(scaled))
    ui.setPalette(palette)
    ui.setWindowIcon(QtGui.QIcon(os.path.join('PNG/playing-cards-icon.png')))
    ui.label.setStyleSheet("QLabel{color: white;"
                           "font: bold}")


def winner():
    ui.label.setHidden(True)
    ui.pushButton_29.setHidden(True)
    ui.pushButton_30.setHidden(True)
    ui.lcdNumber.setHidden(True)
    ui.label_2.setHidden(False)
    ui.label_3.setHidden(False)
    ui.label_2.setText(f"CONGRATULATION!\n\nYou won this game.\nYour score is {ui.lcdNumber.intValue()}\n\n"
                       f"If you want to start new game,\n press Ctrl+N")
    ui.label_2.setStyleSheet("QLabel { border-radius:10px;"
                             "background-color: black;"
                             "border-style: outset;"
                             "border-width: 2px;"
                             "border-color: red;"
                             "font: bold 22px;"
                             "color: red;"
                             "text-align:center;"
                             "}")
    movie = QMovie("PNG/giphy.gif")
    movie.setScaledSize(QtCore.QSize(ui.width(), ui.height()))
    ui.label_3.setMovie(movie)
    movie.start()


def new_game():
    global stock, num, names
    ui.label_2.setHidden(True)
    ui.label_3.setHidden(True)
    ui.label.setHidden(False)
    ui.pushButton_29.setHidden(False)
    ui.pushButton_30.setHidden(False)
    ui.lcdNumber.setHidden(False)
    shuffle(cards)
    stock = cards[28:]
    num = []
    names = []
    for i in range(28):
        pyramid[i].setText(_translate("MainWindow", None))
        pyramid[i].setIcon(QIcon(QPixmap(f"PNG/{cards[i]}.png")))
        pyramid[i].setIconSize(QSize(125, 125))
        pyramid[i].value = cards[i]
        pyramid[i].show()
    d.not_enabled_pyramid()
    d.iter_stock()
    ui.lcdNumber.display(0)
    return stock, num, names


def main():
    ui.label_2.setHidden(True)
    ui.label_3.setHidden(True)
    ui.pushButton_29.clicked.connect(d.iter_stock)
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
    d = Desk()
    app = QtWidgets.QApplication([])
    ui = uic.loadUi("window.ui")
    window_style()
    exitActionN = QAction('New game')
    exitActionN.setShortcut('Ctrl+N')
    exitActionN.triggered.connect(new_game)

    exitActionE = QAction('Exit')
    exitActionE.setShortcut('Ctrl+Q')
    exitActionE.triggered.connect(qApp.quit)

    menubar = ui.menuBar()
    fileMenu = menubar.addMenu('Menu')
    fileMenu.addAction(exitActionN)
    fileMenu.addAction(exitActionE)
    cards = ["AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
             "AD", "KD", "QD", "JD", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D",
             "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C",
             "AS", "KS", "QS", "JS", "10S", "9S", "8S", "7S", "6S", "5S", "4S", "3S", "2S"]
    shuffle(cards)
    pyramid = [ui.pushButton_1, ui.pushButton_2, ui.pushButton_3, ui.pushButton_4, ui.pushButton_5, ui.pushButton_6,
               ui.pushButton_7, ui.pushButton_8, ui.pushButton_9, ui.pushButton_10, ui.pushButton_11, ui.pushButton_12,
               ui.pushButton_13, ui.pushButton_14, ui.pushButton_15, ui.pushButton_16, ui.pushButton_17,
               ui.pushButton_18,
               ui.pushButton_19, ui.pushButton_20, ui.pushButton_21, ui.pushButton_22, ui.pushButton_23,
               ui.pushButton_24,
               ui.pushButton_25, ui.pushButton_26, ui.pushButton_27, ui.pushButton_28]
    stock = cards[28:]
    num = []
    names = []
    for i in range(28):
        pyramid[i].setText(_translate("MainWindow", None))
        pyramid[i].setIcon(QIcon(QPixmap(f"PNG/{cards[i]}.png")))
        pyramid[i].setIconSize(QSize(125, 125))
        pyramid[i].value = cards[i]
    d.not_enabled_pyramid()
    d.iter_stock()
    ui.lcdNumber.display(0)
    main()
    ui.show()
    sys.exit(app.exec_())
