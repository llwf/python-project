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