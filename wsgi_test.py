#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

#http响应处理函数
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'Web')
#	print(environ)
	return [body.encode('utf-8')]

#创建服务器，IP为空，端口8000，处理函数application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
#开始监听HTTP请求
httpd.serve_forever()