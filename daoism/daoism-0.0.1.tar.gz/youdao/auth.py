import time
import uuid
import hashlib


class Auth:
    @staticmethod
    def get_time():
        return str(int(time.time()))

    @staticmethod
    def get_salt():
        return str(uuid.uuid1())

    def __init__(self, key, secret) -> None:
        self.key = key
        self.secret = secret
        self.salt = Auth.get_salt()
        self.time = Auth.get_time()

    def _truncate(self, q):
        if q is None:
            return None
        size = len(q)
        return q if size <= 20 else q[0:10] + str(size) + q[size - 10 : size]

    def get_auth(self, q):
        time = self.time
        salt = self.salt
        signStr = f"{self.key}{self._truncate(q)}{salt}{time}{self.secret}"
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(signStr.encode("utf-8"))
        return {
            "sign": hash_algorithm.hexdigest(),
            'curtime': time,
            "salt": salt,
            "signType": "v3",
            "appKey": self.key,
        }
