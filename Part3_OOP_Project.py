# For this project you will be using OOP to create a card game. This card game will 
# be the card game "War" for two players, you and the computer. If you don't know 
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card takes
# both cards and puts them, face down, on the bottom of his stack
#
# If the cards are the same rank, it is War. Each player turns up three cards face down 
# and one card face up. The player with the higher cards takes both piles (six cards). If the 
# turned-up cards are again the same rank, each player places another card face down and turns
# another card face up. The player with the higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
#https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards
SUITES = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck():
    """
    THis is the Deck Class. THis object will create a deck of cards to initiate play.
    You can then use this Deck list of cards to split in half and give to the players. 
    It will use SUITE and RANKS to create the deck. It should also have a method for 
    splitting/cutting the deck in half and Shuffling the deck.
    """
    
    def __init__(self):
        print("Creating New Ordered Deck!")
        self.allcards = [(s,r) for s in SUITES for r in RANKS]
        
    
    def cutting(self):
        return (self.allcards[:26],self.allcards[26:])


    def shuffling(self):
        print("Shuffling the deck")
        shuffle(self.allcards)
        return 

class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove cards from that hand.
    There should be an add and remove card method here.
    """
    def __init__(self, cards):
        self.cards = cards
    def __str__(self):
        return "Contain {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)
    def remove(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand class object.
    The Player can then play can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    def play_card(self):
        drawn_card = self.hand.remove()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove())
                return war_cards
    
    def still_has_cards(self):
        """
        return True if player still has cards left
        """
        return len(self.hand.cards) != 0

###########
#GAME PLAY#
###########

print("Welcome to War, let's begin")
#Create new deck and split it in half
d = Deck()
d.shuffling()
half1, half2 = d.cutting()



# create both players!
comp = Player("Computer", Hand(half1))
user = Player('dfs', Hand(half2))


total_rounds = 0
war_count = 0
while comp.still_has_cards() and user.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("here are the current standing")
    print(user.name +"has the count:" + str(len(user.hand.cards)))
    print(comp.name +"has the count:" + str(len(comp.hand.cards)))
    print("play a card!")
    print('\n')
    table_cards = []
    compcard = comp.play_card()
    p1card = user.play_card()
    table_cards.append(compcard)
    table_cards.append(p1card)
    if compcard[1] == p1card[1] :
        war_count += 1
        print("war!")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        if RANKS.index(compcard[1]) < RANKS.index(p1card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if compcard[1] < p1card[1]:
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)


print("game over, number of rounds:" + str(total_rounds))
print("a war happended"+ str(war_count)+"times")