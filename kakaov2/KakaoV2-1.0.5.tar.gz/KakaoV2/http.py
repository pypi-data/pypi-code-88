import aiohttp, json, asyncio, ssl, socket, struct
from bson import encode
from .channel import Channel
from .message import Message
from .error import AuthException, PasscodeException
from .utils import get_xvc, getBookingData, getCheckInData, Packet, CryptoManager, Writer
class HTTP:
    def __init__(self, client, device_uuid):
        self.__session_key = ""
        self.__device_uuid = device_uuid
        self.__session = aiohttp.ClientSession(trust_env = True)
        self.reader, self.writer = None, None
        self.__writer = None
        self.__crypto = CryptoManager()
        self.packetDict = {}
        self.__processingHeader = b""
        self.__processingBuffer = b""
        self.client = client
        self.__processingSize = 0
        self.loop = asyncio.get_event_loop()
        return 
    def __get_booking_data(self):
        hostname = "booking-loco.kakao.com"
        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                data = encode({"os": "win32", "model": "", "MCCMNC": ""})

                b = Packet(1000, 0, "GETCONF", 0, data)
                ssock.write(b.toLocoPacket())

                data = ssock.recv(4096)

                recvPacket = Packet()
                recvPacket.readLocoPacket(data)
                return recvPacket

    def __get_checkin_data(self, host: str, port: int):
        crypto = CryptoManager()
        sock = socket.socket()
        sock.connect((host, port))

        handshakePacket = crypto.getHandshakePacket()
        sock.send(handshakePacket)

        p = Packet(
            1,
            0,
            "CHECKIN",
            0,
            encode(
                {
                    "userId": 0,
                    "os": 'win32',
                    "ntype": 0,
                    "appVer": '3.2.6',
                    "MCCMNC": "999",
                    "lang": "ko",
                }
            ),
        )

        sock.send(p.toEncryptedLocoPacket(crypto))

        data = sock.recv(2048)

        recvPacket = Packet()
        recvPacket.readEncryptedLocoPacket(data, crypto)

        return recvPacket
    async def try_passcode(self, email, password, passcode):
        headers = {}
        headers["User-Agent"] = "KT/3.2.6 Wd/10.0 ko"
        headers["A"] = "win32/3.2.6/kr"
        headers["X-VC"] = get_xvc(email, self.__device_uuid)
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = {}
        data["email"] = email
        data["password"] = password
        data["device_name"] = 'KakaoV2'
        data["device_uuid"] = self.__device_uuid
        data["os_version"] = "10.0"
        data["passcode"] = passcode
        data["permanent"] = True
        data["once"] = False
        result = await self.url_open_json("https://katalk.kakao.com/win32/account/register_device.json", data=data, headers=headers)
        if result["status"] == 0:
            return result
        else:
            raise PasscodeException
    async def request_passcode(self, email, password):
        headers = {}
        headers["User-Agent"] = "KT/3.2.6 Wd/10.0 ko"
        headers["A"] = "win32/3.2.6/kr"
        headers["X-VC"] = get_xvc(email, self.__device_uuid)
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = {}
        data["email"] = email
        data["password"] = password
        data["device_name"] = 'KakaoV2'
        data["device_uuid"] = self.__device_uuid
        data["os_version"] = "10.0"
        data["permanent"] = True
        data["once"] = False
        result = await self.url_open_json("https://katalk.kakao.com/win32/account/request_passcode.json", data=data, headers=headers)
        if result["status"] == 0:
            return result
        else:
            raise PasscodeException
    async def upload(self, data, dataType, userId):
        path = ""
        async with aiohttp.ClientSession() as session:
            async with session.post("https://up-m.talk.kakao.com/upload", 
                headers={
                    "A": "win32/3.2.6/kr",
                },
                data={
                    "attachment_type": dataType,
                    "user_id": userId,
                },
                files={
                    "attachment": data,
                },) as resp:
                path = (await resp.content()).decode()

        key = path.replace("/talkm", "")
        url = "https://dn-m.talk.kakao.com" + path

        return path, key, url

    async def login(self, email, password):
        headers = {}
        headers["User-Agent"] = "KT/3.2.6 Wd/10.0 ko"
        headers["A"] = "win32/3.2.6/kr"
        headers["X-VC"] = get_xvc(email, self.__device_uuid)
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = {}
        data["email"] = email
        data["password"] = password
        data["device_name"] = 'KakaoV2'
        data["device_uuid"] = self.__device_uuid
        data["os_version"] = "10.0"
        # data["permanent"] = True
        data["forced"] = True
        result = await self.url_open_json('https://katalk.kakao.com/win32/account/login.json', data=data, headers=headers)
        if result["status"] == -100:
            raise AuthException
        if result["status"] == 0:
            self.__session_key = result["access_token"]
            self.__user_id = result["userId"]
            return self.__session_key, self.__user_id
        else:
            raise AuthException
    async def url_open_json(self, url, data=None, headers={}):
        headers["User-Agent"] = "KT/3.2.6 Wd/10.0 ko"
        headers["A"] = "win32/3.2.6/kr"
        headers["S"] = self.__session_key + "-" + self.__device_uuid
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        result = None
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=None if not data else data, headers=headers) as resp:
                result = json.loads(await resp.text())
        return result
    async def url_open(self, url, data=None, headers={}):
        headers["User-Agent"] = "KT/3.2.6 Wd/10.0 ko"
        headers["A"] = "win32/3.2.6/kr"
        headers["S"] = self.__session_key + "-" + self.__device_uuid
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        result = None
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=None if not data else data, headers=headers) as resp:
                result = await resp.text()
        return result
    async def heartbeat(self):
        while True:
            await asyncio.sleep(180)
            PingPacket = Packet(0, 0, "PING", 0, encode({}))
            self.loop.create_task(self.__writer.sendPacket(PingPacket))
    async def __processingPacket(self, encryptedPacket):
        encLen = encryptedPacket[0:4]
        IV = encryptedPacket[4:20]
        BODY = encryptedPacket[20:]

        self.__processingBuffer += self.__crypto.aesDecrypt(BODY, IV)

        if not self.__processingHeader and len(self.__processingBuffer) >= 22:
            self.__processingHeader = self.__processingBuffer[0:22]
            self.__processingSize = (
                struct.unpack("<i", self.__processingHeader[18:22])[0] + 22
            )

        if self.__processingHeader:
            if len(self.__processingBuffer) >= self.__processingSize:
                p = Packet()
                p.readLocoPacket(self.__processingBuffer[: self.__processingSize])

                self.loop.create_task(self.__onPacket(p))

                self.__processingBuffer = self.__processingBuffer[
                    self.__processingSize :
                ]
                self.__processingHeader = b""
    async def __onPacket(self, packet):
        if packet.PacketID in self.packetDict:
            self.packetDict[packet.PacketID].set_result(packet)
            del self.packetDict[packet.PacketID]
        body = packet.toJsonBody()

        if packet.PacketName == "MSG":
            chatId = body["chatLog"]["chatId"]
            if "li" in body: li = body["li"]
            else: li = 0
            channel = Channel(chatId, li, self.__writer)
            msg = Message(self, channel, body)
            self.loop.create_task(self.client.on_message(msg))

        if packet.PacketName == "NEWMEM":
            chatId = body["chatLog"]["chatId"]
            if "li" in body: li = body["li"]
            else: li = 0

            channel = Channel(chatId, li, self.__writer)
            self.loop.create_task(self.client.on_join(channel))

        if packet.PacketName == "DELMEM":
            chatId = body["chatLog"]["chatId"]
            if "li" in body: li = body["li"]
            else: li = 0

            channel = Channel(chatId, li, self.__writer)
            # channel = packet.toJsonBody()
            self.loop.create_task(self.client.on_quit( channel))

        if packet.PacketName == "DECUNREAD":
            chatId = body["chatId"]
            channel = Channel(chatId, 0, self.__writer)
            self.loop.create_task(self.client.on_read(channel))
    async def receive_packet(self):
        encryptedBuffer = b""
        currentPacketSize = 0
        while True:
            recv = await self.reader.read(256)
            if not recv:
                self.loop.stop()
                break

            encryptedBuffer += recv

            if not currentPacketSize and len(encryptedBuffer) >= 4:
                currentPacketSize = struct.unpack("<I", encryptedBuffer[0:4])[0]

            if currentPacketSize:
                encryptedPacketSize = currentPacketSize + 4

                if len(encryptedBuffer) >= encryptedPacketSize:
                    self.loop.create_task(
                        self.__processingPacket(encryptedBuffer[0:encryptedPacketSize])
                    )
                    encryptedBuffer = encryptedBuffer[encryptedPacketSize:]
                    currentPacketSize = 0

    async def get_address(self, host, port):
        checkinObj = self.__get_checkin_data(host, port).toJsonBody()
        port = checkinObj["port"]
        address = checkinObj["host"]
        return address, port
    async def get_ticket_address(self):
        
        bookingObj = self.__get_booking_data().toJsonBody()
        port = bookingObj["wifi"]["ports"][0]
        address = bookingObj["ticket"]["lsl"][0]
        return address, port

    async def open_socket(self, host, port):
        self.reader, self.writer = await asyncio.open_connection(host, port)
        self.__writer = Writer(self.__crypto, self.writer, self.packetDict)
        
        LoginListPacket = Packet(
            0,
            0,
            "LOGINLIST",
            0,
            encode(
                {
                    "appVer": "3.2.7",
                    "prtVer": "1",
                    "os": "win32",
                    "lang": "ko",
                    "duuid": self.__device_uuid,
                    "oauthToken": self.__session_key,
                    "dtype": 1,
                    "ntype": 0,
                    "MCCMNC": "999",
                    "revision": 0,
                    "chatIds": [],
                    "maxIds": [],
                    "lastTokenId": 0,
                    "lbk": 0,
                    "bg": False,
                }
            ),
        )
        self.writer.write(self.__crypto.getHandshakePacket())

        self.loop.create_task(self.__writer.sendPacket(LoginListPacket))
        return self.reader, self.__writer