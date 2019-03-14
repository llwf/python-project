#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

#
# a*x^2+b*x+c=0
#

import math
import cmath

def quadratic(a, b, c):
	if not isinstance(a+b+c, (int, float)):
		raise TypeError('bad operand type of quadratic')
	if a != 0:
		delta = math.pow(b, 2) - 4*a*c
		if delta >= 0:
			x1 = (-b + math.sqrt(delta)) / (2*a)
			x2 = (-b - math.sqrt(delta)) / (2*a)
		else:
			x3 = (-b + cmath.sqrt(delta)) / (2*a)
			x4 = (-b - cmath.sqrt(delta)) / (2*a)
			x1 = complex(x3.real, round(float(x3.imag), 2))
			x2 = complex(x4.real, round(float(x4.imag), 2))
	elif b != 0:
		return -c/b
	else:
		raise ValueError("方程无解")
	return x1, x2
	
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
	
print('quadratic(0, 3, 1) =', quadratic(0, 3, 1))

print('quadratic(2, 0, 1) =', quadratic(2, 0, 1))