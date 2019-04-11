#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import os

with open('./config.ini') as f:
	print(f.read())
	print('++++++++++')

with open('./config.ini') as f:
	i = 0
	for line in f.readlines():
		i += 1
		print('%d: %s' % (i, line.strip()))

with open('./config.ini', 'a') as f:
	f.write('\nthis is append line')
	
with open('./pic.jpg', 'rb') as f:
	byte = f.read(20)
	for i in range(20):
		print("0x%x" % byte[i])

with open('./file.txt', 'w') as f:
	f.write('\nthis is append line')
	
os.rename('file.txt', 'new_file.txt')
os.remove('new_file.txt')

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

print('+++++++++++++++++++')		
def find_file(str, path = '.'):
	file_list = []
	path = os.path.abspath(path)
	for x in os.listdir(path):
		current = os.path.join(path, x)
		if os.path.isdir(current):
			file_list += find_file(str, current)
		elif x.find(str) > -1:
			file_list.append(current)
	return file_list

if __name__ == '__main__':
	print(find_file('test', 'E:\\Study\\Python\\python-project'))
	print('\n--------------\n')
	print(find_file('class'))	
	print('\n--------------\n')
	print(find_file('IMG', 'E:\\Study\\Python'))	
	
