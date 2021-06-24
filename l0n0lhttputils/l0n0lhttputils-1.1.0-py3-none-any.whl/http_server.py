# -*- coding:UTF-8 -*-
# 作者: l0n0l
# 时间: 2020/09/22 周二
# 点: 18:00:25

# 描述:异步 http 服务器
from aiohttp import web
import asyncio

class http_server:
    def __init__(self, host: str, port: int, loop: asyncio.AbstractEventLoop = None):
        self.host = host
        self.port = port
        self.loop = loop or asyncio.get_event_loop()

        self.app = web.Application(loop=self.loop)
        self.router = self.app.router
        self.add_route = self.app.router.add_route
        self.add_routes = self.app.router.add_routes
        self.add_static = self.app.router.add_static

    async def __start(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        self.site = web.TCPSite(runner, host=self.host, port=self.port)
        await self.site.start()

    async def __close(self):
        await self.site.stop()

    def __default_cos_header(self):
        """
        返回默认跨站header
        """
        return {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Headers": "*"
        }

    def start(self, loop: asyncio.AbstractEventLoop = None):
        if loop is None:
            loop = asyncio.get_event_loop()
        loop.create_task(self.__start())

    def close(self, loop):
        if loop is None:
            loop = asyncio.get_event_loop()
        loop.create_task(self.__close())

    def route(self, method, path, option_headers=None):
        """装饰器,将异步函数装饰为访问route.
        @method: str : (get|post|put|delete|option)\n
        @path: str : "/a" "/{prefix}/a" "/a/b/c"\n
        @option_headers: (True | http header:dict) 会自动添加一个option方法的回调。
            如果option_header=True 会自动添加 __default_cos_header 函数返回的默认跨站 option 方法。
            如果option_header={"header":value},会将dict中的header作为 option 方法返回的header\n
        例如：
        ```
        server = http_server(host,port)
        #1 添加 /test 路径
        @server.route("get", "/test")
        async def test_route(req)
            pass
        #2 添加 /任意值/test 路径，对于nginx反向代理很有用
        @server.route("get", "/{prefix}/test")
        async def test_route(req)
            pass

        #3 添加 默认的跨站option方法
        @server.route("get", "/{prefix}/test", server.__default_cos_header())
        async def test_route(req)
            pass

        #4 添加 默认的跨站option方法
        @server.route("get", "/{prefix}/test", True)
        async def test_route(req)
            pass
        ```
        例3 和 例4 是等价的
        """
        def f(func):
            oh = option_headers
            self.add_route(method, path, func)
            if oh is not None:
                if isinstance(oh, bool) and oh == True:
                    oh = self.__default_cos_header()

                async def option_handler(request: web.Request):
                    return web.Response(headers=oh)

                self.app.router.add_options(path, option_handler)
            return func
        return f
