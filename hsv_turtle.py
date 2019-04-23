#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

from turtle import *

def HSV2RBG(hue, s, v):
	hi = int(hue/60)%6
	f = hue/60 - hi
	p = v*(1-s)
	q = v*(1-f*s)
	t = v*(1-(1-f)*s)
	RGB = [0.0, 0.0, 0.0]
	if hi == 0:
		RGB = [v, t, p]
	elif hi == 1:
		RGB = [q, v, p]
	elif hi == 2:
		RGB = [p, v, t]
	elif hi == 3:
		RGB = [p, q, v]
	elif hi == 4:
		RGB = [t, p, v]
	elif hi == 5:
		RGB = [v, p, q]
	return RGB
	
def drawHSV(s, v):
	hue = 0.0
	color(1, 0, 0)
	width(30)
	for i in range(356):
		RGB = HSV2RBG(hue, s, v)
		color(RGB[0], RGB[1], RGB[2])
		rt(1)
		hue += 1
		fd(3)

def drawRainbow():
	hue = 0.0
	color(1, 0, 0)
	speed(100)
	hideturtle()
	pensize(3)
	pu()
	goto(-400, -300)
	pd()
	right(100)
	for i in range(330):
		circle(1000)
		right(0.08)
		hue += 1
		RGB = HSV2RBG(hue, 1, 1)
		color(RGB[0], RGB[1], RGB[2])
		
speed('fastest')
pu()
goto(0, 200)
pd()
drawHSV(1.0, 1.0)
pu()
goto(200, 150)
pd()
drawHSV(0.5, 0.8)
drawRainbow()
done()