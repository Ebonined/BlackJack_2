suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
from random import shuffle

class Profile():
    numtot = 0

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.playercards = []

    def deposite(self, stake, percent):
        out = (stake * percent) + stake
        self.money = self.money + out
        return out

    def stake(self, amount):
        self.money = self.money - amount
        return amount
    
    def card(self, card):
        self.playercards.append(card)
        ace_count = 0
        if card.rank != 'Ace':
            self.numtot += values[card.rank]
        if card.rank == 'Ace':
            ace_count += 1
        if ace_count > 0:
            for x in range(ace_count):
                x
                if self.numtot < 21 and 21-self.numtot < 11:
                    self.numtot += 1
                elif self.numtot < 21 and 21-self.numtot >= 11:
                    self.numtot += 11
                else:
                    self.numtot += 1
    
    def check_bust(self):
        if self.numtot == 21:
            return 'BJ'
        elif self.numtot > 21:
            return 'B'
        else:
            return 'NB'
    
    def reset(self):
        self.playercards = []
        self.numtot = 0
    
    def __str__(self):
        return 'Name: {}, balance: {}'.format(self.name, self.money)

class CompProfile:
    numtot = 0

    def __init__(self):
        self.playercards = []
    
    def card(self, card):
        self.playercards.append(card)
        ace_count = 0
        if card.rank != 'Ace':
            self.numtot += values[card.rank]
        if card.rank == 'Ace':
            ace_count += 1
        if ace_count > 0:
            for x in range(ace_count):
                x
                if self.numtot < 21 and 21-self.numtot < 11:
                    self.numtot += 1
                elif self.numtot < 21 and 21-self.numtot >= 11:
                    self.numtot += 11
                else:
                    self.numtot += 1
    def check_bust(self):
        if self.numtot == 21:
            return 'BJ'
        elif self.numtot > 21:
            return 'B'
        else:
            return 'NB'
            
    def reset(self):
        self.playercards = []
        self.numtot = 0
    
class Card:

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
    
    def display(self):
        return [self.rank, self.suit]
    
    def __str__(self):
        return self.rank +' of '+ self.suit

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))
    
    def card_shuffle(self):
        shuffle(self.deck)
        
    def card_remove(self):
        """
        removes the first card on the deck of cards and returns the removed card
        """
        return self.deck.pop(0)
    
    def __str__(self):
        test_card  = ''
        for x in self.deck:
            test_card += x.rank+' of '+x.suit+'\n'
        return test_card

def card_display(card_list):
    first_row = ''
    second_row = ''
    main_list = []
    for index in card_list:
        temp_list = []
        temp_list.append(index.rank)
        temp_list.append(index.suit)
        main_list.append(temp_list)
    for index in main_list:
        for enum, index2 in enumerate(index):
            if enum == 0:
                app = str_out(index2, 13)
                first_row += app
            elif enum == 1:
                app = str_out(index2, 13)
                second_row += app
    return first_row+'\n'+second_row


def str_out(item='daniel', lent=13):
    item = str(item)
    from math import modf
    marg = lent - 2
    item_lenght = len(item)
    cor = marg - item_lenght
    if cor%2 == 0:
        cor1 = int(cor/2)
        cor2 = cor1
    elif cor%2 != 0:
        cor1 = int(modf(cor/2)[1])
        cor2 = cor1 + 1
    prin = '|'+cor1*' '+item+' '*cor2+'|'
    return prin

def print_card(comp, player, show_comp = False): # Function to print cards of both player and dealer
    """
    Function to print cards of both player and dealer
    """
    print('\n'*2)
    print('-'*50)
    print(card_display(comp.playercards))
    if show_comp == True:
        print(comp.numtot)
    elif show_comp == False:
        pass
    print('\n\n')
    print(card_display(player.playercards))
    print(player.numtot)
    print('-'*50)


if __name__ == '__main__':
    player = Profile('Daniel', 20000)
    print(player)
    player.stake(800)
    print(player)
    player.deposite(800, 1.5)
    print(player)
    player.card(Card('Ace', 'Heart'))
    player.card(Card('Ace', 'Heart'))
    print(player.numtot)

    card = Card('Two','Diamonds')
    print(card, card.display())
    print(str_out())

 #   test_deck = Deck()
 #   print(test_deck)
    