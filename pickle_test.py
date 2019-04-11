#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import pickle

d = dict(name='Bob', age = 21, score = 95)
pickle.dumps(d)

with open('dump.txt', 'wb') as f
	pickle.dump(d, f)