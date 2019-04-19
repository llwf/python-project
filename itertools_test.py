#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

naturals = itertools.count(1)
for n in naturals:
	if n > 100:
		break
	print(n)
naturals = itertools.count(3)
for n in naturals:
	if n > 100:
		break
	print(n)
	
cs = itertools.cycle('ABC')
n = 0
for c in cs:
	n += 1
	if n > 100:
		break
	print(c)
	
rs = itertools.repeat('ABC', 3)
for c in rs:
	print(c)
	
naturals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, naturals)
print(list(ns))

for c in itertools.chain('ABC', 'XYZ'):
	print(c)
	
for key, group in itertools.groupby('AAABBCCCAACCBB'):
	print(key, list(group))
	

def pi(N):
    # 计算pi的值 
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

    # step 4: 求和:
	n = itertools.count(1)
	ns = itertools.takewhile(lambda x: x <= N, n)
	PI = 0
	for ni in ns:
		if ni % 2 == 0:
			x = -4/(2*ni-1)
		else:
			x = 4/(2*ni-1)
		PI += x
	return PI

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
print(pi(1000000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

def pi_2(N):
	odd = itertools.count(1, 2)
	f = itertools.cycle((4, -4))
	PI = 0
	for i in range(N):
		PI += (next(f)/next(odd))
	return PI

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
print(pi(1000000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')	
	

