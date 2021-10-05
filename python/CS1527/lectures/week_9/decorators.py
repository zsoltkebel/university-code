def our_decorator(func):
    def function_wrapper(x):
        print('Before calling' + func.__name__)
        func(x)
        print('After calling' + func.__name__)
    return function_wrapper

def foo(x):
    print('Hi, foo has been called with ' + str(x))


foo('Hi')

foo = our_decorator(foo)
foo(42)

@our_decorator
def foo_2(x):
    print('Hi, foo has been called with ' + str(x))

foo_2(42)
