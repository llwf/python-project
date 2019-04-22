#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, string

def rndChar():
	s = string.ascii_letters + string.digits
	return random.choice(s)

def rndBGColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
	
def rndFontColor():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#二维码宽、高	
width = 60*4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('arial.ttf', 36)

draw = ImageDraw.Draw(image)

#验证码背景填充随机颜色
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill = rndBGColor())

#打上四个随机验证码并填充颜色
chars = []
for t in range(4):
	c = rndChar()
	chars += c
	draw.text((60*t + 10, 10), c, font = font, fill = rndFontColor())
	
#模糊验证码图片：
image = image.filter(ImageFilter.BLUR)
name = 'file/' + ''.join(chars) + '.jpg'
image.save(name, 'jpeg')