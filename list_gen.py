#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import os

print(x*x for x in range(20, 30))
print([d for d in os.listdir('.')])

d = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
print([k + '=' + v for k, v in d.items()])

brands = ['Apple', 'Baidu', 'Ck', 'Dior', 1566, 556.255]
print([brand.lower() for brand in brands if isinstance(brand, str)])
print([brand.upper() for brand in brands if isinstance(brand, str)])