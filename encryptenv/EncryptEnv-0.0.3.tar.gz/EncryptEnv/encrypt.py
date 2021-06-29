import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key().decode()

def restore_key(key, entrypted_msg):
    entrypted_msg=entrypted_msg.encode()
    f = Fernet(key)
    decrypted_message = f.decrypt(entrypted_msg)
    res=decrypted_message.decode()
    return res

def encyrpt_key(key, msg):
    encoded_message = msg.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message).decode()
    return encrypted_message