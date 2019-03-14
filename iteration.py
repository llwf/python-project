#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

from collections import Iterable

d = {'a':1, 2:'b', 'c':3, 'asd':456.2, 5:'2323'}

for key in d:
	print(key)

for value in d.values():
	print(value)

for key, value in d.items():
	print(key,value)

str = "abcdefghijklmnopqrstuvwxyz"
for ch in str:
	print(ch)

print(isinstance(d, Iterable))
print(isinstance(str, Iterable))
print(isinstance(12333, Iterable))
print(isinstance([1,2,3,4], Iterable))
print(isinstance((1,2,3,4), Iterable))

for i, value in enumerate(str):
	print(i, '-->', value)
for i, value in enumerate(d):
	print(i, '-->', value)
	
def findMinAndMax(L):
	if L == []:
		return (None, None)
	min=max=L[0]
	for value in L:
		if min > value:
			min = value
		elif max < value:
			max = value
	return (min, max)
	
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')