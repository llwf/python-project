#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

count = 0
def hanoi(n, a, b, c):
	global count
	if n == 1:
		count = count + 1
		print(a, '-->', c)
	else:
		hanoi(n-1, a, c, b)
		count = count + 1
		print(a, '-->', c)
		hanoi(n-1, b, a, c)

hanoi(5, 'A', 'B', 'C')
print(count)