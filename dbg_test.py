#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import logging
import pdb
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
pdb.set_trace()
print(10 / n)