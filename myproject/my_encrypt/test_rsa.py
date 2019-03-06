# -*- coding: UTF-8 -*-
import rsa
import base64

public_key_str = '''-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBAM+eZD23GY90oxptydeBdaTmVrXngy5eqXYRGTdYvhBO2nhlmFiZMobO
bH6gFbdtn5g/ugMUOoXlPk5nyUMw5VRcXTsVeu5PGbofvYtf67M03AAkRL44uGtB
NhUeqlq+yAU2y3KKwQVwjuiyPcdkhBWk3ZQnEMeKM6WLDXDnA2vbAgMBAAE=
-----END RSA PUBLIC KEY-----
'''
private_key_str = '''-----BEGIN RSA PRIVATE KEY-----
MIICYQIBAAKBgQDPnmQ9txmPdKMabcnXgXWk5la154MuXql2ERk3WL4QTtp4ZZhY
mTKGzmx+oBW3bZ+YP7oDFDqF5T5OZ8lDMOVUXF07FXruTxm6H72LX+uzNNwAJES+
OLhrQTYVHqpavsgFNstyisEFcI7osj3HZIQVpN2UJxDHijOliw1w5wNr2wIDAQAB
AoGAa7eP5n0i48zt+n5PpGHkeaOQBVySMPKoFTuVy6NdKPTgYGrFeeIx1sMugxvn
aH2VudYGWiaannFrvB4YV/EPcXDyW47kPq6tlDF6qBtV/ZHhVo5MBgUT4gyJBaSZ
uUlxqUvr3OKIW79rD0MVT4rfEzJ5ML1z851oKUCO+mq/ptECRQDfA9jbl9wPW5Bf
QOvy8s01A+4PMfvF9d3ecKx6BaTsu+Uc26R49i18P7LrKwRzWWrOIdofJso6Xc8/
nFwWMd3qN7vq/QI9AO5TlasNsu7Zh3J/nf71DZI5O3tFsIOS+9qvYpy6g3cui/II
UwL6HJplc0gGiFeZZq53lLsYcgto6s2FtwJEE87mqxKA9EhAuYUtr+WK/oN72JOq
9jlRXJmLaEcqD/Dcd8S2hhvvjFKoFKU8fvZZOzfchNnQKoD8kHzV3Q7O1CfhJA0C
PQCr0IhzA/I+rYYvbn9qAiKhiy8tpMUnZfy54Hz4PqJudpkfiQ7Hc6bRTFg60bLT
bF0RZFZON8ZoIWA9gKsCRQCvMe5QYkPe7k1IL1mI1582ukCDU11dAZL4r0ytWBp4
CkgmwX7iGvRn+CLRc1avGY08tJgnhdVMibwvSVH0ltWd2q+BoA==
-----END RSA PRIVATE KEY-----'''
private_key = rsa.PrivateKey.load_pkcs1(private_key_str)
public_key = rsa.PublicKey.load_pkcs1(public_key_str)
msg = "abc123"

encrypt_msg = base64.encodestring(rsa.encrypt(msg, public_key))
decrypt_msg = rsa.decrypt(base64.decodestring(encrypt_msg), private_key)
print(chr(10) + "原始文本:")
print(msg)
print(chr(10) + "加密后的文本:")
print(encrypt_msg)
print(chr(10) + "解密后的文本:")
print(decrypt_msg)
