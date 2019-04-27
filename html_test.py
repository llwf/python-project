#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)
	def handle_endtag(self, tag):
		print('</%s>' % tag)
	def handle_startendtag(self, tag, attrs):
		print('<%s/>' % tag)
	def handle_data(self, data):
		print(data)
	def handle_comment(self, data):
		print('<!--', data, '-->')
	def handle_entityref(self, name):
		print('&%s;' % name)
	def handle_charref(self, name):
		print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

from urllib import request
import ssl
import re

class MyPythonEventHTMLParser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.__flag = ''
	def handle_starttag(self, tag, attrs):
		if tag == 'h3' and ('class', 'event-title') in attrs:
			self.__flag = 'title'
		elif tag == 'time':
			self.__flag =  'time'
		elif tag == 'span' and ('class', 'say-no-more') in attrs:
			self.__flag = 'year'
		elif tag == 'span' and ('class', 'event-location') in attrs:
			self.__flag = 'location'
			
	def handle_endtag(self, tag):
		self.__flag = ''
	def handle_data(self, data):
		if self.__flag == 'title':
			print('会议：%s' % data)
		elif self.__flag == 'time':
			print('会议时间：%s' % data)
		elif self.__flag == 'year':
			if re.match(r'\s\d{4}', data):
				print('会议年份：%s' % data)
		elif self.__flag == 'location':
			print('会议地点：%s' % data)
			print('++++++++++++++++++++')

URL = r'''https://www.python.org/events/python-events/'''
parser = MyPythonEventHTMLParser()
context = ssl._create_unverified_context() #这是针对ssl验证问题
with request.urlopen(URL, timeout = 4, context = context) as f:
	page = f.read()
parser.feed(page.decode('utf-8'))
