#! /usr/bin/python3
# *-* coding=utf-8 *-*

# Python内置了字典：dict的支持，dict全称dictionary.
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
names = ['Michale', 'Bob', 'Tracy']
scores = [95, 75, 85]

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
d = {'Michale':95, 'Bob':75, 'Tracy':85}
d['Michale'] = 88
print(d['Michale'])

# 这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置.
# 这样，取的时候才能根据key直接拿到value。

print('Thomas' in d)
print(d.get('Thomas'))    # 注意：返回None的时候Python的交互式命令行不显示结果。
print(d.get('Thomas', 90))


# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)

# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，
# 需要牢记的第一条就是dict的key必须是不可变对象。这是因为dict根据key来计算value的存储
# 位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位
# 置的算法称为哈希算法（Hash）。要保证hash的正确性，作为key的对象就不能变。
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
# 而list是可变的，就不能作为key.

# 使用key-value存储结构的dict在Python中非常有用，
# 选择不可变对象作为key很重要，最常用的key是字符串。

