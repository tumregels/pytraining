def double(y):
    x=2
    print('x = {}, y = {}'.format(x,y))
    return x*y

def h(n):
    print('Start h')
    print(1/n)
    print(n)

def g(n):
    print('Start g')
    h(n-1)
    print(n)

def f(n):
    print('Start f')
    g(n-1)
    print(n)

def f(b):       # f has global scope, b has local scope
    a = 6       # a has scope local to function call f()
    return a*b  # this a is the local a

a = 0           # this a has global scope
print('f(3) = {}'.format(f(3)))
print('a is {}'.format(a))        # global a is still 0

def f(b):# f : global scope, b : local scope
	a = 6 # a : local scope
	return a*b

>>> a = 0 # global scope
>>> f(3)
18
>>> a
0

>>> ============== RESTART ==============
>>> def f(b):#f : global scope, b : local scope
	return a*b

>>> a = 0 # global scope
>>> f(3)
0
>>> a
0
>>> 

>>> def f(b):
	global a
	a = 6
	return a*b

>>> a = 0
>>> f(3)
18
>>> a
6

def h(n):
   print('Start h')
   print(1/n)
   print(n)

def g(n):
   print('Start g')
   h(n-1)
   print(n)

def f(n):
   print('Start f')
   g(n-1)
   print(n)



strAge = input('Enter your age: ')
intAge = int(strAge)
print('You are {} years old.'.format(intAge))

try:
    strAge = input('Enter your age: ')
    intAge = int(strAge)
    print('You are {} years old.'.format(intAge))
except:
    print('Enter your age using digits 0-9!')


def readAge(filename):
    'converts first line of file filename to an integer and prints it'
    try:
        infile = open(filename)
        strAge = infile.readline()
        age = int(strAge)
        print('age is', age)
    except ValueError:
        print('Value cannot be converted to integer.')
        
        
def readAge(filename):
    'converts first line of file filename to an integer and prints it'
    try:
        infile = open(filename)
        strAge = infile.readline()
        age = int(strAge)
        print('age is',age)
    except IOError:
        # executed only if an IOError exception is raised
        print('Input/Output error.')
    except ValueError:
        # executed only if a ValueError exception is raised
        print('Value cannot be converted to integer.')
    except:
        # executed if an exception other than IOError or ValueError is raised
        print('Other error.')

def divider():
    while True:
        nums = input('Enter 2 digits (format: x y):')
        (x,y) = nums.split()
        try:
            x = int(x)
            y = int(y)
            res = x/y
            print(res)
        except ZeroDivisionError:
            print('ZeroDivisionError')
            print('try again without 0')
        except ValueError:
            print('ValueError')
            print('try again without letters')
        except:
            print("Something went wrong!")
            raise

divider()

Enter 2 digits (format: x y):5 3
1.6666666666666667
Enter 2 digits (format: x y):5 0
ZeroDivisionError
try again without 0
Enter 2 digits (format: x y):a b
ValueError
try again without letters
Enter 2 digits (format: x y):4 b
ValueError
try again without letters
Enter 2 digits (format: x y):




try:
try_suite
finally:
finally_suite

try:
    <indented code block>
except <ExceptionType>:
    <exception handler block>
finally:
    <always do code block>
<non-indented statement>

def read_data(filename):
    lines = []
    infile = None
    try:
        infile = open(filename, encoding="utf8")
        for line in infile:
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if infile is not None:
            infile.close()
    return lines

try:
    # process
except exception:
    # handle
finally:
    # cleanup
# continue


def salute(name, greeting='Hallo', punct='!'):
    return greeting + ' ' + name + punct


>>> def salute(name, greeting='Hallo', punct='!'):
	return greeting + ' ' + name + punct

>>> salute('Valod')
'Hallo Valod!'
>>> salute('Valod', greeting='Parev')
'Parev Valod!'  
>>> salute('Valod', greeting='Parev',punct=':)')
'Parev Valod:)'
>>> salute('Valod', punct='!')
'Hallo Valod!'
>>> salute('Valod', punct='**!**')
'Hallo Valod**!**'
>>> 
>>> salute(punct='**!**','Valod')
SyntaxError: non-keyword arg after keyword arg
>>> 

>>> def f(a, b):
        print(a, b)

        
