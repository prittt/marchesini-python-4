import sys
import functools
import builtins

def print_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        old_print = builtins.print
        def print(*args, **kwargs):
            old_print("--- Marchesini ---", end=" ")
            old_print(*args, **kwargs)
        builtins.print = print
        ret =  func(*args, **kwargs)
        builtins.print = old_print
        return ret

    return wrapper

# def print_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         global print
#         old_print = print
#         def print(*args, **kwargs):
#             old_print("--- Marchesini ---", end=" ")
#             old_print(*args, **kwargs)
#         ret =  func(*args, **kwargs)
#         print = old_print
#         return ret

#     return wrapper


@print_decorator
def myfun1():
    print('myfun1-a')
    print('myfun1-b')

def myfun2():
    print('myfun2-a')
    print('myfun2-b')

# Test delle funzioni
myfun1()
myfun2()
myfun1()
myfun2()
