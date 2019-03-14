#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'abcdefghijk']

print(L[0:3])
print(L[2:3])
print(L[:3])
print(L[-2:-1])
print(L[-1:-2])
print(L[-3:])
print(L[-3:-1])
print(L[-3:4])
print(L[-1:])
print(L[-1])
print(L[-1][:3])
print(L[-1][3])


L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:21])
print(L[:10:2])
print(L[-10::3])
print(L[10:21:5])
print(L[::5])
print(L[:])

def trim(s):
	while s[:1] == " ":
		s=s[1:]
	while s[-1:] == " ":
		s=s[:-1]
	return s
	
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')