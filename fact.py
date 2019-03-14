#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)

print(fact(10))
print(fact(100))
print(fact(800))

def fact_new(n):
	return fact_iter(n, 1)
	
def fact_iter(num, base):
	if num == 1:
		return base
	return fact_iter(num - 1, num * base)
	
print('/n/n new')
print(fact(10))
print(fact(100))
print(fact(800))
print(fact(1000))