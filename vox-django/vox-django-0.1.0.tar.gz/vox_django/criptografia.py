from base64 import b64encode, b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

BS = 16
key = bytearray([45, 42, 45, 66, 45, 73, 76, 68, 67, 42, 79, 68, 69, 45, 45, 45])
cipher = AES.new(key, AES.MODE_ECB)


def encrypt_aes(message):
    return b64encode(cipher.encrypt(pad(message.encode(), 16))).decode('utf8')


def decrypt_aes(encoded):
    data = cipher.decrypt(b64decode(encoded))

    return unpad(data, 16).decode('utf8')
