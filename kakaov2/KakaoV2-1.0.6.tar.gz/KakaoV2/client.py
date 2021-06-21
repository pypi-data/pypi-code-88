from .utils import get_xvc, Packet
from .http import HTTP
from .error import AuthException
from bson import encode

import asyncio, aiohttp

class Client:
    def __init__(self, device_uuid=None):
        self.__device_uuid = device_uuid
        self.__session_key = ""
        self.user_id = ""
        self.loop = asyncio.get_event_loop()
        self.lock = asyncio.Lock()   
        self.http = HTTP(self, device_uuid)
        
    def run(self, email, password):
        self.loop.create_task(self.__start(email, password))
        self.loop.run_forever()

    def event(self, coro):
        setattr(self, coro.__name__, coro)

    async def on_ready(self):
        pass
    async def on_message(self, msg):
        pass
    async def on_join(self, channel):
        pass
    async def on_quit(self, channel):
        pass
    async def on_read(self, channel):
        pass

    async def __start(self, email, password):
        self.__session_key, self.user_id = await self.http.login(email, password)
        address, port = await self.http.get_ticket_address()
        while True:
            try:
                address, port = await self.http.get_address(address, int(port))
                break
            except:
                continue
        await self.http.open_socket(address, int(port))
        self.loop.create_task(self.http.receive_packet())
        self.loop.create_task(self.http.heartbeat())
        self.loop.create_task(self.on_ready())
        
        



