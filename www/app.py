import logging; logging.basicConfig(level=logging.INFO)
'''logging模块是Python内置的标准模块，主要用于输出运行日志，
可以设置输出日志的等级、日志保存路径、日志文件回滚等'''
import asyncio, os, json, time
'''asyncio，异步IO；os，系统接口；json，json 编码解码模块；
time，系统时间模块；datetime，日期模块'''
from datetime import datetime

from aiohttp import web
'''aiohttp，异步 Web 开发框架；jinja2，前端模板引擎；
aiomysql，异步 mysql 数据库驱动'''

def index(request):
	return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    logging.info('server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()