#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import functools

int2 = functools.partial(int, base=2)

print(int2('10001001110001111101'))

max2 = functools.partial(max, 10)

print(max2(3, 9))