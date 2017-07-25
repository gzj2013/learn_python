#!/usr/bin/python3
# -*- coding=UTF-8  -*-

"""
1. 利用 map() 函数，把用户输入否认不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入 ： [‘adam’,’LISA’,’barT’], 
输出 ：[‘Adam’,’Lisa’,’Bart’]

2. Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，
可以接受一个list并利用reduce()求积：

3. 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
思路：char2num函数用来将字符串转化为int，然后我们跳过小数点，将123.456变为123456，
再用reduce函数 把它们变为整数，最后除以10^n 即可得到对应的小数
"""
from functools import reduce

def normalize(str):
    return str[:1].upper() + str[1:].lower()

def prod(x, y):
    return x*y

def str2float(s):  
    def char2num(s):  
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]  
 
    n = s.index('.')  
    factor = len(s) - 1 - n   # 小数点后几位
 
    s = s[:n]+s[n+1:]     # 去掉小数点
    return reduce(lambda x,y:x*10+y,map(char2num, s))/(10**factor)  

if __name__ == '__main__':      
    L1=['adam','LISA','barT']
    L2=list(map(normalize,L1))
    print(L2)

    L3 = reduce(prod, [1,2,3,4,5])
    print(L3)

    print('str2float(\'123.4567\') =', str2float('123.4567'))
