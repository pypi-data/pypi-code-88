from __future__ import annotations

import base64
import hashlib
import os.path as Path
import pickle
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from enum import Enum


class DataStore:
    """ Persistent and portable serialized data store. """

    __author__ = "kakaiba-talaga"
    __version__ = "1.0.2"
    __license__ = "GPL-3.0-or-later"
    __url__ = "https://github.com/kakaiba-talaga/pyDataStore"

    # Default file data store.
    fileDataStore = "data.store"

    # The highest protocol version is 5 which can be used in Python >= 3.8.
    # Protocol version 4, Python >= 3.4. This is the default protocol for Python >= 3.8.
    # Protocol version 3, Python >= 3.0. This is the default protocol for Python >= 3.0.
    protocol = pickle.HIGHEST_PROTOCOL

    # AES specific variables.
    aesBlockSize = AES.block_size
    aesMode = AES.MODE_CFB

    def __init__(self, fileDataStore: str = None, cipher = None, aesKey: str = None):
        """
        Persistent and portable serialized data store.

        A Python `dict` object that has been `dump`-ed can be `load`-ed in the future. The object can be encoded using `Base64` or `AES`.

        `fileDataStore` = Location of the file to use as data store. Default is `data.store` or `./data.store`.

        `cipher` = Instance of the `Cipher` Enum. Either `Cipher.Base64` (default) or `Cipher.AES`

        `aesKey` = A string that will be used as the secret key in encoding. Required only be used when `cipher` is set to `Cipher.AES`.

        ---

        GitHub Repository: https://github.com/kakaiba-talaga/pyDataStore
        """

        self.fileDataStore = self.fileDataStore if fileDataStore in [None, ""] else fileDataStore
        self.fileDataStore = Path.abspath(self.fileDataStore)

        # This will only be used if `cipher` is set to Cipher.AES.
        self.cipher = Cipher.Default if (cipher in [None, ""] or not isinstance(cipher, Cipher)) else cipher

        # AES supports multiple key sizes: 16 (AES128), 24 (AES192), or 32 (AES256).
        # This will output a key size of 32 bytes.
        self.aesKey = hashlib.sha256(aesKey.encode("utf-8")).digest() if (cipher != None and isinstance(cipher, Cipher) and cipher == Cipher.AES and aesKey not in [None, ""]) else ""

    def dump(self, inObjDict: dict):
        """
        This will store the `dict` object in the data store. If the object already exists, it will be overwritten.

        `inObjDict` should be a `dict` following this format:

        ```
        {
            "object": "OBJECT_NAME",
            "data": {
                "DATA_KEY": "DATA_VALUE",
                "DATA_KEY": "DATA_VALUE",
                ...
            }
        }
        ```

        Every `DATA_VALUE` will automatically be encoded either by `Cipher.Base64` or `Cipher.AES`.

        If the keys `object` and `data` are missing, this will return `False`.
        """

        if (not self.__validate(inObjDict)):
            raise Exception("This dict object has an invalid format.")

        newData = []
        inObjDict = self.__iterate(inObjDict)
        fileExist = Path.isfile(self.fileDataStore)

        try:
            fileMode = "rb+" if fileExist else "wb"
            dbFile = open(self.fileDataStore, fileMode)

            if (fileExist):
                objExists = False

                while True:
                    try:
                        lineObj = pickle.load(dbFile)

                        if (lineObj["object"] == inObjDict["object"]):
                            objExists = True
                            lineObj = inObjDict

                        newData.append(lineObj)
                    except EOFError:
                        break

                if (objExists):
                    dbFile.seek(0)
                    dbFile.truncate()

                    for datum in newData:
                        pickle.dump(datum, dbFile, self.protocol)
                else:
                    pickle.dump(inObjDict, dbFile, self.protocol)
            else:
                pickle.dump(inObjDict, dbFile, self.protocol)

            dbFile.close()
        except Exception as error:
            raise Exception(error)

    def __iterate(self, objDict: dict, encode: bool = True):
        dataDict = objDict["data"]
        func = self.__encode if encode else self.__decode

        for key in dataDict:
            dataDict[key] = func(dataDict[key])

        return objDict

    def __validate(self, objDict: dict):
        """
        Validate if the `objDict` is following the correct format.
        
        `objDict` should be a `dict` following this format:

        ```
            {
                "object": "OBJECT_NAME",
                "data": {
                    "DATA_KEY": "DATA_VALUE",
                    "DATA_KEY": "DATA_VALUE",
                    ...
                }
            }
        ```
        """

        valid = False

        if ("object" in objDict and "data" in objDict):
            valid = True

        return valid

    def __encode(self, datum: str):
        """ This will `base64` encode `datum` by default. """

        return self.__encode_base64(datum) if self.cipher in [Cipher.Default, Cipher.Base64] else self.__encode_aes(datum)

    def __encode_base64(self, raw: str | bytes):
        rawCheck = raw if type(raw) is bytes else raw.encode("utf-8").strip()

        return base64.b64encode(rawCheck)

    def __encode_aes(self, raw : str):
        pad = lambda s: s + ((self.aesBlockSize - len(s)) % self.aesBlockSize) * chr((self.aesBlockSize - len(s)) % self.aesBlockSize)
        rawBase64Encoded = self.__encode_base64(pad(raw))
        iv = get_random_bytes(self.aesBlockSize)
        cipher = AES.new(key=self.aesKey, mode=self.aesMode, iv=iv)

        return self.__encode_base64(iv + cipher.encrypt(rawBase64Encoded))

    def __decode(self, datum: bytes):
        """ This will decode the `base64` encoded `datum` by default. """

        return self.__decode_base64(datum) if self.cipher in [Cipher.Default, Cipher.Base64] else self.__decode_aes(datum)

    def __decode_base64(self, datum: bytes, decodeEncoding: bool = True):
        return base64.b64decode(datum).decode("utf-8") if decodeEncoding else base64.b64decode(datum)

    def __decode_aes(self, datum: bytes):
        unpad = lambda s: s[:-ord(s[-1:])]
        datum = self.__decode_base64(datum, False)

        # Initialization vector.
        iv = datum[:self.aesBlockSize]

        # Payload.
        payload = datum[self.aesBlockSize:]

        cipher = AES.new(key=self.aesKey, mode=self.aesMode, iv=iv)

        return unpad(self.__decode_base64(cipher.decrypt(payload)))

    def load(self, objName: str):
        """ This will retrieve the `dict` object of the `objName` if it exists. Otherwise, this will return `None`."""

        returnObj = None

        if (Path.isfile(self.fileDataStore)):
            dbFile = open(self.fileDataStore, "rb")

            while True:
                try:
                    lineObj = pickle.load(dbFile)

                    if (lineObj["object"] == objName):
                        returnObj = self.__iterate(lineObj, False)
                        break
                except EOFError:
                    break

            dbFile.close()
        else:
            raise Exception(f"The specified data store, {self.fileDataStore}, cannot be found.")

        return returnObj

    def destroy(self):
        """ If the data store exists, this will delete all objects and will return `True`. Otherwise, this will return `False`. """

        returnStatus = False
        fileExist = Path.isfile(self.fileDataStore)

        if (fileExist):
            with open(self.fileDataStore, "rb+") as dbFile:
                dbFile.truncate()

            returnStatus = True

        return returnStatus

    def version(self):
        return self.__version__

    def author(self):
        return self.__author__

    def license(self):
        return self.__license__

    def github_url(self):
        return self.__url__


class Cipher(Enum):
    """
    Cipher enumerations.
    
    `Default` - `Base64`

    `Base64` - Base64 encoding.

    `AES` - AES encoding.
    """

    Default = "base64"
    Base64 = "base64"
    AES = "aes"
