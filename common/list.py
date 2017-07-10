#! /usr/bin/python3
# *-* coding=utf-8 *-*

classmates = ['Michale', 'Bob', 'Tracy']

print(classmates)
print('len = %d' % len(classmates))

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0])
print(classmates[1])
print(classmates[2])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates)

# 删除list末尾的元素
classmates.pop()
print(classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(L)

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))