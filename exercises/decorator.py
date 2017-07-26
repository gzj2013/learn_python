#!/usr/bin/python3
# -*- coding=UTF-8  -*-
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call')
        # print('call %s():' % func.__name__)
        ret_func = func(*args, **kw)
        print('end call')
        return ret_func
    return wrapper


def log_1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


def log_2(text):
    if isinstance(text, str):

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decorator
    else:

        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('call %s():' % text.__name__)
            return text(*args, **kw)

        return wrapper

# 借助Python的@语法，把decorator置于函数的定义处：
@log_2
def now():
    print('2017-07-24')

@log_2('execute')
def now_1():
    print('2017-07-24')

if __name__ == "__main__":
    now()
    print
    # print(now.__name__)
    now_1()
    # print(now_1.__name__)
