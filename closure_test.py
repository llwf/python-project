#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

def createCounter():
	count = 0
	def counter():
		nonlocal count
		count =  count + 1
		return count
	return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
	
def is_odd(n):
	return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)
L = list(filter(lambda n: n % 2, range(1, 20)))
print(L)