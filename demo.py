# import logging
# logging.basicConfig(level=logging.INFO)


# import asyncio,os,json,time

# from datetime import datetime


# from aiohttp import web


# def index(request):
#     return web.Response(body=b'<h1>sunshuai</h1>',content_type='text/html')
	


# @asyncio.coroutine
# def init(loop):
# 	app=web.Application(loop=loop)
# 	app.router.add_route('GET','/',index)
# 	srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
# 	logging.info('server started at http://127.0.0.1:9000....')
# 	return srv


# loop=asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()



import orm
from models import User,Blog,Comment
import logging 
logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time

async def test(loop):
	await orm.create_pool(loop=loop,user='root',password='root',db='db')
	u= User(name='Test',email='test@example.com',passwd='113231231')
	logging.info(u,'user')
	await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

