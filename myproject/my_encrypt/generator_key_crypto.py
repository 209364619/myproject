# coding=utf-8
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
import rsa


class rsa_helper():

    def generator_key(self, ):
        random_generator = Random.new().read
        rsa = RSA.generate(1024, random_generator)

        private_pem = rsa.exportKey()
        print('私钥：')
        print(private_pem)

        # with open('master-private.pem', 'wb') as f:
        #     f.write(private_pem)

        public_pem = rsa.publickey().exportKey()
        print("公钥：")
        print(public_pem)
        # with open('master-public.pem', 'wb') as f:
        #     f.write(public_pem)
        dict = {"public": public_pem, "private": private_pem}
        return dict

    def use_encrypt(self, text, public_key):
        # 公钥加密数据
        rsakey_pub = RSA.importKey(public_key)
        cipher = PKCS1_v1_5.new(rsakey_pub)
        encrypt_text = base64.encodestring(cipher.encrypt(text))
        return encrypt_text

    def use_decrypt(self, encrypt_text, private_key):
        # 私钥解密
        rsakey_private = RSA.importKey(private_key)
        cipher = PKCS1_v1_5.new(rsakey_private)
        origin_text = cipher.decrypt(base64.decodestring(encrypt_text), 'ERROR')
        return origin_text


if __name__ == '__main__':
    helper = rsa_helper()
    with open('test.pem', 'rb') as key_buff:
        key_private = key_buff.read()
        key_public = '''-----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDiRK/s+kYoIVo+S36lnyjtmZ2V
        A3XKOGr2fNJDwo8P8mwE6YFYLhe8QIqGtj5kaxHXLzbEK8vUvI1yQphBAdEwtZ7y
        vl9VGcMH+VvnuBtyrpsPg+ncCqbYoF1Spe2+6nMSvDiWd+7zQSm5g7YYPIefwKq1
        fJ70HGIMU2++IliAxwIDAQAB
        -----END PUBLIC KEY-----
        '''
        text = "123"
        mi = helper.use_encrypt(text, public_key=key_public)
        print mi
        mi = '''Lh+G4NTOEk8G1ej7MOn7Iz+LH4C7RdT3KDPIyuonSFaFQRwxsj9BH1pbBgpr1GPJAKVbmehc4eskjRkCDr4hjELbknvlFrxW3Pp1qcuUB1gsKo3hp5zjWCnIlCePvRCKdhZ79vShEE08Hck7HiApCAXGVks5M//n0G7ehXvEJH8='''
        origin = helper.use_decrypt(mi, private_key=key_private)
        print origin
