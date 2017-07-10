#!/usr/bin/python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


class Animal(object):
	def __init__(self, name, leg):
		self.name = name
		self.leg = leg

	def print_score(self):
		print('%s: %s' % (self.name, self.leg))
bart = Animal('Bart Simpson', 59)
lisa = Animal('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()