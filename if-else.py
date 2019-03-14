#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

name=input('what\'s your name:')
height=float(input('身高m：'))
weight=float(input('体重KG: '))
bmi = weight/(height**2)

if bmi > 32:
	print(name, 'bmi:', bmi, '严重肥胖')
elif bmi > 28:
	print(name, 'bmi:', bmi, '肥胖')
elif bmi > 25:
	print(name, 'bmi:', bmi, '过重')
elif bmi > 18.5:
	print(name, 'bmi:', bmi, '正常')
else:
	print(name, 'bmi:', bmi, '过轻')