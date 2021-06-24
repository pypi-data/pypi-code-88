from cryptography.fernet import Fernet
from src.configuration import config
import logging

log = logging.getLogger(__name__)

global fernet


def read_fernet_key():
    try:
        if fernet is not None:
            return fernet
        else:
            key = config.read('security', 'FERNET_KEY')
            if not key:
                log.warning("Empty key")
    except Exception as e:
        log.error("error")
        raise


def genereta_fernet_object(key):
    fernet = Fernet(key)
    return fernet


def generete_key():
    # generate encryption key
    key = Fernet.generate_key()
    print("Key", key)
    return key


def encrypte_value(value):
    # encrypt
    if value is not None:
        token = fernet.encrypt(b"my message")
        print("Value:", token)
    else:
        print("Error value is None")


def decrypte_value(token):
    # decrypt
    if token is not None:
        fernet.decrypt(token)
        print("Value: ", fernet.decrypt(token))

# extract ttl
#print("TTL: ", fernet.extract_timestamp(token))