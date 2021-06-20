import time
from .utils import Packet
import bson


class Channel:
    def __init__(self, chatId, li, writer):
        self.li = li
        self.writer = writer
        self.id = chatId

    async def __sendPacket(self, command, data):
        packet = Packet(0, 0, command, 0, bson.encode(data))
        return (await self.writer.sendPacket(packet)).toJsonBody()

    async def sendChat(self, msg, extra, t):
        data = {
            "chatId": self.id,
            "extra": extra,
            "type": t,
            "msgId": time.time(),
            "msg": str(msg),
            "noSeen": False,
        }
        return await self.__sendPacket("WRITE", data)

    async def send(self, msg):
        return await self.sendChat(msg, "{}", 1)


    async def kick(self, member_id):
        if self.li:
            data = {
                "li": self.li,
                "c": self.id,
                "mid": member_id,
            }
            await self.__sendPacket("KICKMEM", data)

    # async def get_linkinfo(self):
    #     return await self.__sendPacket("INFOLINK", {"lis": [self.li]})

    async def get_info(self):
        return await self.__sendPacket("CHATINFO", {"chatId": self.id})

    async def get_user(self, userId):
        return await self.__sendPacket( "MEMBER", {"chatId": self.id, "memberIds": [userId]} )
