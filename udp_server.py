#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 9999))
print('Bind UDP on port 9999...')

while True:
	data, addr = s.recvfrom(1024)
	print('Recvied from %s:%s.' % addr)
	s.sendto(b'Hello, %s!' % data, addr)