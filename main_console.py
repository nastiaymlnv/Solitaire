from random import shuffle
import sys


class Desk:

    def __init__(self, spisok, num, access, cards, steps, row):
        self.spisok = spisok
        self.num = num
        self.cards = cards
        self.steps = steps
        self.access = access
        self.row = row

    def input_card(self, num, spisok, c1, c2, access):
        """Method that checks cards values (spisok list) if they in list of unblocked cards (access list).
         Then inserts into the list of sum of numbers (num list)."""
        for i in range(len(spisok)):
            if cards.index(spisok[i]) in access:
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
        Desk.summ(Desk, num, spisok, c1, c2, access)

    def summ(self, num, spisok, c1, c2, access):
        """Method that counts the amount of two numbers in sum list and deletes cards positions in the pyramid. """
        global click_stock, len_stack
        if sum(num) == 13:
            global steps
            steps += 1
            if c1 >= 28:    #cards in the stock
                #cards.pop(click_stock)
                cards[click_stock] = '##'
                len_stack -= 1
                click_stock += 1
                if click_stock == len(cards):
                    click_stock = len(cards) - len_stack
                cards[c2] = '##'
            if c2 >= 28:    #cards in the stock
                cards.pop(click_stock)
                len_stack -= 1
                click_stock += 1
                if click_stock == len(cards):
                    click_stock = len(cards) - len_stack
                cards[c1] = '##'
            if c2 == -1:    #if the variable is a king
                cards[c1] = '##'
            if c1 < 28 and c2 < 28:    #cards in the pyramid
                cards[c1] = '##'
                cards[c2] = '##'
            spisok.clear()
            num.clear()
            if cards[0] == '**':
                print("--- C O N G R A T ' S ---\n"
                      "   --- Y O U  W O N ---")
                quit()
            Cards.view(Cards, cards)
            inputt()
        else:
            Cards.view(Cards, cards)
            inputt()


class Cards(Desk):

    def view(self, cards):
        """Method for representation the card pyramid in the desk."""
        global steps, click_stock, len_stack
        while 1:
            if cards[click_stock] == '##':
                click_stock += 1
                if click_stock == len(cards):  #returns stock into the start
                    click_stock = len(cards) - len_stack
            break
        print(f'              {cards[0]}                        SCORE: {steps}\n'
              f'            {cards[1]}  {cards[2]}\n'
              f'          {cards[3]}  {cards[4]}  {cards[5]}\n'
              f'        {cards[6]}  {cards[7]}  {cards[8]}  {cards[9]}\n'
              f'      {cards[10]}  {cards[11]}  {cards[12]}  {cards[13]}  {cards[14]}\n'
              f'    {cards[15]}  {cards[16]}  {cards[17]}  {cards[18]}  {cards[19]}  {cards[20]}\n'
              f'  {cards[21]}  {cards[22]}  {cards[23]}  {cards[24]}  {cards[25]}  {cards[26]}  {cards[27]}\n\n'
              f'STOCK: {cards[click_stock]} (press 99 to use, 88 to continue)\n'
              f'00 - exit')

    def all_cards_access(self, access, c1, c2, num, spisok):
        """Method for checking the position of card and entering to the list with unblocked card positions."""
        if c1 == click_stock:
            access.append(c1)
        elif c2 == click_stock:
            access.append(c2)
        row = 1
        for i in range(len(cards[:21])):
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
                if cards[i + row] == "##" and cards[i + row + 1] == "##":
                    access.append(i)
        Desk.input_card(Desk, num, spisok, c1, c2, access)


def inputt():
    """Method which respond about input."""
    global steps, click_stock, len_stack
    access = [21, 22, 23, 24, 25, 26, 27]
    spisok = []
    num = []
    while 1:
        try:
            c1 = int(input('Enter first position: '))
            break
        except ValueError:
            pass
    if c1 == 00:
        sys.exit('--- Bye:) ---')
    if c1 == 88:
        steps += 1
        click_stock += 1
        if click_stock == len(cards):
            click_stock = len(cards) - len_stack
        Cards.view(Cards, cards)
        inputt()
    elif c1 == 99:
        if 'K' in cards[click_stock]:
            steps += 1
            cards.pop(click_stock)
            click_stock += 1
            if click_stock == len(cards):
                click_stock = len(cards) - len_stack
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
            if "K" in cards[c1]:
                c2 = -1
                spisok.append(cards[c1])
                Cards.all_cards_access(Cards, access, c1, c2, num, spisok)
                if c1 in access:
                    cards[c1] = "##"
                    access.append(c1)
                    steps += 1
                    Cards.view(Cards, cards)
                    inputt()
                else:
                    Cards.view(Cards, cards)
                    inputt()
            else:
                spisok.append(cards[c1])
    while 1:
        try:
            c2 = int(input('Enter second position: '))
            break
        except ValueError:
            pass
    if c2 == 88:
        if click_stock == len(cards):
            click_stock = len(cards) - 28
        else:
            steps += 1
            click_stock += 1
            if click_stock == len(cards):
                click_stock = len(cards) - len_stack
            Cards.view(Cards, cards)
            inputt()
    elif c2 == 99:
        if 'K' in cards[click_stock]:
            steps += 1
            cards.pop(click_stock)
            click_stock += 1
            if click_stock == len(cards):
                click_stock = len(cards) - len_stack
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
    Desk.input_card(Desk, num, spisok, c1, c2, access)
    return spisok


if __name__ == "__main__":
    click_stock = 28    #count of clicks on the stock
    len_stack = 24      #length of the stock
    steps = 0
    cards = ["AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
             "AP", "KP", "QP", "JP", "10P", "9P", "8P", "7P", "6P", "5P", "4P", "3P", "2P",
             "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C",
             "AT", "KT", "QT", "JT", "10T", "9T", "8T", "7T", "6T", "5T", "4T", "3T", "2T"]
    shuffle(cards)
    Cards.view(Cards, cards)
    inputt()
