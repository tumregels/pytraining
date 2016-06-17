x = 34 - 23      # A comment.
y = "Hello"
z = 3.45    
if z == 3.45 or y == "Hello":
    x = x + 1
    y = y + " World"
print(x)
print(y)

x = 42

if x > 1 :
    print('More than one')
    if x < 100 : 
        print('Less than 100')

print('All done')

if x < 2 :
    print('Small')
elif x < 10 :
    print ('Medium')
else :
    print('LARGE')
print('All done')


for word in ['stop', 'desktop', 'post', 'top']:
    if 'top' in word:
        print(word)
print('Done.')

x='Python'
while x:
    print(x)
    x=x[1:]
    
answer = "no"
while answer == "no":
        answer = input("Are we there? ")
print("We're there!")

epsilon = 1.0
while 1.0 + epsilon > 1.0:
    epsilon = epsilon / 2.0
    print(epsilon)

epsilon = 2.0 * epsilon
print(epsilon)

num=6
while num > 0:
    print (‘*’ * num)
    num = num-1
    




