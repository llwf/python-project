#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x, ',', p.y)

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(4, 8, 3)
print(c)

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('A')
print(q)
q.popleft()
print(q)

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'ABC'
print(dd['key1'])
print(dd['key2'])

from collections import OrderedDict

d = dict([('a', 1), ('c', 3), ('b', 2)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity
	
	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last = False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitem__(self, key, value)

fifo = LastUpdatedOrderedDict(4)
print(fifo)
fifo['A'] = 'a'
fifo['B'] = 'b'
fifo['C'] = 'c'
fifo['D'] = 'd'
print(fifo) 
fifo['E'] = 'e'
print(fifo)
fifo['C'] = 'c'
print(fifo)

from collections import ChainMap
import os, argparse

defaults = {
	'color': 'red',
	'user': 'guest'
}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

combined = ChainMap(command_line_args, os.environ, defaults)

print('color = %s' % combined['color'])
print('user = %s' % combined['user'])

from collections import Counter
c = Counter('programming')
print(c)












