#!/usr/bin/python3
# -*- coding=UTF-8  -*-

"""
"""



def is_odd(n):
    return n % 2 == 1


# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()



def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

        
if __name__ == "__main__":
    L=list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
    print(L)
    
    # 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

    # 打印1000以内的素数:
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
