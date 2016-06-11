names = ['Ann', 'Bob', 'Cal', 'Dee', 'Eve', 'Flo', 'Hal', 'Ike']

for i in range(start, end + 1):
    print(format(i, 'X'), end=' ')  #hex
    print(i, end=' ')               #dec
    print(chr(int(i)))              #letter

>>>    
531 1329 Ա
532 1330 Բ
533 1331 Գ
534 1332 Դ
535 1333 Ե
536 1334 Զ
537 1335 Է

>>> content
b'This is a text document\nposted on the\nWWW.\n'
>>> type(content)
<class 'bytes'>
>>> s = content.decode('utf-8')
>>> type(s)
<class 'str'>
>>> s
'This is a text document\nposted on the\nWWW.\n'
>>> s = content.decode()
>>> s
'This is a text document\nposted on the\nWWW.\n'
>>> 


>>> vec = [2, 4, 6]
>>> [3*x for x in vec]
    [6, 12, 18]

>>> [3*x for x in vec if x > 3]
    [12, 18]

>>> [3*x for x in vec if x < 2]
    []

>>> [[x,x**2] for x in vec]
    [[2, 4], [4, 16], [6, 36]]

>>> [x, x**2 for x in vec] 
    # error - parens required for tuples

[expression for element in list]

[expression for element in list if condition]

for element in list:
    if conditon:
        expression

        
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> squares = [x**2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

>>> lst = []
>>> for x in [1,2,3]:
        for y in [3,1,4]:
            if x!=y:
                lst.append((x,y))
                
>>> lst
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
>>> lst = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
>>> lst
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]

[ expression for name in list if filter ]

>>> li = [3, 6, 2, 7, 1, 9]
>>> [x * 2 for x in li if x > 4]
[12, 14, 18]

>>> # call a method on each element
>>> fruits = ['  banana', '  raspberry ', ' grapefruit  ']
>>> [fruit.strip() for fruit in fruits]
['banana', 'raspberry', 'grapefruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']

>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> lst = [3, 2, 4, 1]
>>> [elem*2 for elem in [item+1 for item in lst] ]
[8, 6, 10, 4]
[4, 3, 5, 2]

>>> matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
>>> [[row[i] for row in matrix] for i in range(len(matrix))]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

import sys

if len(sys.argv) < 2:
    sys.exit('Usage: {} filename'.format(sys.argv[0]))
    
infile = open(sys.argv[1])
s = infile.read()
print(s)


import sys

if len(sys.argv) < 4:
    sys.exit('Usage: {} arg1 arg2 arg3'.format(sys.argv[0]))


script, first, second, third = sys.argv

print("script name:", (script))
print("first variable:", (first))
print("second variable:", (second))
print("third variable:", (third))
