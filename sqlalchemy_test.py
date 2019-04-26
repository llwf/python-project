#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#创建数据库表的命令，关联两个数据库表
'''
create table student
(
id varchar(20),
name varchar(20),
PRIMARY KEY (id)	
);

create table book1
(
id varchar(20),
name varchar(20),
user_id varchar(20),
FOREIGN KEY (user_id) REFERENCES student(id)
);
'''

Base = declarative_base()

class Student(Base):
	#表的名字
	__tablename__ = 'student'
	#表的数据结构
	id = Column(String(20), primary_key=True)
	name = Column(String(20))
	books = relationship('Book')

class Book(Base):
	__tablename__ = 'book1'
	id = Column(String(20), primary_key=True)
	name = Column(String(20))
	user_id = Column(String(20), ForeignKey('student.id'))

#数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')

DBSession = sessionmaker(bind=engine)

session = DBSession()
new_student = Student(id='5', name='Bob')
session.add(new_student)
new_book = Book(id='122', name='Hello World!', user_id='5')
session.add(new_book) 
session.commit()
session.close()

session = DBSession()
student = session.query(Student).filter(Student.id=='5').one()
print('type:', type(student))
print('name:', student.name)
print(student.books)
for book in student.books:
	print('book id %s name %s' % (book.id, book.name))

session.close()