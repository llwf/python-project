#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import logging

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:\'%s\'' % e)
		logging.exception(e)
	finally:
		print('finally...')
main()
print('END')

# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
	n = 2
	try:
		n = foo('0')
	except ValueError as e:
		print('ValueError!:', n)
#		raise
	finally:
		print('result:', n)
bar()
print('+++++++++++++++++++++++++++++++++++')
print('Test 2')
from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
