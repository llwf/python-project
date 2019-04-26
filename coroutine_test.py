#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#consumer函数是一个generator是一个生成器（带有yield的函数都是生成器）
#生成器包含send函数，可以传入参数并启动执行，close函数，关闭generator生成器资源
def consumer():
	r = 'init'
	while True:
		# input << yield << ret
		# yield关键字，在此生成器函数返回，后面附件的表达式结果作为返回值
		#同时可以将yield赋值给一个函数局部变量，通过send(x)就可以将外部的x传给变量n
		n = yield r
		if not n:
			print('n is null')
			return
		print('[CONSUMER] Consuming %s...' % n)
		r = '200 OK'

def produce(c):
	#启动生成器,初始传入参数必须是None
	r = c.send(None)
	print('[PRODUCER] start Consumer return: %s' % r)
	n = 0
	while n < 5:
		n += 1
		print('[PRODUCER] Producing %s...' % n)
		#切换到consumer执行consuming, consumer通过yield拿到传入的n后赋值给n然后往下执行
		r = c.send(n)
		#执行完了后又到了yield，然后通过yield传回来r
		#
		#produce拿到consumer的执行结果后可以进行后续操作，然后继续执行下一个producer
		print('[PRODUCER] Consumer return: %s' % r)
	#produce生产完后，通过c.close关闭consumer
	c.close()

c = consumer()
produce(c)