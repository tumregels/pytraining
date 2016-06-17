namelist = ['Armen', 'Gago', 'Valod', 'Armin', 'Step', 'Lilo', 'Kiazh']

pets = ['ant', 'bat', 'cow', 'dog', 'elk']


#exercise 4
lst = [159.99, 160.00, 205.95,128.83, 175.49]

>>> 3
3
>>> type(3)
<class 'int'>
>>> 4.4
4.4
>>> type(4.4)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> 3 / 5
0.6
>>> 4 + 10
14
>>> 4 / 2
2.0
>>> 17.0 - 10.0
7.0
>>> 17.0 - 10
7.0
>>> 54 // 10 # integer division
5
>>> 54 % 10 # modulo operator
4
>>> -17 // 10
-2
>>> 3.3 // 1
3.0
>>> 2 ** 4
16
>>> -4
-4
>>> 4 * 4 #binary operator
16
>>> -4 #unary operator
-4
>>> --4
4
>>> ---4
-4
>>> 2 / 3 # finite memory
0.6666666666666666
>>> 5 / 3
1.6666666666666667
>>> 100000000000 + 0.00000000001
100000000000.0
>>> -2 ** 2
-4
>>> (-2)**2
4
>>> "Hello World"
'Hello World'
>>> _
'Hello World'
>>> "my string"
'my string'
>>> type("Hello World")
<class 'str'>
>>> 'new string'
'new string'
>>> type("Hello World")
<class 'str'>
>>> type('new string')
<class 'str'>
>>> 'why string'
'why string'
>>> 'string of letters' # string == lar/arm
'string of letters'
>>> s1 = 'new'
>>> s2 = 'old'
>>> s3 = 'modern'
>>> s1 + s2 + s3
'newoldmodern'
>>> s4 = s1 + ' ' + s2 + s3
>>> s4
'new oldmodern'
>>> ' ' in s4
True
>>> 'o' in s3
True
>>> 'f' not in s4
True
>>> s2 * 4
'oldoldoldold'
>>> (s2 + ' ')*4
'old old old old '
>>> s4
'new oldmodern'
>>> s4[0]
'n'
>>> s4[-1]
'n'
>>> s4[:]
'new oldmodern'
>>> s4[0:2]
'ne'
>>> s4[0:3]
'new'
>>> len(s1)
3
>>> s1.count
<built-in method count of str object at 0x001488E0>
>>> s1.count(n)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s1.count(n)
NameError: name 'n' is not defined
>>> s1.count('n')
1
>>> s4.count("o")
2
>>> s4
'new oldmodern'
>>> print(1+2)
3
>>> print('charles' + 'darwin')
charlesdarwin
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
>>> dir(str)
['__add__', '__class__', ...,'zfill']
>>> type(s4)
<class 'str'>
>>> help(str.strip)
Help on method_descriptor:

strip(...)
    S.strip([chars]) -> str...

>>> s5 = ' This is in the middle '
>>> s5.strip()
'This is in the middle'
>>> namelist = ['Armen','Gago ','Valod','Armin',
			'Step ','Lilo ','Kiazh']	
>>> lst = [159.99, 160.00, 205.95,128.83, 175.49]
>>> lst.append(160.00)
>>> lst.count(160.00)
2
>>> min(lst)
128.83
>>> lst.index(128.83)
3
>>> lst.remove(128.83)
>>> lst
[159.99, 160.0, 205.95, 175.49, 160.0]
>>> lst.sort()
>>> lst
[159.99, 160.0, 160.0, 175.49, 205.95]
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," he said.'
'"Yes," he said.'
>>> "\"Yes,\" he said."
'"Yes," he said.'
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'
>>> print('"Isn\'t," she said.')
"Isn't," she said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements
>>> # with an empty list
>>> letters[:] = []
>>> letters
[]
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while b < 10:
...     print(b)
...     a, b = b, a+b
...
1
1
2
3
5
8
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
>>> a, b = 0, 1
>>> while b < 1000:
...     print(b, end=',')
...     a, b = b, a+b
...
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
