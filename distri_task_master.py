#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

#distri_task_master.py

import time, queue, random
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()

#windows定义callable函数
def func_task_queue():
	global task_queue
	return task_queue
def func_result_queue():
	global result_queue
	return result_queue

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
	pass

def run_master():
	#把两个Queue注册到网络上，callable参数关联了两个Queue对象
	QueueManager.register('get_task_queue', callable = func_task_queue)
	QueueManager.register('get_result_queue', callable = func_result_queue)
	
	#绑定端口，设置auth key
	port = 5000
	auth_key = b'llwf'
	#manager = QueueManager(address = ('', port), authkey = auth_key)
	# windows需要写ip地址
	manager = QueueManager(address = ('127.0.0.1', port), authkey = auth_key)
	#启动Queue
	manager.start()
	
	#获得通过网络访问的Queue对象
	task = manager.get_task_queue()
	result = manager.get_result_queue()
	#添加任务到队列
	for i in range(10):
		n = random.randint(0, 10000)
		print('Put task %s' % n)
		task.put(n)
		
	#从result队列读取结果
	print('Try get results from distri worker process...')
	for i in range(10):
		try:
			r = result.get(timeout = 10)
			print('Result: %s' % r)
		except queue.Empty:
			print('Task Queue is empty.')
		
	#关闭manager
	manager.shutdown()
	print('Master exit.')
	
if __name__ == '__main__':
	freeze_support()
	run_master()
