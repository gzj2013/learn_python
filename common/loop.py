#! /usr/bin/python3
# *-* coding=utf-8 *-*

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print('Hello %s!' % name)

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



# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 比如我们要计算100以内所有奇数之和，可以用while循环实现
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

