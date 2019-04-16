#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

#distri_task_master.py

import time, queue, sys
from multiprocessing.managers import BaseManager

#创建QueueManager
class QueueManager(BaseManager):
	pass
	
#由于这个QueueManager只是从网络上获取Queue，只用提供注册名字，不用绑定回调Queue
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器
server_addr = '127.0.0.1'
print('Connect to server %s' % server_addr)
#端口和auth key必须和服务器端一致，才能保证通信正常
port = 5000
auth_key = b'llwf'
m = QueueManager(address = (server_addr, port), authkey = auth_key)
#从网络连接
m.connect()
#获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()

#从task队列获取任务，然后执行，执行后把结果写入result队列
for i in range(10):
	try:
		n =  task.get(timeout = 5)
		print('Run work task %s*%s...' % (n, n))
		r = '%s * %s = %s' % (n, n, n*n)
		time.sleep(1)
		result.put(r)
	except queue.Empty:
		print('Task Queue is empty.')
#处理结束
print('Worker finished and exit.')