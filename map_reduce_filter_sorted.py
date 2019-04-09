#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

from functools import reduce

def normalize(name):
	return name[:1].upper()+name[1:].lower()
	
L1 = ['adam', 'BILL', 'liSA', 'Garry']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
	return reduce(lambda x, y: x*y, L)

print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
	print('测试成功！')
else:
	print('测试失败！')

	

def str2float(s):
	DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}	
	def char2num(c):
		return DIGITS[c]
	def fn(x, y):
		return x*10+y
	intNum, floatNum = s.split('.')
	intNum = reduce(fn, map(char2num, intNum))
	floatNum = 10**(-len(floatNum))*reduce(fn, map(char2num, floatNum))
	return intNum + floatNum

print('str2float(\'123.456\') = ', str2float('123.456'))
if(abs(str2float('123.456')-123.456) < 0.00001):
	print('测试成功！')
else:
	print('测试失败！')
#if(abs(str2float('123')-123) < 0.00001):
#	print('测试成功！')
#else:
#	print('测试失败！')
if(abs(str2float('123.0')-123.0) < 0.00001):
	print('测试成功！')
else:
	print('测试失败！')
if(abs(str2float('0.123')-0.123) < 0.00001):
	print('测试成功！')
else:
	print('测试失败！')

def is_odd(n):
	return n % 2 == 1
	
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15])))

def not_empty(s):
	return s and s.strip()
	
print(list(filter(not_empty, ['A', '', None, ' B', 'C ', '  '])))


def _int_iter():#生成器生成从3开始的无限奇数序列
    n = 1
    while True:
        n = n + 2
        yield n
 
def  _not_divisible(n):#定义筛选函数
    return lambda x:x % n > 0
 
def primes():
    yield 2          #先返回一个2
    it = _int_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
for n in primes():#构造循环条件，使之可以输出任何范围的素数序列
    if n < 1000:
        print(n)
    else:
        break
		
def _odd_iter():#奇数生成器生成从3开始的奇数
	n = 1
	while True:
		n = n + 2
		yield n
		
def _not_divisible(n):#定义质数筛选函数
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter()#初始化序列
	while True:
		n = next(it)#返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it)#生成筛选后的序列

for n in primes():
	if n < 1000:
		print(n)
	else:
		break
		
	

#测试
output = filter(lambda x: str(x) == str(x)[::-1], range(1, 1000))
print('1~1000:', list(output))
if list(filter(lambda x: str(x) == str(x)[::-1], range(1, 200))) == [1, 2, 3, 4, 5, 6,
7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141,
151, 161, 171, 181, 191]:
	print('测试成功！')
else:
	print('测试失败！')

def is_palindrome(n):
	return str(n) == str(n)[::-1]
	
#测试
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6,
7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141,
151, 161, 171, 181, 191]:
	print('测试成功！')
else:
	print('测试失败！')	
	
L = [25, -56, 0, 88, 23, 485, -95]	
print(sorted(L))
print(sorted(L, key=abs))	
print(sorted(L, key=abs, reverse=True))	
print(sorted(L, reverse=True))

Name = ['Bob', 'ada', 'Lisa', 'koby']
print(sorted(Name))
print(sorted(Name, key=str.lower))	
print(sorted(Name, key=str.lower, reverse=True))	
print(sorted(Name, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0].lower()
	
def by_score(t):
	return t[1]

print(sorted(L, key=by_name))
print(sorted(L, key=by_score, reverse=True))











		



	