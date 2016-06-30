from tkinter.filedialog import askopenfilename

filename = askopenfilename()
infile = open( filename, 'r')
data = infile.read()
infile.close()


# syntax error
excuse = 'I'm sick'
print("hello world)
a = 3 + 5 7
#exceptions
infile = open('sample.txt')

>>> excuse='I'm sick'
SyntaxError: invalid syntax
>>> print("Hello world)
      
SyntaxError: EOL while scanning string literal
>>> a = 3 + 5 7
SyntaxError: invalid syntax
>>> open('sample.txt')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    open('sample.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'sample.txt'
>>> 

def temperature(t):
    if t > 32:
        print('It is hot')
    elif t > 86:
        print('It is cool')
    else: # t <= 32
        print('It is freezing')
    print('Goodbye')

def temperature(t):
    if 86 >= t > 32:
        print('It is hot')
    elif t > 86:
        print('It is cool')
    else: # t <= 32
        print('It is freezing')
    print('Goodbye')

def temperature(t):
    if t > 86:
        print('It is hot')
    elif t > 32: # 86 >= t > 32
        print('It is cool')
    else: # t <= 32
        print('It is freezing')
    print('Goodbye')
	
>>> BMI(190, 75)
Normal
>>> BMI(140, 75)
Underweight
>>> BMI(240, 75)
Overweight

def BMI(weight, height):
  'prints BMI report’

  pass

>>> raise Exception("I know python!")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    raise Exception("I know python!")
Exception: I know python!
>>> raise KeyboardInterrupt("Cntr-C")
Traceback (most recent call last):...
KeyboardInterrupt: Cntr-C

for <variable> in <sequence>:
    <indented code block>
<non-indented code block>


>>> name = 'Apple'
>>> for char in name:
	print(char)
	
A
p
p
l
e
>>> for word in ['stop', 'desktop', 'post', 'top']:
    if 'top' in word:
        print(word)

stop
desktop
top
>>> 

>>> infile = open('test.txt') 
>>> content = infile.read() 
>>> for char in content:
        print(char, end='')
		
>>> infile = open('test.txt') 
>>> lines = infile.readlines() 
>>> for line in lines:
        print(line, end='')


>>> for i in range(10):
        print(i, end=' ')


0 1 2 3 4 5 6 7 8 9

>>> for i in range(7, 100, 17):
        print(i, end=' ')


7 24 41 58 75 92

>>> for i in range(len('world')):
	print(i, end=' ')

	
0 1 2 3 4

>>> pets = ['cat', 'dog', 'fish', 'bird']

>>> for animal in pets:
        print(animal, end=' ')

cat dog fish bird

>>> for i in range(len(pets)):
        print(pets[i], end=' ')

cat dog fish bird


>>> checkSorted([2, 4, 6, 8, 10])
True
>>> checkSorted([2, 4, 6, 3, 10])
False

def checkSorted(lst):
	'return True if lst is increasing False otherwise'
    #for i in ...:
        # i = 0, 1, 2, ..., len(lst)-2
        #if ith elem > i+1th elem:
            return False
    #return True

tf = checkSorted([2, 4, 6, 8, 10])==True
print(tf)
tf = checkSorted([2, 4, 6, 3, 10])==False
print(tf)

>>> arithmetic([3, 6, 9, 12, 15]) 
True
>>> arithmetic([3, 6, 9, 11, 14]) 
False
>>> arithmetic([3])
True


def arithmetic(lst):
    '''
    return True if list lst is arithmetic sequence,
    False otherwise
    >>> arithmetic([3, 6, 9, 11, 14])
    False
    >>> arithmetic([3, 6, 9, 12, 15])
    True
    >>> arithmetic([3])
    True
    '''

    if len(lst) < 2:
        return True

    diff = lst[1] - lst[0]
    pass
	
import doctest
doctest.testmod()


>>> factorial(0)
1 
>>> factorial(1)
1
>>> factorial(3)
6
>>> factorial(6)
720

def factorial(n):
    '''returns n! for input integer n
	>>> factorial(6)
	720
	'''
    res = 1
    #for i in ...:
        #multiply
    #return res

import doctest
doctest.testmod()	

>>> acronym('Random access memory')
'RAM' 
>>> acronym("GNU's not UNIX")
'GNU'

def acronym(phrase):
    '''return the acronym of the input string phrase
	>>> acronym("GNU's not UNIX")
	'GNU'
	'''

    # split phrase into a list of words

    # accumulate first character, as an uppercase, of every word
    res = ''
    pass

import doctest
doctest.testmod

>>> divisors(1)
[1]
>>> divisors(6)
[1, 2, 3, 6]
>>> divisors(11)
[1, 11]

def divisors(n):
    'return the list of divisors of n'

    res = []    # accumulator

    #for i in range ... :
        # if i is a divisor of n
            # accumulate i

    return res
	
	
print(divisors[6])
	
def bubblesort(lst):

    #for i in range ... :

        #for j in range ... :

            #if lst[j] > lst[j+1]:
                #swap it
                
>>> lst = [3, 1, 7, 4, 9, 2, 5]
>>> bubblesort(lst)
>>> lst
[1, 2, 3, 4, 5, 7, 9]

lst = [4,13,1,7]

for var in sequence:
   for var in sequence:
      statements(s)
   statements(s)
