#! /usr/bin/python3
# *-* coding=utf-8 *-*

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9]:
    sum += x
print(sum)

sum = 0
for x in range(101):
    sum += x
print(sum)


# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
# 比如range(5)生成的序列是从0开始小于5的整数：
print(list(range(5)))



