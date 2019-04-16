#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])	
print('Exit code:', r)	
print('+++++++++++++++++++++++++++')	
print('$ nslookup')
sp = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output, err = sp.communicate(b'set q=mx\npython.org\nexit\n')	
#print(output.decode('utf-8'))
print('Exit code:', sp.returncode)		

	
	
	