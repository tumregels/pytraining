def welcome(name):
    return "Welcome "+name

greet_me = welcome

>>> greet_me("Arsen")
'Welcome Arsen'
>>> 

def welcome(name):
    def get_message():
        return "Welcome "

    result = get_message()+name
    return result

>>> welcome("Arsen")
'Welcome Arsen'
>>> 


def welcome(name):
    return "Welcome " + name

def call(func):
    fixed_name = "Sparta"
    return func(fixed_name)  

>>> call(welcome)
'Welcome Sparta'
>>> 

def create_greet_func():
    def get_message():
        return "Good Morning!"

    return get_message


>>> greet = create_greet_func()
>>> greet()
'Good Morning!'
>>> create_greet_func()()
'Good Morning!'
>>>

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeitalic    
def hello():
    return "hello world"
    
hello = makeitalic(hello)
print(hello())

>>> hello()
'<i>hello world</i>'
>>> 

@makebold    
def hello():
    return "hello world"
    
>>> hello()
'<b>hello world</b>'
>>> 

   
def hello():
    return "hello world"
hello = makebold(hello)
    
>>> hello()
'<b>hello world</b>'
>>> 


def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
    
@makebold    
def hello():
    return "hello world"
    
print(hello())

>>> hello()
'<b><i>hello world</i></b>'


def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


def hello():
    return "hello world"
hello = makebold(makeitalic(hello))
    
print(hello())
#<b><i>hello world</i></b>


def makebold(f): 
    return lambda: "<b>" + f() + "</b>"
def makeitalic(f): 
    return lambda: "<i>" + f() + "</i>"

@makebold
@makeitalic    
def hello():
    return "hello world"
    
print(hello())
#<b><i>hello world</i></b>


from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()


example.__name__

example.__doc__


def hello():
	'''Docstring'''
	print('hello world')
	
>>> hello.__name__
'hello'
>>> hello.__doc__
'Docstring'
>>> 

def my_decorator(f):
    def wrapper(*args, **kwds):
        print('-----------')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def hello():
    """Docstring"""
    print("hello world")
    
>>> hello()
-----------
hello world
>>> hello.__name__
'wrapper'
>>> hello.__doc__
>>> 

# Update a wrapper function to look like the wrapped function
from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('-----------')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def hello():
    """Docstring"""
    print("hello world")
    
>>> hello()
-----------
hello world
>>> hello.__name__
'hello'
>>> hello.__doc__
'Docstring'
>>> 


>>> hello()
'<b><i>hello world</i></b>'
>>> hello.__name__
'hello'
>>> hello.__doc__
'Docstring'
>>> 

from functools import wraps

def makebold(fn):
    @wraps(fn)
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    @wraps(fn)
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    '''Docstring'''
    return "hello world"

print(hello())
## returns <b><i>hello world</i></b>

def decorate(func):
   def wrapper(self):
       return "<!>{0}<!>".format(func(self))
   return wrapper

class Person(object):
    def __init__(self):
        self.name = "Steve"
        self.surname = "Jobs"

    @decorate
    def get_fullname(self):
        return self.name+" "+self.surname

great_person = Person()
print(great_person.get_fullname())

def decorate(func):
   def wrapper(self):
       return "<!>{0}<!>".format(func(self))
   return wrapper

class Person(object):
    def __init__(self):
        self.name = "Steve"
        self.surname = "Jobs"
        self.company = "Apple"

    @decorate
    def get_fullname(self):
        return self.name+" "+self.surname

    @decorate
    def get_company(self):
        return self.company

great_person = Person()
print(great_person.get_fullname())#<!>Steve Jobs<!>
print(great_person.get_company())#'<!>Apple<!>'

>>> great_person = Person()
>>> great_person.get_fullname()
'<!>Steve Jobs<!>'
>>> great_person.get_company()
'<!>Apple<!>'


