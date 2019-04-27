#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Description:web crawler"""

from idna import unicode
import requests
from bs4 import BeautifulSoup
import lxml
import json
import mysql.connector

__author__ = 'Carlos Leo'


id = 0

# 获取网页返回信息
def get_response(page):
    resp = requests.get('https://book.douban.com/top250', params={'start': str(page * 25)})
    if resp.status_code == 200:
        return resp.text
    else:
        raise RecursionError('fail to request to target.')


# 使用BeautifulSoup解析
def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find('div', id='wrapper').find_all('table')
    for table in tables:
        img = table.find('img')['src']
        name = table.select('.pl2')[0].a['title']
        string = unicode(table.find('p').string)
        lst = string.split(' / ')
        author = lst[0].strip()
        publisher = lst[-3].strip()
        date = lst[-2].strip()
        price = lst[-1].strip()
        credit = unicode(table.select('.rating_nums')[0].string)
        try:
            desc = unicode(table.select('.inq')[0].string)
        except IndexError:
            desc = '无'
        global id
        id += 1
        yield {
            'id': id,
            'img': img,
            'name': name,
            'author': author,
            'publisher': publisher,
            'date': date,
            'price': price,
            'credit': float(credit),
            'desc': desc
        }


# 写入文件
# def write_to_file():
#     with open('books.txt', 'w') as f:
#         for i in range(10):
#             for book in parse_html(get_response(i)):
#                 json.dump(book, f, ensure_ascii=False)
#                 f.write('\n')
#                 print(book, 'was saved into book.txt')


# 存入数据库
def save():
    for i in range(10):
        for book in parse_html(get_response(i)):
            save_to_db(book['id'], book['img'], book['name'], book['author'], book['publisher'], book['date'],
                       book['price'], book['credit'], book['desc'])
            print('save book' + str(book) + 'to db')


# 存入一本书到数据库
def save_to_db(*args):
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    cursor.execute('insert into book(id, img, name, author, publisher, date, price, credit, description) '
                   'values(%s, %s, %s, %s, %s, %s, %s, %s, %s)', args)
    conn.commit()
    cursor.close()
    conn.close()



if __name__ == '__main__':
    save()