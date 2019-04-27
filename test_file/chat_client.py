#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Ada', b'Bob', b'Clair', b'Danly']:
	s.sendto(data, ('127.0.0.1', 9999))
	print(s.recv(1024).decode('utf-8'))
s.close()
