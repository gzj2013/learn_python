#! /usr/bin/python3
# *-* coding=utf-8 *-*

# 再议不可变对象

# str是不变对象，而list是可变对象。
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)

# 而对于不可变对象，比如str，对str进行操作呢：
s = 'abc'
b = s.replace('b', 'S')
print(s)
print(b)

# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。



# tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
a = set([(1, 2, 3), (4, 5, 6)])
print(a)
b = set([1, 2, 3])
print(b)

c = {(1, 2, 3):15, }
print(c)
print(c[(1,2,3)])