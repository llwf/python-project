#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

from func import my_abs, func_none
from math import *
	
print(my_abs(-999))
print(my_abs(-15.63343))

def move(x, y, step, angle=0):
	nx = x + step*cos(angle)
	ny = y + step*sin(angle)
	return nx, ny
print(move(200, 300, 20, pi/6))
print(pi,'1\n\n')
func_none()
print(pi,'2\n\n')
print(func_none())