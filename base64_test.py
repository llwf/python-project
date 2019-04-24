#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

'''base64 encode/decode test'''
import base64

def safe_base64_decode(code):
    '''自动补齐并解码'''
    while len(code) % 4 != 0:
        code = code + b'='
    return base64.b64decode(code)



# 测试:
assert safe_base64_decode(b'YWJjZA==') == b'abcd'
assert safe_base64_decode(b'YWJjZA') == b'abcd'
print('ok')
