# debugging
def h():
    print('inside h')
    
def k():
    print('Inside k')
    h()
    
def main():
    k()
    
main()


def acronym(phrase):
    '''return the acronym of the 
	input string phrase'''
    # split phrase
    
    # accumulate first character
    
	# .upper()
    #return res

#print(acronym('Random access memory'))
#'RAM' 
#print(acronym("GNU's not UNIX"))
#'GNU'


def divisors(n):
    'return the list of divisors of n'

    # accumulator

    #for i in range ...
        # if i is a divisor of n
            # accumulate i

    #return res

#print(divisors(1))
#[1]
#print(divisors(6))
#[1, 2, 3, 6]
#print(divisors(11))
#[1, 11]


def nested2(n):
    for j in range(n):
        for i in range(j+1):
            print(i, end=' ’)
        print()
		
def bubblesort(lst):

    #for i in range ...:

        #for j in range(i):

            #if lst[j] > lst[j+1]:
                #flip

#alst = [3, 1, 7, 4, 9, 2, 5]
#bubblesort(alst)
#print(alst)
#[1, 2, 3, 4, 5, 7, 9]

 table = [[3, 5, 7, 9],
             [0, 2, 1, 6],
             [3, 8, 3, 1]]

def incr2D(t):
    'increments each number in 2D list t'

    # for every row index i
        # for every column index j
            t[i][j] += 1

#incr2D(table) 
#print(table)

def negative (lst):

    # using counter loop pattern
        # if 
            # return index
            
    # return -1

#alst = [3, 1, -7, -4, 9, -2]
#print(negative(lst))
#2
#print(negative([1, 2, 3]))
#-1
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
	('Kiazh', 'Damyan'):'48-76-54'}
   
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

#exercise 3, lesson 6
phonebook = {
	('Arm', 'Spartyan'):'56-78-90',
	('Vlad', 'Tundyan'):'34-56-78',
	('Kiazh', 'Damyan'):'48-76-54'}

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