>>> f('apple', 'apricot')
apple appricot
>>> l = ['apple', 'apricot']
>>> f(*l)
apple apricot
>>> f(l)
TypeError: f() missing 1 required positional argument: 'b'
>>> 

>>> def f(a='apple', b='apricot'):
        print(a, b)

        
>>> def f(a='apple', b='apricot'):
        print(a, b)

        
>>> f(b ='lemon', a='orange')
orange lemon
>>> d = {'a':'orange','b':'lemon'}
>>> f(d)
{'b': 'lemon', 'a': 'orange'} apricot
>>> f(**d)
orange lemon


def f(fruit1, fruit2, veg1='potato', veg2='tomato'):
    print (fruit1, fruit2, veg1, veg2)
>>> l = ['kiwi', 'mango']
>>> d = {'veg1': 'cucumber', veg2:'onion'}
>>> foo(*l, **d)
kiwi kumquat cauliflower


>>> def f(fruit1, fruit2, veg1='potato', veg2='tomato'):
    print (fruit1, fruit2, veg1, veg2)
    
>>> l = ['kiwi', 'mango']
>>> d = {'veg1': 'cucumber', 'veg2':'onion'}
>>> f(*l,**d)
kiwi mango cucumber onion
>>> f(*l)
kiwi mango potato tomato
>>> f(**d)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    f(**d)
TypeError: f() missing 2 required positional arguments: 'fruit1' and 'fruit2'
>>> 

def f(*args):
    print("args is ", args)
       
>>> def f(*args):
    print("args is ", args)
    
>>> f(1, 2, 3, 4)
args is  (1, 2, 3, 4)
>>> 
def f(*args):
    print("args is ", args)
    print("type of args is ",type(args))
  
>>> f(1, 2, 3, 4)
args is  (1, 2, 3, 4)
type of args is  <class 'tuple'>
>>> def f(*args):
	for arg in args:
		print(arg, end=' ')
		
>>> f(1, 2, 3, 4)
1 2 3 4 
>>> def f(*args):
	for arg in args:
		print(arg, end='-')
		
>>> f(1, 2, 3, 4)
1-2-3-4-
>>> 


def f(a, *args):
    print("a = ", a)
    print("args = ", args)
   
f(1, 2, 3, 4)

def f(a, *args, b):
    print("a = ", a)
    print("args = ", args)
    print("b = ", b)
   
f(1, 2, 3, 4)

>>> def f(a, *args):
    print("a = ", a)
    print("args = ", args)
    
>>> f(1,2,3,4)
a =  1
args =  (2, 3, 4)
>>> def f(a, *args, b):
    print("a = ", a)
    print("args = ", args)
    print("b = ", b)

>>> f(1, 2, 3, 4)
TypeError: f() missing 1 required keyword-only argument: 'b'
>>> def f(a, b, *args):
    print("a = ", a)
    print("args = ", args)
    print("b = ", b)

>>> f(1, 2, 3, 4)
a =  1
args =  (3, 4)
b =  2
>>> 

def f(**kwargs):
    # kwargs is a dict of all keyword arguments
    for (k,v) in kwargs.items():
        print('{}={}'.format(k,v))
        
        
>>> def f(**kwargs):
    # kwargs is a dict of all keyword arguments
    for (k,v) in kwargs.items():
        print('{}={}'.format(k,v))

        
>>> f(a=1,b=2,c=3)
b=2
a=1
c=3
>>> 

>>> def f(**kwargs):
    # kwargs is a dict of all keyword arguments
    for (k,v) in kwargs.items():
        print('{}={}'.format(k,v))
    print('type of kwargs is ', type(kwargs))

    
>>> f(a=1,b=2,c=3)
b=2
a=1
c=3
type of kwargs is  <class 'dict'>
>>> 

def functionName(fargs,*args,**kwargs):
    <indented code block>
    
    
def print_args(*args, **kwargs):
    for i, arg in enumerate(args):
        print("positional argument {0} = {1}".format(i, arg))
    for key in kwargs:
        print("keyword argument {0} = {1}".format(key, kwargs[key]))
        
>>> def print_args(*args, **kwargs):
    for i, arg in enumerate(args):
        print("positional argument {0} = {1}".format(i, arg))
    for key in kwargs:
        print("keyword argument {0} = {1}".format(key, kwargs[key]))

        
