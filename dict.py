#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

d = {'liulian': 123, "zhangsan": 333, 'hahah': 445}
print(d,"\nddd")
print(d['liulian'])
print('Thomas' in d)
print(d.get('liulian'))
print(d.get('Thomas', 'Not in'))
#print(d.pop())
print(d.pop('liulian'))
print(d,"\nddd")

t = (1,2,3)
mt = (1, 4)

s1 = set(t)
print(s1)
s2 = set(mt)
print(s2)