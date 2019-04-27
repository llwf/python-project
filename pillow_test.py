#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

# 打开一个png图像文件，注意是当前路径:
im = Image.open('file/mat_depth.png')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w/2, h/2))
print('Resize image to: %sx%s' % (w/2, h/2))
# 把缩放后的图像用png格式保存:
im.save('file/thumbnail.png', 'png')

flower = Image.open('file/flower.jpg')
blur_flower = flower.filter(ImageFilter.BLUR)
blur_flower.save('file/blur_flower.jpg', 'jpeg')



