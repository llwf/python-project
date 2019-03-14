#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type, only int/float accept')
	if x >= 0:
		return x
	else:
		return -x
		
def func_none():
	pass