>>> print_args(0,1,2,d=3,e=4,f=5)
positional argument 0 = 0
positional argument 1 = 1
positional argument 2 = 2
keyword argument f = 5
keyword argument e = 4
keyword argument d = 3
>>>  

def sum(*values, **options):
    s = 0
    for i in values:
        s = s + i
    if "neg" in options:
        if options["neg"]:
            s = -s
    return s

>>> sum(1, 2, 3)
6
>>> sum(1, 2, 3, neg=True)
-6
>>> sum(1, 2, 3, neg=False)
6
        
def sum(*values, **options):
    s = 0
    for i in values:
        s = s + i
    if "neg" in options:
        if options["neg"]:
            s = -s
    return s

s = sum(1, 2, 3, 4, 5)            # returns 15
s = sum(1, 2, 3, 4, 5, neg=True)  # returns -15
s = sum(1, 2, 3, 4, 5, neg=False) # returns 15


def sum(*args, **kwargs):
    s = 0
    for i in args:
        s = s + i
    if "power" in kwargs:
        if kwargs["neg"]:
            s = -s
    return s

def sum(*values, **options):
    s = 0
    for i in values:
        s = s + i
    if "power" in options:
        if options["neg"]:
            s = -s
    return s

def sum(*args, neg=False):
    s = 0
    for i in args:
        s = s + i
    if neg
        s = -s
    return 
    
def sum_of_powers(*args, power=1):
    result = 0
    for arg in args:
        result += arg ** power
    return result
    
def sum_of_powers(*args, power=1):
    #accumulator
    #for each
        #do sum
    #return result
    
>>> sum_of_powers(1,2)
3
>>> sum_of_powers(1,2,power=2)
5
>>> sum_of_powers(1,2,power=3)
9

>>> s = 'to be or not to be'
>>> words = s.split(' ')
>>> words
['to', 'be', 'or', 'not', 'to', 'be']
>>> " ".join(words)
'to be or not to be'
>>> "_!_".join(words)
'to_!_be_!_or_!_not_!_to_!_be'
>>> lst = [1,2,3,4]
>>> "-".join([str(x) for x in lst])
'1-2-3-4'
>>> s = ' hallo !!'
>>> s.strip(' !')
'hallo'
>>> s.lstrip(' ')
'hallo !!'
>>> s = 'abc'
>>> s.isalpha()
True
>>> s.isdigit()
False

>>> u = [1,2,3]
>>> v = ('a', 'b', 'c')
>>> w = [4,5,6]
>>> zip(u,v)
<zip object at 0x0232CE90>
>>> list(zip(u,v))
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> list(zip(a,b,c))
[(1, 'a', 4), (2, 'b', 5), (3, 'c', 6)]
>>> v = ('a', 'b', 'c')
>>> (a,b,c) = v
>>> a
'a'
>>> b
'b'
>>> c
'c'
>>> a = [1,2,3]
>>> b = ['a','b','c']
>>> e = dict(zip(a,b))
>>> e
{1: 'a', 2: 'b', 3: 'c'}
>>> 


>>> u = [1,2,3]
>>> v = ('a', 'b', 'c')
>>> w = [4,5,6]
>>> (a,b,c) = v
>>> a
'a'
>>> b
'b'
>>> c
'c'
>>> zip(u,v)
<zip object at 0x0232CF58>
>>> list(zip(u,v))
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> list(zip(u,v,w))
[(1, 'a', 4), (2, 'b', 5), (3, 'c', 6)]
>>> e = dict(zip(u,v))
>>> e
{1: 'a', 2: 'b', 3: 'c'}
>>> 

>>> def f(a, b=7, c=“Hi”):
        return a + b
>>> f(5,3,”hello”)
>>> f(5,3)
>>> f(5)

>>> def f(a, b=7, c="Hi"):
        return a + b

>>> f(5,6)
11
>>> f(5,5,"dummy")
10
>>> f(5)
12

>>> def f(fruit1, fruit2, veg1='potato', veg2='tomato'):
	print (fruit1, fruit2, veg1, veg2)

>>> l = ['kiwi', 'mango']
>>> d = {'veg1': 'cucumber', 'veg2':'onion'}
>>> f(fruit2='orange', fruit1='banana',**d)
banana orange cucumber onion
>>> d = {'fruit1':'banana','fruit2':'orange','veg1': 'cucumber', 'veg2':'onion'}
>>> f(**d)
banana orange cucumber onion
>>> 
