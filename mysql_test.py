#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import mysql.connector
try:
	conn = mysql.connector.connect(user='root', password='password', database='test')
	cursor = conn.cursor()
	cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
	cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Sunmonday'])
	conn.commit()
finally:
	cursor.close()
	conn.close()

try:
	conn = mysql.connector.connect(user='root', password='password', database='test')
	cursor = conn.cursor()
	cursor.execute('select * from user where id=%s', ('1',))
	values = cursor.fetchall()
	print(values)
finally:
	cursor.close()
	conn.close()