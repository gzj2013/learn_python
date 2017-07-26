#!/usr/bin/python3
# -*- coding=UTF-8  -*-

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
        
if __name__=='__main__':
    test()
    print ('你好,世界')

    '''
    这是多行注释，使用单引号。
    这是多行注释，使用单引号。
    这是多行注释，使用单引号。
    '''
    print("I'am \"IronMan\"")
    print(r'\\\t\\')
    print('\\\t\\')
    print(r'''this is the first line 
    this is the second line
    this is the third line''')