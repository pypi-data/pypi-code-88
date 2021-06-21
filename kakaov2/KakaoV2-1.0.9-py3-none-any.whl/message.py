import json
import hashlib
import requests
from .utils import File

class Message:
    def __init__(self, http, channel, body):
        self.__http = http
        self.__body = body
        self.channel = channel
        self.id = self.__body["chatLog"]["logId"]
        self.type = self.__body["chatLog"]["type"]
        self.content = self.__body["chatLog"]["message"]
        # self.id = self.__body["chatLog"]["msgId"]
        self.author = self.__body["chatLog"]["authorId"]

        try:
            if "attachment" in self.__body["chatLog"]:
                self.attachment = json.loads(self.__body["chatLog"]["attachment"])
            else:
                self.attachment = {}
        except:
            pass

        self.nickName = self.author

    def __repr__(self):
        return "<Message id={0.id} channel={0.channel!r} type={0.type!r} author={0.author!r}>".format(self)

    async def reply(self, msg, t=1):
        return await self.channel.sendChat(
            msg,
            json.dumps(
                {
                    "attach_only": False,
                    "attach_type": t,
                    "mentions": [],
                    "src_linkId": self.channel.li,
                    "src_logId": self.id,
                    "src_mentions": [],
                    "src_message": self.content,
                    "src_type": self.type,
                    "src_userId": self.author,
                }
            ),
            26,
        )

    async def send(self, msg):
        return await self.channel.send(msg)

    async def read(self):
        return await self.channel.notiRead(self.id)

    async def delete(self):
        return await self.channel.deleteMessage(self.id)

    # async def hide(self):
    #     return await self.channel.hideMessage(self.logId, self.type)

    async def kick(self):
        return await self.channel.kickMember(self.author)

    async def __sendFile(self, data, w, h, datatype):
        path, key, url = await self.__http.upload(data, "image/jpeg", self.author)
        return await self.channel.forwardChat(
            "",
            json.dumps(
                {
                    "thumbnailUrl": url,
                    "thumbnailHeight": w,
                    "thumbnailWidth": h,
                    "url": url,
                    "k": key,
                    "cs": hashlib.sha1(data).hexdigest().upper(),
                    "s": len(data),
                    "w": w,
                    "h": h,
                    "mt": datatype,
                }
            ),
            2,
        )

    async def send_file(self, _file, w, h):
        if not isinstance(_file, File):
            raise TypeError
        with open(_file.path, "rb") as f:
            data = f.read()

        return await self.__sendFile(data, w, h, _file.datatype)
