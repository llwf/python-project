#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in  python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use md5 in  python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def cal_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()
	
def login(user, password):
	if user in db and cal_md5(password) == db[user]:
		return True
	else:
		return False

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

import random

class User(object):
	def __init__(self, username, password):
		self.username = username
		self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
		self.password = cal_md5(password + self.salt + self.username)
		print(self.password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
	if username in db:
		user = db[username]
		return user.password == cal_md5(password + user.salt + user.username)
	else:
		return False

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

import hmac

def hmac_md5(key, s):
	return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
	def __init__(self, username, password):
		self.username = username
		self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
		self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
	if username in db:
		user = db[username]
		return user.password == hmac_md5(user.key, password)
	else:
		return False
		
# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


