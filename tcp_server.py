#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import socket, threading, time

def tcpLink(sock, addr):
	#addr 是一个包含IP和Port的tuple，所以格式化字符串需要使用%s %s
	print('Accept a new connection from %s:%s...' % addr)
	
	sock.send(('Welcome %s:%s' % addr).encode('utf-8'))
	while True:
		data = sock.recv(1024)
#		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9999))
s.listen(10)
print('Waiting for connection...')

while True:
	sock, addr = s.accept()
	t = threading.Thread(target = tcpLink, args = (sock, addr))
	t.start()
	