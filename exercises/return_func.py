#!/usr/bin/python3
# -*- coding=UTF-8  -*-

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

def count_1():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
    

if __name__ == "__main__":
    sum = calc_sum(1,2,3,4)
    print(sum)

    f = lazy_sum(1, 3, 5, 7, 9)
    print(f())

    f1,f2,f3 = count_1()
    print(f1(),f2(),f3())
    f1,f2,f3 = count()
    print(f1(),f2(),f3())