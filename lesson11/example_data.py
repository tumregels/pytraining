>>> def foo(data=[]):
	data.append(1)
	return data

>>> foo()
[1]
>>> foo()
[1, 1]
>>> foo()
[1, 1, 1]
>>> 

>>> i = 10
>>> def foo(data=i):
        print(data)

	
>>> i = 8
>>> foo()
10
>>> 

def custom_add(i):
    def add(x):
        return x + i
    return add
    
>>> add_five = custom_add(5)
>>> add_five(1)
6
>>> add_ten = custom_add(10)
>>> add_ten(1)
11

def custom_add(i):
    def add(x):
        return x + i
    return add

>>> add_7 = custom_add(7)
>>> add_7(1)
8
>>> add_10 = custom_add(10)
>>> add_10(1)
11
>>> 
>>> i = 10
>>> add_10 = custom_add(i)
>>> add_10(5)
15
>>> i = 20
>>> add_10(5)
15
>>> 

>>> def compose(f, g, x):
        return f(g(x))

>>> compose(str, sum, [1,2,3])
'6'

def maker(N):
    def action(X): # Make and return action
        return X ** N # retains N
    return action
        
>>> f = maker(2)
>>> f
<function maker.<locals>.action at 0x02081300>
>>> f(4)
16
>>> maker(3)(3)
27
>>> 
        
        
>>> map(float,['7','8'])
<map object at 0x020ACBF0>
>>> list(map(float,['7','8']))
[7.0, 8.0]
>>> [float(i) for i in ['7','8']]
[7.0, 8.0]
>>>

list(map(f, sequence)) equivalent to [f(x) for x in sequence]

is directly equivalent (*) to:

map(aFunction, aSequence)

[x**2 for x in range(10)]

>>> def square(x): return x ** 2

