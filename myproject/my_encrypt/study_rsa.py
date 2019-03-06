# coding=utf-8
import rsa
import base64


class rsa_helper():
    def __init__(self):
        self.private_key = '''-----BEGIN RSA PRIVATE KEY-----
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
        self.public_key = '''-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBAM+eZD23GY90oxptydeBdaTmVrXngy5eqXYRGTdYvhBO2nhlmFiZMobO
bH6gFbdtn5g/ugMUOoXlPk5nyUMw5VRcXTsVeu5PGbofvYtf67M03AAkRL44uGtB
NhUeqlq+yAU2y3KKwQVwjuiyPcdkhBWk3ZQnEMeKM6WLDXDnA2vbAgMBAAE=
-----END RSA PUBLIC KEY-----
'''

    def encrypt(self, text):
        public_key = rsa.PublicKey.load_pkcs1(self.public_key)
        encrypt_msg = base64.encodestring(rsa.encrypt(text, public_key))
        return encrypt_msg

    def decrypt(self, encrypt_text):
        private_key = rsa.PrivateKey.load_pkcs1(self.private_key)
        try:
            decrypt_msg = rsa.decrypt(base64.decodestring(encrypt_text), private_key)
        except Exception as e:
            return e.message
        return decrypt_msg


if __name__ == '__main__':
    helper = rsa_helper()
    encrypt_text = helper.encrypt('123456')
    print encrypt_text
    encrypt_text = '''k1+vUC5iwDbLL52F8LGFfJH0aiVxJbhg/O5BERb6v/7KAlFY0MqNLXQrP8ClsZwkd98G2Ri5ewyFWI5mcuLHsZme1ixLHqynhvoKjtDk7Xnsjj+exQmdpZHRjkxv/8U+OMgaGMZ5hcltz5Qr2rvwEU/LYGJOVyTYJX7jSqebECk='''
    decrypt_text = helper.decrypt(encrypt_text)
    print decrypt_text
