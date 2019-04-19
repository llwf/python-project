#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

with request.urlopen("http://www.baidu.com") as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
#	print('Data:', data.decode('utf-8'))
	
print("++++++++++++++++++++++")	
with request.urlopen("http://www.google.com") as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
#	print('Data:', data.decode('utf-8'))
	
from urllib import request

req = request.Request('http://www.baidu.com/')
#req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
	
import json
	
def fetch_data(url):
	with request.urlopen(url) as f:
		data = f.read()
		return json.loads(data.decode('utf-8'))
		
URL='http://news-at.zhihu.com/api/4/news/latest'
data=fetch_data(URL)
print(data)
print('ok')