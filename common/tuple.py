#! /usr/bin/python3
# *-* coding=utf-8 *-*

# 元组
# tuple和list非常类似，但是tuple一旦初始化就不能修改,因此它也没有append()，insert()方法
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print('len = %d' % len(classmates))

# 用索引来访问tuple中每一个位置的元素，记得索引是从0开始的
print(classmates[0])
print(classmates[1])
print(classmates[2])

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)

# tuple里面的元素的数据类型也可以不同
L = ('Apple', 123, True)
print(L)

# tuple元素也可以是另一个tuple或list
s = ('python', 'java', ('asp', 'php'), 'scheme')
print(len(s))


# “可变的”tuple
s = ('python', 'java', ['asp', 'php'], 'scheme')
print(len(s))
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，
# 而是list的元素。tuple一开始指向的list并没有改成别的list，所以，
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，
# 就不能改成指向其他对象，但指向的这个list本身是可变的！