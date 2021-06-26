import requests
import json
import base64
# import profitmart.utils

URL = 'http://mobile.profitmart.in/NestHtml5Mobile/rest'

import base64
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import serialization,hashes

def encryptKey(publickey,data):
	start = 0
	end = 53
	if 53 > len(data):
		end = len(data)
	enc=''
	while end < len(data):
		enc += base64.b64encode(publickey.encrypt(data[start:end],padding.PKCS1v15())).decode()
		enc += '\n'
		start = end
		end += 53
		if end > len(data):
			end = len(data)
	if end - start > 0:
		enc += base64.b64encode(publickey.encrypt(data[start:end],padding.PKCS1v15())).decode()
		enc += '\n'
	return base64.b64encode(enc.encode()).decode()

def decryptKey(privatekey,data):
	data = base64.b64decode(data).split(b'\n')
	data.pop()
	decrypted=''
	for dt in data:
		decrypted += privatekey.decrypt(base64.b64decode(dt),padding.PKCS1v15()).decode()
	return decrypted

def getHash(data):
	h = hashes.Hash(hashes.SHA256())
	h.update(data)
	return h.finalize().hex()

def getPubKeyFromPem(pem):
	return serialization.load_pem_public_key(pem)

def getPemFromPubKey(pubkey):
	return pubkey.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)

def getPemFromPriKey(prikey):
	return prikey.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.TraditionalOpenSSL,encryption_algorithm=serialization.NoEncryption())
	

def getPublicKey(url,uid,appid,secret):
	body = {'uid':uid,'appid':appid,'secret':secret}
	response = requests.post(url,json=body)
	response = response.json()
	# print(response)
	if response['stat'] == 'ok':
		publicKey = getPubKeyFromPem(response['token'].encode())
		publicKey_hash = getHash(response['token'].encode())
		tomcatCount = response['tomcatCount']
		token = response['token']
		session = response['session']
		return (publicKey, publicKey_hash, tomcatCount, token, session)
	else:
		print(response['message'])
		return None

# Post method..
def POST(functionName, json_data, key, tomcatCount):
    response = requests.post(URL+functionName+"?jsessionid=" + "." + tomcatCount + "&jData=" + json_data + "&jKey=" + key + "")
    r = response.json()
    res_dict = json.loads(json.dumps(r))

    return res_dict

# Get Default login...
def getClientData(uid, publicKey4, publicKey4_hash,tomcatCount):
    data_json = json.dumps({'uid': uid})
    response = POST('/DefaultLogin', encryptKey(publicKey4,
                    data_json.encode()), publicKey4_hash, tomcatCount)
    return response

