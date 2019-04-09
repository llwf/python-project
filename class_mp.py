#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
	pass

class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass
	
class Runnable(object):
	def run(self):
		print('Running...')
		
class Flyable(object):
	def fly(self):
		print('Flying...')
		

class Dog(Mammal, Runnable):
	pass
	
class Bat(Mammal, Flyable):
	pass
	
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a
	def __getitem__(self, n):
		if isinstance(n, int): # n是索引
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice): # n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda: 24
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
		
for n in Fib():
	print(n)
print(Fib()[10])
print(Fib()[:11])	
print(Fib()[3:11])
print(Fib)			
		
f = Fib()
for n in f:
	print(n)
print(f[10])
print(f[:11])	
print(f[3:11])
print(f)			
print(f.score)				
print(f.age())						
print(f.name)		
		
		
		
		
		
		
		
		
		
		
		