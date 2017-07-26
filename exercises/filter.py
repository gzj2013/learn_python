#!/usr/bin/python3
# -*- coding=UTF-8  -*-

def is_odd(n):
    return n % 2 == 1


# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()



"""
练习1
    质数又称素数。指在一个大于1的自然数中，除了1和此整数自身外，不能被其他自然数整除的数。
    偶数一定不是素数，除2之外；
"""
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes(num):
    n = 2
    yield n

    it = _odd_iter() # 初始序列
    # 设置一个退出循环的条件：
    while n < num:
        n = next(it) # 取出序列的下一个数，并使it增长；
        yield n
        it = filter(_not_divisible(n), it) # 过滤掉序列it中那些可被n整除的数
            


"""
练习2
    回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数;
"""
def is_palindrome(n):
    s = str(n)
    bits = int(len(s) / 2)
    x = 0
    ret = True

    if bits == 0:
        return False

    while x < bits:
        ret = ret and (s[x]==s[-x-1])
        x = x+1
    
    return ret


if __name__ == "__main__":
    L=list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
    print(L)
    
    # 打印1000以内的素数:
    output = list(primes(100))
    print(list(output))

    print()
    # 打印1000以内的回数:
    output = filter(is_palindrome, range(1, 1000))
    print(list(output))