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
        # to be implemented
        
        
class Point:
    'class that represents a point in the plane'

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'return coordinates of the point as a tuple'
        return (self.x, self.y)

    def move(self, dx, dy):
        'change the x, y coordinates by dx, dy'
        self.x += dx
        self.y += dy

class Point:
    'class that represents a point in the plane'

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'return coordinates of the point as a tuple'
        return (self.x, self.y)

    def move(self, dx, dy):
        'change the x,y coordinates by dx,dy'
        self.x += dx
        self.y += dy

    def getx(self):
        'return x coordinate of the point'
        return self.x

        
class Point:

    def setx(self, xcoord):
        self.x = xcoord

    def sety(self, ycoord):
        self.y = ycoord

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
class ClassName:
    classVariableName1 = value1
    classVariableName2 = value2
    ...
    def methodName(self, arg11, arg12, ...):
        statements

    def methodName(self, arg21, arg22, ...):
        statements
    ...

>>> help(Point)
Help on class Point in module __main__:

class Point(builtins.object)
 |  Methods defined here:
 |  
 |  get(self)
 |  
 |  move(self, dx, dy)
 |  
 |  setx(self, xcoord)
 |  
 |  sety(self, ycoord)
 |  
 |  -----------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>> help(Point)
Help on class Point in module __main__:

class Point(builtins.object)
 |  class that represents a point in the plane
 |  
 |  Methods defined here:
 |  
 |  get(self)
 |      return coordinates of the point as a tuple
 |  
 |  move(self, dx, dy)
 |      change the x, y coordinates by dx, dy
 |  
 |  setx(self, xcoord)
 |      set x coordinate of point to xcoord
 |  
 |  sety(self, ycoord)
 |      set y coordinate of point to ycoord
 |  
 |  ------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 
 
>>> snoopy = Animal()
>>> snoopy.setpecies('dog') 
>>> snoopy.setLanguage('bark')
>>> snoopy.speak()
I am a dog and I bark.


class Animal:
    'represents an animal'

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a {} and I {}.'.format(self.spec, self.lang))

class Point:
    'class that represents a point in the plane’

    def __init__(self, xcoord, ycoord):
        'initialize coordinates to (xcoord, ycoord)'
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'return coordinates of the point as a tuple'
        return (self.x, self.y)

    def move(self, dx, dy):
        'change the x,y coordinates by dx,dy'
        self.x += dx
        self.y += dy
        
class Point:
    'class that represents a point in the plane’

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'return coordinates of the point as a tuple'
        return (self.x, self.y)

    def move(self, dx, dy):
        'change the x,y coordinates by dx,dy'
        self.x += dx
        self.y += dy


class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds'):
        self.species = species
        self.language = language

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a {} and I {}.'.format(self.spec, self.lang))

>>> snoopy = Animal('dog', 'bark')
>>> snoopy.speak()
I am a dog and I bark. 
>>> tweety = Animal('canary')
>>> tweety.speak() 
I am a canary and I make sounds. 
>>> animal = Animal() 
>>> animal.speak() 
I am a animal and I make sounds.


class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit 
        
>>> a = [1,2,3,4,5]
>>> a.pop()
5
>>> a
[1, 2, 3, 4]
>>> a.pop(0)
1
>>> a
[2, 3, 4]
>>> import random
>>> random.shuffle(a)
>>> a
[4, 3, 2]

>>> deck = Deck()
>>> deck.shuffle()
>>> card = deck.dealCard()
>>> card.getRank(), card.getSuit()
('2', '♠')
>>> card = deck.dealCard()
>>> card.getRank(), card.getSuit()
('Q', '♣')
>>> card = deck.dealCard()
>>> card.getRank(), card.getSuit()
('4', '♢')

class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = [] # deck is initially empty

        for suit in Deck.suits: # suits and ranks are in Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))


    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        shuffle(self.deck)
        
        
        
class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = [] # deck is initially empty

        #for each suit in deck:
            #for each card in deck:
                #append


    def dealCard(self):
        
        # return something

    def shuffle(self):
        'shuffle the deck'
        #shuffle from random module

class Queue:
    'a classic queue class'

    def __init__(self):
        'instantiates an empty list'
        self.q = []

    def isEmpty(self):
        'returns True if empty, False otherwise'
        return (len(self.q) == 0)

    def enqueue (self, item):
        'insert item at rear of queue'
        return self.q.append(item)

    def dequeue(self):
        'remove and return item at front of queue'
        return self.q.pop(0)

        
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
        
