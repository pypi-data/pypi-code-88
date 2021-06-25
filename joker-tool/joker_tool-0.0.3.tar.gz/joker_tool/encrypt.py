# -*- coding: utf-8 -*-
"""                                 
File Name:  encrypt.py
Author:     Zsy
Place:      BeiJin
Time:       2021-03-03
"""
import hashlib
from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5


class Md5Encrypt(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_sign_data(self, data):
        """
        去除参数的值为空或者参数名为sign的数据，返回参与签名的字典类型数据
        :return:
        """
        signData = {}
        for key, value in data.items():
            # if key != "sign":
            if key != "sig" and key != "__NS_sig3" and key != "__NStokensig":
                signData[key] = value

        return signData

    def sign_string(self, signData, keyString=None):
        """
        对参数按照key=value的格式，并按照参数名ASCII字典序排序拼接成字符串stringA，最后拼接上key，返回拼接API密钥
        :return:
        """
        # 定义空列表
        list = []
        # 定义空字符串
        stringA = ""
        # 循环遍历字典数据的键值，取出存放到列表中
        for key in signData.keys():
            list.append(key)
        # 对列表的对象进行排序，默认升序，即按照ASCII码从小到大排序
        list.sort()
        # 循环遍历排序后的列表，根据键值取出字典键对应的值
        for i in list:
            stringA += i + "=" + signData[i] + "&"
        # 参数拼接成需要加密的字符串
        if keyString:
            stringA += keyString

        return stringA

    def start_main(self, data, keyString=None):
        """
        函数调用入口，MD5加密，返回加密后的字符串（小写和大写）
        :return:
        """

        # 调用GetSignData函数，获取参与签名的参数，返回新的字典数据
        signData = self.get_sign_data(data)
        # 调用函数，返回需要加密的字符串
        signBody = self.sign_string(signData, keyString)
        print(signBody)

        # 创建对象md
        md = hashlib.md5()
        # 对stringA字符串进行编码
        md.update(signBody.encode('utf-8'))
        # 数据加密
        signValue = md.hexdigest()
        # 把加密的结果，小写转换成大写，upper函数
        signValueUpper = signValue.upper()
        print(signValue, signValueUpper)
        return signValue, signValueUpper


class AESCBCEncrypt(object):
    """
    AES CEB 加解密
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = AES.MODE_CBC
        # 如果模式为ECB 则 iv 可以省略
        # self.mode = AES.MODE_ECB

    def base64_encrypt(self, text):
        """
        :param text: 需要加密的字符串
        :return: base64 加密后的16进制字符串
        """
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, self.vi)
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add).encode('utf-8')
        cipher_text = cryptor.encrypt(text)
        return base64.b64encode(cipher_text).decode()

    def hash_encrypt(self, text):
        """
        :param text: 需要加密的字符串
        :return: hash 加密后的16进制字符串
        """
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, self.vi)
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    def base64_decrypt(self, text):
        """
        # 解密后，去掉补足的空格用strip() 去掉
        :param text:加密后的字符串
        :return:解密后的 base64 编码的字符
        """
        cryptor = AES.new(self.key, self.mode, self.vi)
        decryptByts = base64.b64decode(text)
        plain_text = cryptor.decrypt(decryptByts)
        return bytes.decode(plain_text).rstrip('\0')

    def hash_decrypt(self, text):
        """
        # 解密后，去掉补足的空格用strip() 去掉
        :param text:加密后的字符串
        :return:解密后的 hash 编码的字符
        """
        cryptor = AES.new(self.key, self.mode, self.vi)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')

    def start_main(self, text, keyString, viByte):
        self.key = key.encode('utf-8')
        self.vi = bytes(viByte, encoding="utf8")
        res_hase_encrypt = self.hash_encrypt(text)
        res_base64_encrypt = self.base64_encrypt(text)
        print("hash加密后的字符串: ", res_hase_encrypt)
        print("base64加密后的字符串: ", res_base64_encrypt)
        return res_base64_encrypt, res_hase_encrypt


class AESECBEncrypt(object):
    """
    加密方式为AES   ECB pkcs7padding  Key C8t8ZV3ks7K3v73s 无iv base64  utf8
    """

    def __init__(self, key):
        self.key = key.encode('utf-8')  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)


class RSAEncrypt(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def encrypt(self, text, pub_key):
        """
        使用这个库时 pubkey 需要在公钥上下两行加上
        eg:
        "-----BEGIN PUBLIC KEY-----\n" + pub_key + "\n-----END PUBLIC KEY-----"
        :param text:
        :param pub_key:
        :return:
        """
        if "-----" not in pub_key:
            pub_key = "-----BEGIN PUBLIC KEY-----\n" + pub_key + "\n-----END PUBLIC KEY-----"
        rsa_key = RSA.importKey(pub_key)
        cipher = Cipher_pkcs1_v1_5.new(rsa_key)
        encrypt_text = base64.b64encode(cipher.encrypt((text).encode("utf-8"))).decode('utf8')
        return encrypt_text


if __name__ == '__main__':
    # 所有发送或者接收到的数据定义为字典类型数据
    # data = {
    #     "pageId": "1",
    #     "pageSize": "50",
    #     "top": "500",
    #     "mobileType": "",
    #     "startDate": "2021-02-24",
    #     "endDate": "2021-03-02",
    #     "type": "",
    #     "themes": "",
    #     "playRules": "",
    #     "artStyles": "",
    #     "productGroups": "",
    #     "chargesType": "",
    #     "tabType": "totalRanking",
    #     "thisTimes": "16146920619",
    # }
    # keyString = "key=OH_MY_LADY_GA_GA"
    # keyString = None
    # md5_encrypt = Md5Encrypt()
    # md5_encrypt.StartMian(data, keyString)

    p = AESCBCEncrypt()
    text = "{\"section_id\":\"19459\",\"last_id\":\"0\",\"device\":\"kbA57598CE63704C704822B99F15B73741\",\"device_system_version\":\"6.0.1\",\"ts\":\"1606025626\",\"app_version\":\"239\",\"cursor\":\"0\",\"device_name\":\"MuMu\",\"sort\":\"reply_time\",\"topic_list_type\":\"help\",\"app_name\":\"1.5.5.403\",\"level\":\"4\"}"
    key = "d@J%0WK8#znQ$PFH"
    vi = "C8t8ZV3ks7K3v73s"
    s = p.start_main(text, key, vi)

    print("加密:", s)

    # key = "C8t8ZV3ks7K3v73s"
    key = "oIJoTJaaCvBV6nCC"
    p = AESECBEncrypt(key)
    base_text = '{\"timestamp\":1624353454189,\"nonce\":1624353454189,\"appKey\":\"CuGsbe6HdAe6vDBHFew2Di\",\"accountType\":\"EMAIL\",\"loginName\":\"162880701@qq.com\",\"countryCallingCode\":\"\",\"password\":\"c603916c28b31be09e092e2df61210de\",\"deviceId\":\"7bf35ab133b57dd0ad53359a622268e2\",\"captchaTicket\":\"{\\\"success\\\":true,\\\"provider\\\":\\\"DINGXIANG\\\",\\\"result\\\":\\\"{\\\\\\\"ret\\\\\\\":0,\\\\\\\"ticket\\\\\\\":\\\\\\\"17A33029C594060AAA7CC8A6BFEEC943E4475B20D85412B08B735@bj:60cabc5acyW8SzI9N7dwDeEmsT7gcuxw3Q4gZPe1\\\\\\\"}\\\"}\",\"callbackUrl\":\"https://u.oppomobile.com/union/loginDirect\",\"processTicket\":\"\",\"agreeUpgrade\":\"false\",\"sign\":\"0f25632534229c10828613858a2b6367\"}'
    encrypt_text = "1Mmg0+Z3lF0Zpt8ma/AjXOlML/uEOt3z6i5LNMBtTMy27+kGsaY/lpFZFIYtBGU/19Bx4KuNgTQ70s3pWUDa2viIIRxoI/4jwV5A0YL0iV+8+UoSwAOEanwRSLdUIzmq1JeXtwYYwpc/pvlQOoemCv8ZsqGefE6huQ052ew1kJASR+IZFBgGpEA9J80XzdIXATpgKP4o1hW8H6iZIsq4Lzl20Sep+5m7vNfUW7hZ8qhJtsknUysK0bbPN2O9vDZLnC/FaCpmf8xDHevh/PD40XFgUEeXYLKkNgJy6JPScGWe/fv8jp4/8siU7oYJslJwb9oXkXNSu6Px82asYMaBKIafAxUGbd/ff+8ieo+Z0vNygSN63jMr0hKVUJyyILiw6i3Hm734auV33jM1uFbt4UnAvWNi49oRI6CTVScLiS9C7JqVHfOgbh7RBkkke90pjPEejktHW8DryrNLPU3QU/c7jkGZapOWNUyemtcI88+2rjdDYbdHviFvEDj+5PQpQ9H1QSjNwMfBan1kI7itU5FlgX3qc5+iTnLdxLHT860taQYNgHc+99iX3bA88c7XmrHfRutAPtc+hBkWE9VlPno73JIKycI0p3AfuBVNXb9tQ/HyAMPWRf2Zf8St5CexaDR+j/yeT+7uvwWENi8/Taz84pNpFV5VSJkSTL72K7F4dmdHXLzCvWS8MF32x/WFvcMOMAQPEd5/4yNlljBrJPtboGxZKC0iVzXMezYAtKgVXAAxea5a5iUjkZ/lpzbNfLD06NTS50qCPxDxD4FpcF/kPEJ7YNfyXJqDHWKUg11i0C+7u0jJoR4nSIk/tdZr"
    s = p.decrypt(encrypt_text)
    # s = p.encrypt(base_text)
    print(s)

    pass
