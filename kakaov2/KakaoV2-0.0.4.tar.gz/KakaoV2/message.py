import json


import hashlib
import requests


class Message:
    def __init__(self, http, channel, body):
        self.__http = http
        self.__body = body
        self.channel = channel
        self.logId = self.__body["chatLog"]["logId"]
        self.type = self.__body["chatLog"]["type"]
        self.content = self.__body["chatLog"]["message"]
        self.id = self.__body["chatLog"]["msgId"]
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
                    "src_logId": self.logId,
                    "src_mentions": [],
                    "src_message": self.message,
                    "src_type": self.type,
                    "src_userId": self.author,
                }
            ),
            26,
        )

    async def send(self, msg):
        return await self.channel.send(msg)

    async def read(self):
        return await self.channel.notiRead(self.logId)

    async def delete(self):
        return await self.channel.deleteMessage(self.logId)

    # async def hide(self):
    #     return await self.channel.hideMessage(self.logId, self.type)

    async def kick(self):
        return await self.channel.kickMember(self.authorId)

    async def __sendPhoto(self, data, w, h):
        path, key, url = await self.__http.upload(data, "image/jpeg", self.authorId)
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
                    "mt": "image/jpeg",
                }
            ),
            2,
        )

    async def send_image_path(self, path, w, h):
        with open(path, "rb") as f:
            data = f.read()

        return await self.__sendPhoto(data, w, h)

    async def send_image_url(self, url, w, h):
        r = requests.get(url)
        r.raise_for_status()

        return await self.__sendPhoto(r.content, w, h)
