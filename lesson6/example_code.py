# debugging
def h():
    print('inside h')
    
def k():
    print('Inside k')
    h()
    
def main():
    k()
    
main()

def hello():
    '''a greeting service
    repeatedly requests user's name
    and greets'''
    while True:
        name = input(
		'What is your name? ')
        print('Hello '+ name)



def cities():
    lst = []
    
    city = input('Enter city: ')

    while city != '':
        lst.append(city)
        city = input('Enter city: ')

    return lst

    
def cities2():
    lst = []
    while True:
        city = input(
		'Enter city: ')

        if city == '':
            return lst

        lst.append(city)

def cities3():
    lst = []
    while True:
        city = input(
		'Enter city: ')

        if city == '':
            break

        lst.append(city)

     return lst

     
def ignore(table):
    for row in table:
        for num in row:
            if num == 0:
                continue
            print(num, end=' ')
        print() 

table = [
  [2, 3, 0, 6],
  [0, 3, 4, 5],
  [4, 5, 6, 0]
]


def before(table):
    for row in table:
        for num in row:
            if num == 0:
                break
            print(num,end=' ')
        print() 
        

employee = {
	'864-20': ['Arm', 'Spartyan'],
	'987-65': ['Vlad', 'Tundyan'],
	'100-01': ['Kiazh', 'Damyan']}

days = {'Mo': 1, 'Tu': 2, 'Th': 4, 'W': 3}

emp = {[1,2]:1,[2,3]:3} # error

days = {'Mo':1, 'Tu':2, 'W':3}

days2 = {'Tu':2, 'Fr':5}

def complete(abbreviation):
    '''returns day of the week 
    corresponding to abbreviation
    '''
    days = {'Mo': 'Monday', 
	    'Tu':'Tuesday', 
	    'We': 'Wednesday',
	    'Th': 'Thursday', 
	    'Fr': 'Friday', 
	    'Sa': 'Saturday',
	    'Su':'Sunday'}
    return days[abbreviation]


def frequency(itemList):
    'returns frequency of items in itemList'

    counters = {}
    for item in itemList:
        if item in counters: # increment item counter
            counters[item] += 1
        else: # create item counter
            counters[item] = 1
    return counters

grades = [95, 96, 100, 85, 95, 90, 95, 100, 100]
#frequency(grades)

text = 'Be the change that you wish to see in the world'

def wordCount(text):
    'prints frequency of each word in text' 
    # split text
    # define empty dictionary
    for word in wordList:   
        #if exists
            # +1
        # doesn't exist
            # =1

         # print word counts with format

phonebook = {
	('Arm', 'Spartyan'):'56-78-90',
	('Vlad', 'Tundyan'):'34-56-78',
	('Kiazh', 'Damyan'):'48-76-54'
}

phonebook = {
	'Arm':'56-78-90',
	'Vlad':'34-56-78',
	'Kiazh':'48-76-54'
}
   
def lookup(phonebook):
    while True:
        first = input('first name: ')
        last = input('last name: ')

        # construct the key

        # if key is in dictionary
            # print value
        # if key not in dictionary
            # print unknown

	
#exercise 2, lesson 6
text = 'Be the change that you wish to see in the world'

def wordCount(text):
    pass


def lookup(adict):
    pass
    
# sorting list of tuples
t = [('a', 10), ('c', 22), ('b', 1)]

# sorting dict by key
d = {'a':10, 'b':1, 'c':22}

#exercise 4, lesson 6
def topten(filename):
    pass
    
filename = 'romeo.txt'
topten(filename)


>>> t
[('a', 10), ('c', 22), ('b', 1)]
>>> t.sort()
>>> t
[('a', 10), ('b', 1), ('c', 22)]
>>> sorted(t)
[('a', 10), ('b', 1), ('c', 22)]


>>> d = {'a':10, 'b':1, 'c':22}
>>> d.items()
dict_items([('a', 10), ('c', 22), ('b', 1)])
>>> type(d.items())
<class 'dict_items'>
>>> t = sorted(d.items())
>>> t
[('a', 10), ('b', 1), ('c', 22)]
>>> type(t)
<class 'list'>
>>> for k,v in sorted(d.items()):
	print(k,v)

	
a 10
b 1
c 22
>>> 

>>> d = {'a':10, 'b':1, 'c':22}
>>> lst = list()
>>> for k,v in d.items():
        lst.append((v,k))
	
>>> lst
[(10, 'a'), (22, 'c'), (1, 'b')]
>>> lst.sort(reverse=True)
>>> lst
[(22, 'c'), (10, 'a'), (1, 'b')]
>>>
