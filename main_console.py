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
            if cards.index(spisok[i]) in access:  # if card value(in cards list) is in access list (i is index of spisok list)
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
        """Method that counts the amount of two numbers in sum list and
        after that deletes cards positions in the pyramid. """
        global click_stock, len_stack
        if sum(num) == 13:
            global steps
            steps += 1
            if c1 >= 28:  # the amoumt of cards in the stock
                cards[click_stock] = '  '  # replaces card with index c1 in stock to the '  '
                len_stack -= 1  # decreases the length of the stock
                click_stock += 1  # moves into the next element on the stock
                if click_stock == len(cards):  # if the stock index is equal to the length of cards (52)
                    click_stock = len(cards) - len_stack  # then returns the stock to the start
                cards[c2] = '  '  # replaces card in pyramid to the '  '
            if c2 >= 28:
                cards[click_stock] = '  '
                len_stack -= 1
                click_stock += 1
                if click_stock == len(cards):
                    click_stock = len(cards) - len_stack
                cards[c1] = '  '
            if c2 == -1:  # if the variable is a king
                cards[c1] = '  '
            if c1 < 28 and c2 < 28:  # cards in the pyramid
                cards[c1] = '  '
                cards[c2] = '  '
            spisok.clear()
            num.clear()
            if cards[0] == '  ':  # if pyramid is empty
                sys.exit(f"#############################################\n"
                         f"#   I F  Y O U  S E E  T H i S  T E X T ,   #\n"
                         f"#  Y O U  A R E  A  L U C K Y  P E R S O N  #\n"
                         f"#    --- C O N G R A T U L A T I O N ---    #\n"
                         f"#           --- Y O U  W O N ---            #\n"
                         f"#         Y O U R  S C O R E : {steps}          #\n"
                         f"#############################################")
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
            if cards[click_stock] == '  ':  # if empty elements are in the stock,
                click_stock += 1  # it moves into the next element into the stock
                if click_stock == len(cards):  # returns the stock into the start
                    click_stock = len(cards) - len_stack
            break
        print(f'\n'
              f'                          {cards[0]}[0]                        SCORE: {steps}\n'
              f'                      {cards[1]}[1]   {cards[2]}[2]\n'
              f'                  {cards[3]}[3]   {cards[4]}[4]   {cards[5]}[5]\n'
              f'              {cards[6]}[6]   {cards[7]}[7]   {cards[8]}[8]   {cards[9]}[9]\n'
              f'          {cards[10]}[10]  {cards[11]}[11]  {cards[12]}[12] {cards[13]}[13]  {cards[14]}[14]\n'
              f'      {cards[15]}[15]  {cards[16]}[16]  {cards[17]}[17]  {cards[18]}[18]  {cards[19]}[19]  {cards[20]}[20]\n'
              f'  {cards[21]}[21]  {cards[22]}[22]  {cards[23]}[23]  {cards[24]}[24]  {cards[25]}[25]  {cards[26]}[26]  {cards[27]}[27]\n\n'
              f'STOCK: {cards[click_stock]} (press 99 to use, 88 to continue)\n'
              f'00 - exit  77 - rules')

    def all_cards_access(self, access, c1, c2, num, spisok):
        """Method for checking the position of card and entering to the list with unblocked card positions."""
        if c1 == click_stock:  # if the input card is in the stock, appends into the access list
            access.append(c1)
        elif c2 == click_stock:
            access.append(c2)
        row = 1
        for i in range(len(cards[:21])):  # checks the position of our element in the pyramid if it is not blocked
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
            if cards[i + row] == '  ' and cards[i + row + 1] == '  ':
                access.append(i)
        Desk.input_card(Desk, num, spisok, c1, c2, access)


def inputt():
    """Method which respond about input."""
    global steps, click_stock, len_stack
    access = [21, 22, 23, 24, 25, 26, 27]
    spisok = []  # the list with positions
    num = []  # the list with values
    while 1:
        try:
            c1 = int(input('Enter first position: '))
            break
        except ValueError:
            pass
    if c1 == 00:
        sys.exit('--- Bye:) ---')
    if c1 == 77:
        print(f'R U L E S:\n'
              f'The object of the game is to remove pairs of cards that add up to the total of the highest card\n'
              f'in the deck from a pyramid arrangement of 28 cards. When using the standard 52-card deck,\n'
              f'Jacks value at 11, Queens 12, and Kings 13. So the highest value is 13.\n'
              f'Playing with a 48-card Spanish deck the highest numbers are also the Kings at 13,\n'
              f'so the pairs must add up to 13. To set up the pyramid,\n'
              f'one card is dealt face up at the top of the playing area,\n'
              f'then two cards beneath and partially covering it, then three beneath them, and\n'
              f'so on completing with a row of seven cards for a total of 28 cards dealt (or six rows of 21 cards).\n'
              f'The remaining cards are placed to the side face down. This is the Stock.\n'
              f'To play, pairs of exposed cards can be removed to the Foundation if their values total 13\n'
              f'(12 if using the Spanish deck). Thus, kings can be removed immediately to the Foundation.\n'
              f'Cards must not be covered. Thus when an Ace rests on a Queen, that Queen can not be removed.\n'
              f'You may draw cards from the Stock one at a time and match it with any exposed card.\n'
              f'If no match is made the drawn Stock card is still discarded into the Foundation.\n'
              f'Once the Stock is exhausted and/or no more pairs can be made, the game ends.\n'
              f'To be considered won, all cards (cards from the pyramid and cards from the stock) '
              f'must be moved to the foundation;\n'
              f'the game cannot be won if at least two cards cannot be moved from the stock.\n'
              f'The pyramid is demolished by the end, if it stands you lose.')
        Cards.view(Cards, cards)
        inputt()
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
            cards[click_stock] = '  '
            len_stack -= 1
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
            # print('Error.Enter a correct number')
            inputt()
        else:
            if "K" in cards[c1]:
                c2 = -1
                spisok.append(cards[c1])
                Cards.all_cards_access(Cards, access, c1, c2, num, spisok)
                if c1 in access:
                    cards[c1] = '  '
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
            cards[click_stock] = '  '
            len_stack -= 1
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
    click_stock = 28  # count of clicks on the stock
    len_stack = 24  # length of the stock
    steps = 0
    cards = ["AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
             "AP", "KP", "QP", "JP", "10P", "9P", "8P", "7P", "6P", "5P", "4P", "3P", "2P",
             "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C",
             "AT", "KT", "QT", "JT", "10T", "9T", "8T", "7T", "6T", "5T", "4T", "3T", "2T"]
    shuffle(cards)
    Cards.view(Cards, cards)
    inputt()
