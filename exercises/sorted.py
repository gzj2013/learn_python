#!/usr/bin/python3
# -*- coding=UTF-8  -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]  
  
def by_name(t):  
    return t[0] 

def by_score(t):  
    return t[1]  
  
if __name__ == "__main__":
    L1 = sorted(L, key=by_name)  
    print(L1)  
    L2 = sorted(L, key=by_score, reverse=True)  
    print(L2)  