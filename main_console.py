from random import shuffle


class Desk:

    def __init__(self, spisok, num, access, cards, steps, row):
        self.spisok = spisok
        self.num = num
        self.cards = cards
        self.steps = steps
        self.access = access
        self.row = row

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
        Desk.summ(Desk, num, spisok, c1, c2)

    def summ(self, num, spisok, c1, c2):
        if sum(num) == 13:
            global steps
            steps += 1
            if c1 == 99:
                cards.pop(click_stock)
                click_stock += 1
            else:
                cards[c2] = '**'
            if c2 == 99:
                cards.pop(click_stock)
                click_stock += 1
            else:
                cards[c1] = '**'
            spisok.clear()
            Cards.view(Cards, cards)
            inputt()
        else:
            Cards.view(Cards, cards)
            inputt()


class Cards(Desk):

    def view(self, cards):
        global steps
        print(f'              {cards[0]}                        SCORE: {steps}\n'
              f'            {cards[1]}  {cards[2]}\n'
              f'          {cards[3]}  {cards[4]}  {cards[5]}\n'
              f'        {cards[6]}  {cards[7]}  {cards[8]}  {cards[9]}\n'
              f'      {cards[10]}  {cards[11]}  {cards[12]}  {cards[13]}  {cards[14]}\n'
              f'    {cards[15]}  {cards[16]}  {cards[17]}  {cards[18]}  {cards[19]}  {cards[20]}\n'
              f'  {cards[21]}  {cards[22]}  {cards[23]}  {cards[24]}  {cards[25]}  {cards[26]}  {cards[27]}\n\n'
              f'STOCK: {cards[click_stock]} (press 99 to use, 88 to continue)')

    def all_cards_access(self, access, c1, c2, num, spisok):
        if c1 == click_stock or c1 == 21 or c1 == 22 or c1 == 23 or c1 == 24 or c1 == 25 or c1 == 26 or c1 == 27 and \
                c2 == click_stock or c2 == 21 or c2 == 22 or c2 == 23 or c2 == 24 or c2 == 25 or c2 == 26 or c2 == 27:
            access.append(c1)
            access.append(c2)
            Desk.input_card(Desk, num, spisok, c1, c2)

        row = 0
        for i in range(len(cards)):
            if i == 0:
                row += 1
            if i == 2:
                row += 1
            if i == 5:
                row += 1
            if i == 9:
                row += 1
            if i == 14:
                row += 1
            if i == 20:
                row += 1
            if cards[i + row] == "**" and cards[i + row + 1] == "**":
                access.append(i)
            else:
                print('One of cards is not avaliable')
                Cards.view(Cards, cards)
                inputt()


def inputt():
    global steps
    global click_stock
    access = []
    spisok = []
    num = []
    c1 = int(input('Enter first position: '))
    if c1 == 88:
        if click_stock > len(cards):
            click_stock = 28
        else:
            steps += 1
            click_stock += 1
            Cards.view(Cards, cards)
            inputt()
    elif c1 == 99:
        if 'K' in cards[click_stock]:
            steps += 1
            cards.pop(click_stock)
            click_stock += 1
            Cards.view(Cards, cards)
            inputt()
        else:
            c1 = click_stock
            spisok.append(cards[c1])
    else:
        if c1 >= 28 or str(c1).isalpha():
            print('Error.Enter a correct number')
            inputt()
        else:
            c2=0
            king(c1, c2, access, num, spisok)
            spisok.append(cards[c1])
    c2 = int(input('Enter second position: '))
    if c2 == 88:
        if click_stock > 53:
            click_stock = 28
        else:
            steps += 1
            click_stock += 1
            Cards.view(Cards, cards)
            inputt()
    elif c2 == 99:
        if 'K' in cards[click_stock]:
            steps += 1
            cards.pop(click_stock)
            click_stock += 1
            Cards.view(Cards, cards)
            inputt()
        else:
            c2 = click_stock
            spisok.append(cards[c2])
    else:
        if c2 >= 28 or str(c2).isalpha():
            print('Error.Enter a correct number')
            inputt()
        else:
            spisok.append(cards[c2])
    Cards.all_cards_access(Cards, access, c1, c2, num, spisok)
    Desk.input_card(Desk, num, spisok, c1, c2)
    return spisok


def king(c1, c2, access, num, spisok):
    if "K" in cards[c1]:
        global steps
        if c1 == 21 or c1 == 22 or c1 == 23 or c1 == 24 or \
                c1 == 25 or c1 == 26 or c1 == 27:
            access.append(cards[c1])
            steps += 1
            cards[c1] = '**'
            Cards.view(Cards, cards)
            inputt()
        else:
            Cards.all_cards_access(Cards, access, c1, c2, num, spisok)


if __name__ == "__main__":
    click_stock = 28
    steps = 0
    cards = ["AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
             "AP", "KP", "QP", "JP", "10P", "9P", "8P", "7P", "6P", "5P", "4P", "3P", "2P",
             "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C",
             "AT", "KT", "QT", "JT", "10T", "9T", "8T", "7T", "6T", "5T", "4T", "3T", "2T"]
    shuffle(cards)
    Cards.view(Cards, cards)
    inputt()
