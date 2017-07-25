#!/usr/bin/python3
# -*- coding=UTF-8 -*-

# 练习
"""
杨辉三角定义如下：

          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
"""

def triangles(max):
    n = 1
  
    while n < max:

        if n == 1:
            L = [1]
            yield(L)
        else:
            index = 1
            L = [1,1]

            while index < n-1:    # fill the elements inside
                L.insert(index, L_pre[index-1]+L_pre[index])
                index = index +1
                     
            yield(L)
            L_pre = L

        n = n+1

    return "done"

if __name__ == '__main__':
    t= triangles(10);
    for x in t:
        print(x)