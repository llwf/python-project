#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import re
m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-123343')
print('%s  %s  %s' % (m.group(0), m.group(1), m.group(2)))

t1 = '19:05:30'
t2 = '23:5:9'
time_regular = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$'
m = re.match(time_regular, t1)
print(m.groups())
m = re.match(time_regular, t2)
print(m.groups())

print('++++++++++++++++')

def is_valid_email(addr):
	email_regular = r'^\w+(\.\w+|w*)@\w+\.\w+$'
	m = re.match(email_regular, addr)
	if m:
		return True
	else:
		return False
# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')	

def name_of_email(addr):
	email_regular = r'^(\<(\w+(\s*|\.?)\w+)\>)?\s*(\w+(\.\w+|w*))\@\w+\.\w+$'
	m = re.match(email_regular, addr)
	if m:
		print(m.groups())
		if m.group(2):
			return m.group(2)
		elif m.group(4):
			return m.group(4)
		else:
			return None
	else:
		return None

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
assert name_of_email('<TimCook>cook@apple.com') == 'TimCook'
assert name_of_email('<Bill.Gate> bill@microsoft.com') == 'Bill.Gate'
assert name_of_email('<Tom Paris>@voyager.org') == None
assert name_of_email('Tom Paris> tom@voyager.org') == None
assert name_of_email('bill.gates.andy@microsoft.com') == None
assert name_of_email('<bill.gates@microsoft.com') == None
print('ok')	
		