class Point:

    # other Point methods here

    def __repr__(self):
        '''canon-string representation Point(x, y)'''
        return 'Point({}, {})'.format(self.x, self.y)

class Point:
    # other Point methods here

    def __add__(self, point):
        return Point(self.x+point.x, self.y+point.y)

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

        
class Queue:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return (len(self.q) == 0)
    
    # other Queue methods here

    def __len__(self):
        return len(self.q)
        
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
        # to be implemented
        
        
class Point:
    'class that represents a point in the plane'

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'return coordinates of the point as a tuple'
        return (self.x, self.y)

    def move(self, dx, dy):
        'change the x, y coordinates by dx, dy'
        self.x += dx
        self.y += dy

class Point:
    'class that represents a point in the plane'

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'return coordinates of the point as a tuple'
        return (self.x, self.y)

    def move(self, dx, dy):
        'change the x,y coordinates by dx,dy'
        self.x += dx
        self.y += dy

    def getx(self):
        'return x coordinate of the point'
        return self.x

        
class Point:

    def setx(self, xcoord):
        self.x = xcoord

    def sety(self, ycoord):
        self.y = ycoord

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
class ClassName:
    classVariableName1 = value1
    classVariableName2 = value2
    ...
    def methodName(self, arg11, arg12, ...):
        statements

    def methodName(self, arg21, arg22, ...):
        statements
    ...

>>> help(Point)
Help on class Point in module __main__:

class Point(builtins.object)
 |  Methods defined here:
 |  
 |  get(self)
 |  
 |  move(self, dx, dy)
 |  
 |  setx(self, xcoord)
 |  
 |  sety(self, ycoord)
 |  
 |  -----------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>> help(Point)
Help on class Point in module __main__:

class Point(builtins.object)
 |  class that represents a point in the plane
 |  
 |  Methods defined here:
 |  
 |  get(self)
 |      return coordinates of the point as a tuple
 |  
 |  move(self, dx, dy)
 |      change the x, y coordinates by dx, dy
 |  
 |  setx(self, xcoord)
 |      set x coordinate of point to xcoord
 |  
 |  sety(self, ycoord)
 |      set y coordinate of point to ycoord
 |  
 |  ------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 
 
>>> snoopy = Animal()
>>> snoopy.setpecies('dog') 
>>> snoopy.setLanguage('bark')
>>> snoopy.speak()
I am a dog and I bark.


class Animal:
    'represents an animal'

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a {} and I {}.'.format(self.spec, self.lang))

class Point:
    'class that represents a point in the planeâ€™

    def __init__(self, xcoord, ycoord):
        'initialize coordinates to (xcoord, ycoord)'
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'return coordinates of the point as a tuple'
        return (self.x, self.y)

    def move(self, dx, dy):
        'change the x,y coordinates by dx,dy'
        self.x += dx
        self.y += dy
        
class Point:
    'class that represents a point in the planeâ€™

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'return coordinates of the point as a tuple'
        return (self.x, self.y)

    def move(self, dx, dy):
        'change the x,y coordinates by dx,dy'
        self.x += dx
        self.y += dy


class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds'):
        self.species = species
        self.language = language

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a {} and I {}.'.format(self.spec, self.lang))

>>> snoopy = Animal('dog', 'bark')
>>> snoopy.speak()
I am a dog and I bark. 
>>> tweety = Animal('canary')
>>> tweety.speak() 
I am a canary and I make sounds. 
>>> animal = Animal() 
>>> animal.speak() 
I am a animal and I make sounds.


class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit 
        
>>> a = [1,2,3,4,5]
>>> a.pop()
5
>>> a
[1, 2, 3, 4]
>>> a.pop(0)
1
>>> a
[2, 3, 4]
>>> import random
>>> random.shuffle(a)
>>> a
[4, 3, 2]

>>> deck = Deck()
>>> deck.shuffle()
>>> card = deck.dealCard()
>>> card.getRank(), card.getSuit()
('2', 'â™ ')
>>> card = deck.dealCard()
>>> card.getRank(), card.getSuit()
('Q', 'â™£')
>>> card = deck.dealCard()
>>> card.getRank(), card.getSuit()
('4', 'â™¢')

