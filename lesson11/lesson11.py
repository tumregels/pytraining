def derivative(f, h):
    '''Returns a function
    which is approximation of
    the derivative of f with respect to h'''

    return lambda x: (f(x + h) - f(x)) / h


def square(x): return x ** 2


# g = derivative(square, 0.001)
# g(5)
# 10.001000000002591


def kthDerivative(f, h, k):
    '''Returns a new function that is the approximation of
    the kth derivative of f with respect to h.'''
    if k == 1:
        return derivative(f, h)
    else:
        return derivative(kthDerivative(f, h, k - 1), h)


def quartic(x):
    '''Returns x**4.'''

    return x ** 4  # g = kthDerivative(quartic, 0.0001, 3)
# g(10)
# 241.9255906715989 # should be 240


def wrap(pre, post):
    def decorate(func):
        def call(*args, **kwargs):
            pre(func, *args, **kwargs)
            result = func(*args, **kwargs)
            post(func, *args, **kwargs)

            return result
        return call
    return decorate


def trace_in(func, *args, **kwargs):
    print("Entering function", func.__name__)


def trace_out(func, *args, **kwargs):
    print("Leaving function", func.__name__)


@wrap(trace_in, trace_out)
def calc(x, y):
    return x + y

# print(calc(1,2))
# ('Entering function', 'calc')
# ('Leaving function', 'calc')
# 3
