class Point:
    'class that represents a point in the plane'

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        # to be implemented

    def get(self):
        'return coordinates of the point as a tuple'
        # to be implemented

    def move(self, dx, dy):
        'change the x and y coordinates by dx and dy'
        self.x += dx
        self.y += dy
        
class Animal:
    pass

def setSpecies(self, species):
    'sets the animal species'
    pass

def setLanguage(self, language):
    'sets the animal language'
    pass

def speak(self):
    'prints a sentence by the animal'
    pass
        
        
class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        pass

    def getRank(self):
        'return rank'
        pass

    def getSuit(self):
        'return suit'
        pass
        
        
class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        #self.deck = [] # deck is initially empty
        pass


    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        pass

    def shuffle(self):
        'shuffle the deck'
        pass
        
class Queue:
    'a classic queue class'

    def __init__(self):
        'instantiates an empty list'
        # initialize empty list

    def isEmpty(self):
        'returns True if empty, False otherwise'
        # return length == 0 test

    def enqueue (self, item):
        'insert item at rear of queue'
        # append and return

    def dequeue(self):
        'remove and return item at front of queue'
        # pop and return