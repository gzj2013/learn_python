#!/usr/bin/python3
# -*- coding=UTF-8  -*-

class Student(object):
    """docstring for Student"""
    def __init__(self, name, score):
        super(Student, self).__init__()
        self.name = name
        self.score = score
        
    def print_score(self):
        print('name=%s, score=%s' % (self.name, self.score))

if __name__=='__main__':
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()