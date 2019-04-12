#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

import pickle, json

d = dict(name='Bob', age = 21, score = 95)
pickle.dumps(d)

with open('dump.txt', 'wb') as f:
	pickle.dump(d, f)
	
with open('dump.txt', 'rb') as f:
	print(pickle.load(f))
		
l = ['A', 'B', 123, 563.235, True, None, {'Bert': 33, 'Lisa': 25}, (0, 1, 2)]		
with open('dump.json', 'w') as f:
	json.dump(l, f)

with open('dump.json', 'r') as f:
	print(json.load(f))
	
class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score,
	}
def dict2student(d):
	return Student(d['name'], d['age'], d['score'])
	
s = Student('Bert', 23, 89.5)
print(json.dumps(s, default=student2dict))
with open('student.json', 'w') as f:
	json.dump(s, f, default=student2dict)

with open('student2.json', 'w') as f:
	json.dump(s, f, default=lambda s: s.__dict__)

with open('student.json', 'r') as f:
	new_student = json.load(f, object_hook=dict2student)
print(new_student)
print(new_student.name, new_student.age, new_student.score)

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
s = json.dumps(obj, ensure_ascii=False)	
print(s)
help(json.dumps)	