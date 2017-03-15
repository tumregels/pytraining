def countdown(n):
    print(n)
    countdown(n - 1)


def countdown(n):
    'counts down to 0'
    if n <= 0:
        print('Blastoff!!!')
    else:
        print(n)
        countdown(n - 1)


def vertical(n):
    '''prints digits of
    n vertically
    '''
    if n < 10:
        print(n)
    else:
        # to do

def vertical(n):
    '''prints digits of
    n vertically
    '''
    if n < 10:
        print(n)
    else:
        vertical(n // 10)
        print(n % 10)
        print(n % 10)


def summa(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + summa(numList[1:])


print(summa([1, 3, 5, 7, 9]))

# ---------

import module_name

def func_name_1:
    pass


def func_name_2:
    pass


def main():
    pass


if __name__ == "__main__":
    main()

# ---------
