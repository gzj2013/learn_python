#!/usr/bin/python3
# -*- coding: UTF-8 -*-

print('包含中文的str')

# ord()函数获取字符的整数表示，
# chr()函数把编码转换为对应的字符
a = ord('A')
b = ord('中')
print(a)
print(b)

# '\u'表示为unicode编码
a = chr(66)
b = chr(25991)
c = '\u4e2d\u6587'        
print(a)
print(b)
print(c)

s = 'ABC'
x = s.encode('ascii')
y = b'ABC'
z = '中文'.encode('utf-8')
zz = b'\xe4\xb8\xad\xe6\x96\x87'

print(x.decode('ascii'), y.decode('ascii'))
print(z.decode('utf-8'), zz.decode('utf-8'))

# len()函数计算的是str的字符数 
length = len('abc')
print(length)

#如果换成bytes，len()函数就计算字节数
len1 = len('ABC'.encode('ascii'))
len2 = len('中文'.encode('utf-8'))
len3 = len(b'\xe4\xb8\xad\xe6\x96\x87')
print(len1, len2, len3)

# %s永远起作用，它会把任何数据类型转换为字符串
# %d  整数
# %f  浮点数
# %s  字符串
# %x  十六进制整数
a = 'Hello, %s' % 'world'

b = '%02d-%02d' % (3, 1)
c = '%02d-%2d' % (3, 1)

d = '%.6f' % 3.1415926

e = 'Age: %s, Gender:%s'  % (25, 'Man')

f = 'growth rate: %d%%' % 7

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 小明的成绩从去年的72分提升到了今年的85分，
# 请计算小明成绩提升的百分点，
# 并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s_last = 72
s_current = 85

growth_rate = 100*(s_current - s_last)/s_last

print('Growth Rate: %.2f%%' % growth_rate)