def decorate2(func):
   def wrapper(*args, **kwargs):
       return "<!>{0}<!>".format(func(*args, **kwargs))
   return wrapper
   
   
   
def tags(t):
    def decorate(func):
        @wraps(func)
        def wrapper(name):
            return "<{0}>{1}<{0}>".format(t,func(name))
        return wrapper
    return decorate

@tags('!')
@tags('p')
@tags('!')
def welcome(name):
    return "Welcome "+name
    
print(welcome("Arsen"))
#<!><p><!>Welcome Arsen<!><p><!>


from functools import wraps

def make_tag(tag):
    def wrapped(func):
        @wraps(func)
        def decorator():
            return '<{0}>{1}</{0}>'
                .format(tag, func())
        return decorator
    return wrapped

@make_tag('b')
@make_tag('i')
def hello():
    return "hello world"

print(hello())
<b><i>hello world</i></b>

>>> def hi():
        print('Barev')
	
>>> hi()
Barev

>>> class A:
    def __init__(self):
      print("init")
      
    def __call__(self):
      print("call")
     
>>> A()
init
>>> a = A()
init

>>> a = A()
init
>>> a()
call
>>> a.__call__()
call
>>> A()
init
>>> A()()
init
call

>>> callable(A)
True

class makeBold(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        return "<b>{}</b>".format(self.f())


@makeBold
def hello():
    return "hello world"

print(hello())
#<b>hello world</b>


class makeItalic(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        return "<i>{}</i>".format(self.f())
        
@makeItalic
def hello():
    return "hello world"

>>> print(hello())
<i>hello world</i>

class cDecorator(object):
  def __init__(self, tag):
    self.tag = tag

  def __call__(self, f):
    def decf():
      return "<{t}>{f}</{t}>".format(f=f(), t=self.tag)
    return decf


@cDecorator('b')
@cDecorator('i')
def hello():
    return "hello world"

print(hello())
<b><i>hello world</i></b>

class Encapsulation(object):
    def __init__(self, x, y, z):
        self.public = x
        self._protected = y
        self.__private = z


>>> E = Encapsulation(1,2,3)
>>> E.public
1
>>> E._protected
2
>>> E.__private
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    E.__private
AttributeError: 'Encapsulation' object has no attribute '__private'
>>> E._Encapsulation__private
3
>>> 


class Encapsulation2(object):
    def publicMethod(self):
        self.__private = "encapsulated"
        return self.__privateMethod()

    def __privateMethod(self):
        return self.__private

>>> E2 = Encapsulation2()
>>> E2.publicMethod()
'encapsulated'
>>> E2.__privateMethod()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    E2.__privateMethod()
AttributeError: 'Encapsulation2' object has no attribute '__privateMethod'
>>> E2._Encapsulation2__privateMethod()
'encapsulated'
>>> E2._Encapsulation2__private
'encapsulated'
>>> 

class Encapsulation(object):
    def __init__(self, secret):
        self.__secret = secret
        
    def __keepSecret(self):
        return self.__secret
    
    def showSecret(self):
        return self.__keepSecret()
        
>>> s = Encapsulation("pin:4242")
>>>
>>> s.__secret
AttributeError: 'Encapsulation' object has no attribute '__secret'
>>> s.__keepSecret()
AttributeError: 'Encapsulation' object has no attribute '__keepSecret'
>>> s.showSecret()
'pin:4242'

>>> s = Encapsulation("pin:4242")
>>> s._Encapsulation__secret
'pin:4242'
>>> s._Encapsulation__keepSecret()
'pin:4242'
>>> 
                
class Seven(object):
    def __init__(self):
        self.__p = 7
    def printSeven(self):
        print(self.__p)
        
class Eight(Seven):
    def __init__(self):
        super().__init__()
        self.__p = 8
    def printEight(self):
        print(self.__p)
        
>>> x = Eight()
>>> x.printEight()
8
>>> x.printSeven()
7