class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = [] # deck is initially empty

        for suit in Deck.suits: # suits and ranks are in Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))


    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        shuffle(self.deck)
        
        
        
class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = [] # deck is initially empty

        #for each suit in deck:
            #for each card in deck:
                #append


    def dealCard(self):
        
        # return something

    def shuffle(self):
        'shuffle the deck'
        #shuffle from random module

class Queue:
    'a classic queue class'

    def __init__(self):
        'instantiates an empty list'
        self.q = []

    def isEmpty(self):
        'returns True if empty, False otherwise'
        return (len(self.q) == 0)

    def enqueue (self, item):
        'insert item at rear of queue'
        return self.q.append(item)

    def dequeue(self):
        'remove and return item at front of queue'
        return self.q.pop(0)

        
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
        
class Point:

    # other Point methods here

    def __repr__(self):
        '''canon-string representation Point(x, y)'''
        return 'Point({}, {})'.format(self.x, self.y)

class Point:
    # other Point methods here

    def __add__(self, point):
        return Point(self.x+point.x, self.y+point.y)

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

        
class Queue:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return (len(self.q) == 0)
    
    # other Queue methods here

    def __len__(self):
        return len(self.q)
        

class Queue:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return (len(self.q) == 0)

    def enqueue (self, item):
        return self.q.append(item)

    def dequeue(self):
        return self.q.pop(0)

class Deck:
    ranks = {'2','3','4','5','6','7','8',
                     '9','10','J','Q','K','A'}
    suits = {'\u2660', '\u2661', 
                    '\u2662', '\u2663'}
    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          
        for suit in Deck.suits: 
            for rank in Deck.ranks:
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)

class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit 
        
    def __repr__(self):
        'return formal representation'
        return "Card('{}', '{}')"
            .format(self.rank, self.suit)


class Representation(object):
    def __repr__(self):
        return 'canonical string representation.'
    def __str__(self):
        return 'Pretty string representation.'

>>> r = Representation()
>>> r
canonical string representation
>>> print(r)
Pretty string representation.
>>> 

class Point:
    # other Point methods here
    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return shell representation Point(x, y)'
        return 'Point({}, {})'.format(self.x, self.y)
        
class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    # other Card methods here

    def __repr__(self):
        'return formal representation'
        return "Card('{}', '{}')".format(self.rank, self.suit)

class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit

    def __repr__(self):
        'return formal representation'
        return "Card('{}', '{}')".format(self.rank, self.suit)

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit
        
import random 
class MyList:
    def __init__(self, initial = []): 
        self.lst = initial

    def __len__(self):
        return len(self.lst)

    def append(self, item): 
        self.lst.append(self, item)

    # implementations of remaining "list" methods

    def choice(self):
        return random.choice(self.lst)
        
import random
class MyList(list):
    'a subclass of list that implements method choice'

    def choice(self):
        'return item from list chosen uniformly at random'
        return random.choice(self)

class ClassName:

class ClassName (SuperClass):

class ClassName (object):

class ClassName (SuperClass1, SuperClass2, ...):

class Animal:
    'represents an animal’

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a {} and I {}.'.format(self.spec, self.lang))

class Bird(Animal):
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print('{}! '.format(self.lang) * 3)
        
class Super:
    'a generic class with one method'
    def method(self):# the Super method
        print('in Super.method')

class Inheritor(Super):
    'class that inherits method'
    pass

class Replacer(Super):
    'class that overrides method'
    def method(self):
        print('in Replacer.method')

class Extender(Super):
    'class that extends method'
    def method(self):
        print('starting Extender.method')
        Super.method(self)# calling Super method
        print('ending Extender.method')
        
class EmptyQueueError(Exception):
    pass

class EmptyQueueError(Exception):
    pass
    
class Queue:
    'a classic queue class'

    def __init__(self):
        'instantiates an empty list'
        self.q = []

    def isEmpty(self):
        'returns True if queue is empty, False otherwise'
        return (len(self.q) == 0)

    def enqueue (self, item):
        'insert item at rear of queue'
        return self.q.append(item)

    def dequeue(self):
        'remove and return item at front of queue'
        if self.isEmpty():
            raise EmptyQueueError('dequeue from empty queue')
        return self.q.pop(0)
        




