#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
import asyncio
from aiohttp import web

async def index(requset):
	await asyncio.sleep(0.5)
	return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(requset):
	await asyncio.sleep(0.5)
	text = '<h1>hello, %s!</h1>' % requset.match_info['name']
	return web.Response(body=text.encode('utf-8'), content_type='tx')

async def init(loop):	
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	app.router.add_route('GET', '/hello/{name}', hello)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
	print('Server started at http://127.0.0.1:8000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
'''

import asyncio
from aiohttp import web

async def index(requset):
	await asyncio.sleep(0.5)
	return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(requset):
	await asyncio.sleep(0.5)
	text = '<h1>hello, %s!</h1>' % requset.match_info['name']
	return web.Response(body=text.encode('utf-8'), content_type='tx')
	
app = web.Application()
app.add_routes([web.get('/', index), web.get('/hello/{name}', hello)])
web.run_app(app, host='127.0.0.1', port=8000)
