#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

#obj.y = 11
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 20)
print(getattr(obj, 'y'))

class Student(object):
	name = 'Student'
	count = 0
	def __init__(self, name):
		self.name = name
		Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
			
class Student2(object):
	__slots__ = ('name', 'age')
	
s = Student2()
s.name = 'Michael'
s.age = 25
#s.score = 99

class GraduateStudent(Student2):
	pass
	
g = GraduateStudent()
g.score = 100

class Student3(object):
	@property
	def birth(self):
#		print('birth get value %s' % self._birth)
		return self._birth
	@birth.setter
	def birth(self, value):
#		print('birth value %s' % value)
		self._birth = value
	
	@property
	def age(self):
		return 2019 - self._birth

s3 = Student3()
s3.birth = 2000
print(s3.birth)
# s3.age = 10
print(s3.age)

class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self, value):
		self._width = value
	
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, value):
		self._height = value
	
	@property
	def resolution(self):
		return self._width*self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')