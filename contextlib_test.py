#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager

class Query(object):
	def __init__(self, name):
		self.name = name
		
	def __enter__(self):
		print('Enter')
		return self
		
	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type:
			print('Error')
		else:
			print('Exit')
			
	def query(self):
		print('Query info about %s...' % self.name)
		
with Query('Jeff') as q:
	q.query()
	
@contextmanager
def tag(name):
	print("<%s>" % name)
	yield
	print("</%s>" % name)
	
with tag("h1"):
	print("hello")
	print("world")
	
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(line)
