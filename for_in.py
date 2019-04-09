#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

sum = 0
num = list(range(101))
for i in num:
	sum = sum + i
print(sum)

sum = 0
n = 0
while n < 99:
	sum = sum + n
	n = n + 2
	if sum > 1000:
		break
print(sum)

sum = 0
n = 0
while n < 99:
	n = n + 1
	if n%2 == 0:
		continue
	sum = sum + n
print(sum)