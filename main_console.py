from random import shuffle


def inputt():
    spisok = []
    num = []
    c1 = int(input('Enter first position: '))
    if len(str(c1)) > 3 or str(c1).isalpha():
        print('Error.Enter a correct number')
        inputt()
    king(c1,steps)
    spisok.append(cards[c1])
    c2 = int(input('Enter second position: '))
    if len(str(c2)) > 3 or str(c2).isalpha():
        print('Error.Enter a correct number')
        inputt()
    spisok.append(cards[c2])
    Desk.input_card(Desk, num, spisok, c1, c2)
    return spisok


def king(c1, steps):
    if "K" in cards[c1]:
        cards[c1] = '**'
        steps += 1
        Cards.view(Cards, cards, stock,steps)
        inputt()


class Desk:

    def __init__(self, spisok, num, cards, stock, steps=0):
        self.spisok = spisok
        self.num = num
        self.cards = cards
        self.stock = stock
        self.steps = steps

    def input_card(self, num, spisok, c1, c2):

        for i in range(len(spisok)):
            if "A" in spisok[i]:
                num.append(1)
            if "K" in spisok[i]:
                num.append(13)
            if "Q" in spisok[i]:
                num.append(12)
            if "J" in spisok[i]:
                num.append(11)
            if '10' in spisok[i]:
                num.append(10)
            if '9' in spisok[i]:
                num.append(9)
            if '8' in spisok[i]:
                num.append(8)
            if '7' in spisok[i]:
                num.append(7)
            if '6' in spisok[i]:
                num.append(6)
            if '5' in spisok[i]:
                num.append(5)
            if '4' in spisok[i]:
                num.append(4)
            if '3' in spisok[i]:
                num.append(3)
            if '2' in spisok[i]:
                num.append(2)
        Desk.summ(Desk, num, spisok, c1, c2, steps)

    def summ(self, num, spisok, c1, c2, steps):
        if sum(num) == 13:
            cards[c1] = '**'
            cards[c2] = '**'
            steps += 1
            spisok.clear()
            Cards.view(Cards, cards, stock, steps)
            inputt()
        else:
            Cards.view(Cards, cards, stock, steps)
            inputt()

class Cards(Desk):

    def view(self, cards, stock, steps):
        print(f'              {cards[0]}\n'
              f'            {cards[1]}  {cards[2]}\n'
              f'          {cards[3]}  {cards[4]}  {cards[5]}\n'
              f'        {cards[6]}  {cards[7]}  {cards[8]}  {cards[9]}\n'
              f'      {cards[10]}  {cards[11]}  {cards[12]}  {cards[13]}  {cards[14]}\n'
              f'    {cards[15]}  {cards[16]}  {cards[17]}  {cards[18]}  {cards[19]}  {cards[20]}\n'
              f'  {cards[21]}  {cards[22]}  {cards[23]}  {cards[24]}  {cards[25]}  {cards[26]}  {cards[27]}\n'
              f'STOCK: {stock[0]}                              SCORE: {steps}')


if __name__ == "__main__":
    steps = 0
    cards = ["AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
             "AP", "KP", "QP", "JP", "10P", "9P", "8P", "7P", "6P", "5P", "4P", "3P", "2P",
             "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C",
             "AT", "KT", "QT", "JT", "10T", "9T", "8T", "7T", "6T", "5T", "4T", "3T", "2T"]
    shuffle(cards)
    stock = cards[28:]
    Cards.view(Cards, cards, stock, steps)
    inputt()