>>> list(map(square,range(10)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def mymap(aFunc, aSeq):
    result = []
    for x in aSeq:
        result.append(aFunc(x))
    return result
    
>>> mymap(square,range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> import operator
>>> mymap(operator.neg,range(10))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

>>> list(map(pow,[2,3,4],[10,11,12]))
[1024, 177147, 16777216]
>>> pow(2,10)
1024
>>> pow(3,11)
177147

def mymap(aFunc, aSeq):
    result = []
    for x in aSeq:
        result.append(aFunc(x))
    return result

def square(x): return x ** 2

equivalent to

square = lambda x: x**2

syntax lambda a1,a2,... : expr(a1,a2,...)

#mymap(square, [1, 2, 3])
#[1, 4, 9]

>>> f = lambda x: x*2
>>> f(1)
2
>>> map(lambda x: x**2, [1, 2, 3])
[1, 4, 9]
>>> filter(lambda x: x==0, [0, 1, 0, 2])
[0, 0]

>>> f = l

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)

t = [40, 50, 60, 70]
F = list(map(fahrenheit, t))
C = list(map(celsius, F))

t = [40, 50, 60, 70]
F = list(map(lambda x: (float(9)/5)*x + 32, t))
C = list(map(lambda x: (float(5)/9)*(x-32), F))

print(F)#[104.0, 122.0, 140.0, 158.0]
print(C)#[40.0, 50.0, 60.0, 70.0]

>>> list(range(-7,7,2))
[-7, -5, -3, -1, 1, 3, 5]
>>> list( filter((lambda x: x < 0), range(-7,7,2)))
[-7, -5, -3, -1]

>>> res = []
>>> for x in range(-7,7,2):
        if x < 0:
            res.append(x)

>>> res
[-7, -5, -3, -1]

filtered_list = list(filter(lambda x : x%2==0,range(100)))

>>> sorted(['A','b','C'])
['A', 'C', 'b']
>>> sorted(['A','b','C'],key=str.lower)
['A', 'b', 'C']

>>> l = ['Silvio Berlusconi','Angela Merkel']
>>> sorted(l)
['Angela Merkel', 'Silvio Berlusconi']
>>> last_name = lambda name: name.split()[1]
>>> sorted(l, key=last_name)
['Silvio Berlusconi', 'Angela Merkel']
>>> sorted(l,key=lambda x: x.split()[1])
['Silvio Berlusconi', 'Angela Merkel']

>>> d = {1: 2, 3: 4, 4:3, 2:1, 0:0}
>>> sorted(d.items(), key=lambda x: x[1])
[(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]

>>> from collections import OrderedDict
>>> od = OrderedDict(sorted(d.items(),key=lambda x: x[1]))
>>> od
OrderedDict([(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)])

>>> lst = ['aaaa','bbb','cc','d']
>>> sorted(lst,...)
['d', 'cc', 'bbb', 'aaaa']
>>> sorted(lst,key=lambda x:len(x))
['d', 'cc', 'bbb', 'aaaa']

>>> from functools import reduce
>>> reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
24
>>> reduce( (lambda x, y: x / y), [1, 2, 3, 4] )
0.041666666666666664

>>> reduce((lambda x,y: x+y), range(5))
10
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> reduce((lambda x,y: x*y), range(5))
0
>>> reduce((lambda x,y: x*y), range(1,5))
24


>>> lst = "Patience is the best prayer".split()
>>> ' '.join(lst)
'Patience is the best prayer'
>>> reduce((lamdba x,y:x+y),lst)
SyntaxError: invalid syntax
>>> reduce((lambda x,y:x+y),lst)
'Patienceisthebestprayer'
>>> reduce((lambda x,y:x+' '+y),lst)
'Patience is the best prayer'

>>> from functools import reduce
>>> reduce(lambda x,y: x+y, [47,11,42,13])
113


def myreduce(func, seq):
    acc = seq[0]
    for next in seq[1:]:
            acc = func(acc, next)
    return acc
    
>>> myreduce((lambda x,y:x+y),range(1,5))
10
>>> myreduce((lambda x,y:x*y),range(1,5))
24
>>> 

>>> list(map(lambda x: x**3, range(1,5)))
[1, 8, 27, 64]
>>> list(filter(lambda x: x%3==0, range(10)))
[0, 3, 6, 9]
>>> from functools import reduce
>>> reduce(lambda x,y:x+y,range(10))
45

	def add(x, y):
	    '''Returns the sum of the two
	            arguments.'''
	    return x + y
	
	def triple(x):
	    '''Takes a number x as an argument
	            and returns 3 * x.'''
	    return 3 * x
	
	def mapReduce(mapFunction, reduceFunction, myList):
	    '''Applies mapFunction to myList to
	            construct a new list and then
	            applies reduceFunction to the
	            new list and returns
	            reduceFunction's result.'''
	
	    newList = map(mapFunction, myList)
	    value = reduce(reduceFunction, newList)
	    return value
	
	print (mapReduce(triple, add, [14, 10, 12, 5]))
    
def add(x, y): return x + y

def twice(x): return  2 * x

from functools import reduce
	
def mapReduce(mapFunction, reduceFunction, seq):
    newSeq = map(mapFunction, seq)
    oneValue = reduce(reduceFunction, newSeq)
    return oneValue

print(mapReduce(twice,add,range(1,5)))

def mapReduce(mapFunction, reduceFunction, seq):
    return reduce(reduceFunction, map(mapFunction, seq))

>>> f = lambda a,b: a if (a > b) else b
>>> reduce(f, [47,11,42,102,13])
102
>>>

>>> import random
>>> randomList=random.sample(range(1, 101), 10)
>>> randomList
[57, 84, 3, 84, 34, 29, 88, 21, 25, 60]
>>> f = lambda a,b: a if (a > b) else b
>>> reduce(f, randomList)
88
>>> 

def derivative(f, h):
    '''Returns a function
    which is approximation of
    the derivative of f with respect to h'''

    return lambda x: (f(x+h) - f(x)) / h
    
def square(x): return x**2

>>> g = derivative(square, 0.001)
>>> g(5)
10.001000000002591

def my_reduce(f, l, init):
    if l == []:
        return init
    return f(my_reduce(f, l[:-1], init), l[-1])
    
    
def speak(topic):
    print "My speach is " + topic

def timer(fn):
    def inner(*args, **kwargs):
        t = time()
        fn(*args, **kwargs)
        print "took {time}".format(time=time()-t)

    return inner

speaker = timer(speak)
speaker("FP with Python")


from time import time

def speak(topic="this"):
    print("My speech is " + topic)

def trace(f):
    def new_f(*args,**kwargs):
        print('Entering {}{}'.format(f.__name__,args))
        result = f(*args, **kwargs)
        print('Exiting {}{} with {}'.format(f.__name__,args, result))
        return result
    return new_f

def sum(n, m):
    return n + m

sum = trace(sum)
print(sum(5,6))

>>> [x for x in range(-7,7,2) if x < 0]
[-7, -5, -3, -1]

>>> speaker("FP with Python")
My speech is FP with Python
took 0.0