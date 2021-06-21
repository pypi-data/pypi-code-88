import hashlib, io, os, socket
from bson import BSON, decode_all, decode, encode
import struct, ssl, asyncio
from binascii import hexlify, unhexlify
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.Hash import SHA1
from Cryptodome.PublicKey.RSA import construct
from Cryptodome.Signature import pss





class Packet:
    def __init__(self, PacketID=0, StatusCode=0, PacketName="", BodyType=0, Body=b""):
        self.PacketID = PacketID
        self.StatusCode = StatusCode
        self.PacketName = PacketName
        self.BodyType = BodyType
        self.Body = Body
    def toLocoPacket(self):
        f = io.BytesIO()
        f.write(struct.pack("<I", self.PacketID))
        f.write(struct.pack("<H", self.StatusCode))

        if (11 - len(self.PacketName)) < 0:
            raise Exception("invalid packetName")

        f.write(self.PacketName.encode("utf-8"))

        f.write(b"\x00" * (11 - len(self.PacketName)))
        f.write(struct.pack("<b", self.BodyType))
        f.write(struct.pack("<i", len(self.Body)))

        f.write(self.Body)
        return f.getvalue()
    def readLocoPacket(self, packet):
        self.PacketID = struct.unpack("<I", packet[:4])[0]
        self.StatusCode = struct.unpack("<H", packet[4:6])[0]
        self.PacketName = packet[6:17].decode().replace("\0", "")
        self.BodyType = struct.unpack("<b", packet[17:18])[0]
        self.BodySize = struct.unpack("<i", packet[18:22])[0]
        self.Body = packet[22:]

    def toEncryptedLocoPacket(self, crypto):
        iv = os.urandom(16)
        encrypted_packet = crypto.aesEncrypt(self.toLocoPacket(), iv)

        f = io.BytesIO()
        f.write(struct.pack("<I", len(encrypted_packet) + len(iv)))
        f.write(iv)
        f.write(encrypted_packet)

        return f.getvalue()
    def readEncryptedLocoPacket(self, packet, crypto):
        packetLen = struct.unpack(">I", packet[0:4])[0]
        iv = packet[4:20]
        data = packet[20 : packetLen - 16]

        dec = crypto.aesDecrypt(data, iv)

        try:
            self.readLocoPacket(dec)
        except Exception as e:
            print(str(e))
    def toJsonBody(self):
        return decode(self.Body)


class Writer:
    def __init__(self, crypto, StreamWriter, PacketDict):
        self.crypto = crypto
        self.StreamWriter = StreamWriter
        self.PacketID = 0
        self.PacketDict = PacketDict

    def __getPacketID(self):
        self.PacketID += 1
        return self.PacketID

    async def sendPacket(self, packet):
        pid = self.__getPacketID()

        fut = asyncio.get_event_loop().create_future()
        self.PacketDict[pid] = fut

        packet.PacketID = pid
        self.StreamWriter.write(packet.toEncryptedLocoPacket(self.crypto))
        await self.StreamWriter.drain()

        return await fut

class CryptoManager:
    def __init__(self):
        self.aes_key = os.urandom(16)

    def getRsaPublicKey(self):
        n = int(
            "A44960441C7E83BB27898156ECB13C8AFAF05D284A4D1155F255CD22D3176CDE50482F2F27F71348E4D2EB5F57BF9671EF15C9224E042B1B567AC1066E06691143F6C50F88787F68CF42716B210CBEF0F59D53405A0A56138A6872212802BB0AEEA6376305DBD428831E8F61A232EFEDD8DBA377305EF972321E1352B5F64630993E5549C64FCB563CDC97DA2124B925DDEA12ADFD00138910F66937FAB68486AE43BFE203C4A617F9F232B5458A9AB409BAC8EDADEF685545F9B013986747737B3FD76A9BAC121516226981EA67225577D15D0F082B8207EAF7CDCB13123937CB12145837648C2F3A65018162315E77EAD2D2DD5986E46251764A43B9BA8F79",
            16,
        )
        e = int("3", 16)

        rsa_key = construct((n, e))
        return rsa_key

    def getHandshakePacket(self):
        f = io.BytesIO()

        enced = self.rsaEncrypt(self.aes_key)
        f.write(struct.pack("<I", len(enced)))
        f.write(struct.pack("<I", 12))
        f.write(struct.pack("<I", 2))
        f.write(enced)

        return f.getvalue()

    def rsaEncrypt(self, data):
        rsa_key = self.getRsaPublicKey()
        rsa_chiper = PKCS1_OAEP.new(
            key=rsa_key, hashAlgo=SHA1, mgfunc=lambda x, y: pss.MGF1(x, y, SHA1)
        )

        return rsa_chiper.encrypt(data)

    def aesEncrypt(self, data, iv):
        aes_chiper = AES.new(self.aes_key, AES.MODE_CFB, iv, segment_size=128)
        return aes_chiper.encrypt(data)

    def aesDecrypt(self, data, iv):
        aes_chiper = AES.new(self.aes_key, AES.MODE_CFB, iv, segment_size=128)
        return aes_chiper.decrypt(data)







def get_xvc(email, device_uuid):
    source = f"JAYDEN|KT/3.2.3 Wd/10.0 ko|JAYMOND|{email}|{device_uuid}"
    return hashlib.sha512(source.encode()).hexdigest()


