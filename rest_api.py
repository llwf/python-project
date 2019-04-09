#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

from enum import Enum, unique

class Chain(object):
	def __init__(self, path = ''):
		self._path = path
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __str__(self):
		return self._path
	__repr__ = __str__

print(Chain().status.user.timeline.list)

class Chain2(object):
	def __init__(self, path = ''):
		self._path = path
	def __getattr__(self, path):
		return Chain2('%s/%s' % (self._path, path))
	def __call__(self, var):
		return Chain2('%s/%s' % (self._path, var))
	def __str__(self):
		return self._path
	__repr__ = __str__

print(Chain2().status.user.timeline.list)		
print(Chain2().users('michael').repos)			
print(Chain2().users('michael').repos.project('hello'))				
		

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)
for date in Month:
	print(date.name, '=>', date, ',', date.value)	

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
	
print(Weekday.Sun)
print(Weekday['Mon'])
print(Weekday.Tue.value)
print(Weekday(6))	
#print(Weekday(7))

@unique
class Gender(Enum):
		Male = 0
		Femal = 1
class Student(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


	