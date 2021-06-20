import base64
import logging

from Crypto.Cipher import AES


class CryptoAES(object):
    def __init__(self, key: str):
        key = base64.b64decode(key)
        if len(key) > 32:
            key = key[:32]
        else:
            key = key[:(len(key) // AES.block_size) * AES.block_size]
        self.key = key

    def encrypt(self, data) -> str:
        str_data = data if isinstance(data, str) else str(data)
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(bytes(str_data, encoding='utf-8'))
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode(encoding='utf-8')

    def decrypt(self, enc_data: str) -> str:
        if enc_data is None:
            return ""
        if len(enc_data) <= 32:
            return enc_data

        enc_bytes = base64.b64decode(enc_data)
        iv, tag, raw = enc_bytes[:16], enc_bytes[16:32], enc_bytes[32:]
        try:
            cipher = AES.new(self.key, AES.MODE_EAX, iv)
            return cipher.decrypt_and_verify(raw, tag).decode('utf-8')
        except UnicodeDecodeError as e:
            logging.warn("decrypt enc_data decode error:%s" % e)
        except ValueError as e:
            logging.warn("decrypt enc_data error:%s" % e)
        return enc_data



# if __name__ == '__main__':
#     for i in range(20):
#         val = "".join(random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()', i))
#         enc = crypto.encrypt(val)
#         print(len(val), len(enc), len(val)/len(enc))

